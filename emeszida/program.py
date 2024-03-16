from .sexagesimal import Sexagesimal

class Program(object):
    def __init__(self, blocks, colophon):
        self.registers = dict()
        self.lines = []
        self.line_lookup = dict()
        for block in blocks:
            for line in block:
                line_number = tuple(line.line_number.digits)
                self.lines.append(line)
                self.line_lookup[line_number] = len(self.lines) - 1
        self.colophon = colophon

    def __str__(self):
        return str(self.lines)

    def dereference(self, register):
        if isinstance(register, Sexagesimal):
            return tuple(register.digits)

        depth = 0
        address = register.address
        while isinstance(address, Register):
            address = address.address
            depth += 1
        result = self.registers[address]
        while depth > 0:
            result = self.registers[tuple(result.digits)]
            depth -= 1
        return result

    def execute(self):
        line_number = 0
        while line_number < len(self.lines):
            stmt = self.lines[line_number]
            print(f"Executing {line_number}: {stmt}")
            result = stmt.execute(self)
            if stmt.opcode == "𒇔𒈾": # Goto
                if isinstance(result, Register):
                    result = self.dereference(result.address)
                line_number = self.line_lookup[tuple(result.digits)]
            elif stmt.opcode == "jz": # jz
                if result:
                    if isinstance(result, Register):
                        result = self.dereference(result.address)
                    line_number = self.line_lookup[tuple(result.digits)]
                else:
                    line_number += 1
            else:
                if stmt.destination != None:
                    dest = stmt.destination.address
                    if isinstance(dest, Register):
                        dest = self.dereference(dest)
                        dest = tuple(dest.digits)
                    self.registers[dest] = result
                line_number += 1
            print("Registers:")
            for address, value in self.registers.items():
                print(f"\t{address}: {value}")
            print()

class Statement(object):
    def __init__(self, args, opcode, destination, line_number):
        self.args = args
        self.opcode = opcode
        self.destination = destination
        self.line_number = line_number

    def __repr__(self):
        return f"{self.opcode}({self.args}) -> {self.destination}"
    def __str__(self):
        return f"LINE {self.line_number} | {self.opcode}({self.args}) => {self.destination}"

    def 𒈭𒄩(self, args):
        # Addition
        total = args[0]
        for arg in args[1:]:
            total += arg
        return total

    def 𒁀𒍣(self, args):
        # Subtraction
        total = args[-1]
        for arg in args[:-1][::-1]:
            total -= arg
        return total

    def 𒀀𒁺(self, args):
        # Multiplication
        total = args[0]
        for arg in args[1:]:
            total *= arg
        return total

    def 𒅆(self, arg):
        # Reciprocal
        assert len(arg) == 1
        (arg,) = arg
        return arg.reciprocal()

    def 𒈨(self, arg):
        # Assignment
        assert len(arg) == 1
        (arg,) = arg
        return arg

    def 𒋫𒈥(self, args):
        # Print
        print("Print", *args)

    def 𒇔𒈾(self, arg):
        # Goto
        assert len(arg) == 1
        (arg,) = arg
        return arg

    def jz(self, arg):
        # Jump if zero
        assert len(arg) == 1
        (arg,) = arg
        if arg == Sexagesimal([(0,0)]):
            return self.destination

    def execute(self, context):
        method = getattr(self, self.opcode)
        inputs = [
            context.dereference(arg)
            if isinstance(arg, Register) 
            else arg 
            for arg in self.args
        ]
        return method(inputs)


class Register(object):
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"Register{str(self.address)}"

