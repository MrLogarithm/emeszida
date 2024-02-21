# http://norvig.com/lispy.html
# http://norvig.com/lispy2.html
# numerals
# operations

# Type definitions

# inim "word" = Symbol
𒅗 = str
# šid "number" = Number
𒋃 = (int, float)
# mu "name" = Atom
𒈬 = (𒅗, 𒋃)
# da "edge" = List
𒁕 = list
# ir₃ "expression" = Expression
𒀴 = (𒈬, 𒁕)
# sa₂ "to be equal" = Env
𒁲 = dict

# (tab (pad₃ ))
program = "𒍦𒋰𒍦𒅆𒊒 𒊏 𒌋𒍧𒍦𒆰 𒁹𒁹𒁹𒋙𒌋𒁹𒁹𒁹𒁹𒍦𒆰 𒊏 𒊏𒍧𒍧𒍧"



def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace("𒍦", " 𒍦 ").replace("𒍧", " 𒍧 ").split()


def parse(program: str) -> 𒀴:
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))


def read_from_tokens(tokens: list) -> 𒀴:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError("unexpected EOF")
    token = tokens.pop(0)
    if token == "𒍦":
        L = []
        while tokens[0] != "𒍧":
            L.append(read_from_tokens(tokens))
        tokens.pop(0)  # pop off ')'
        return L
    elif token == "𒍧":
        raise SyntaxError("unexpected 𒍧")
    else:
        return atom(token)

# numbers, places separated by tar 𒃵, below a whole number separated by šu2 𒋙

class num(object):
    def __init__(self, s):
        self.initial_string = s
        self.sign = 1 # always positive for now
        self.value = [[0], [0]] # first element is > 1, second is < 1
        if "𒋙" in s:
            gt_one, lt_one = s.split("𒋙")
            values = []
            for value in lt_one.split("𒃵"):
                tens = value.count("𒌋")
                ones = value.count("𒁹")
                values.append(tens+ones)
            self.value[1] = values
            values = []
            for value in gt_one.split("𒃵"):
                tens = value.count("𒌋")
                ones = value.count("𒁹")
                values.append(tens+ones)
            self.value[0] = values
        else:
            values = []
            for value in s.split("𒃵"):
                tens = value.count("𒌋")
                ones = value.count("𒁹")
                values.append(tens*10+ones)
            self.value[0] = values

    def __str__(self):
        return self.initial_string

    def __repr__(self):
        return self.value




def parse_number(number: str):
    tens = number.count("𒌋")
    ones = number.count("𒁹")
    return tens + ones

def parse_full_number(number: str):
    number = 0
    if "𒋙" in number:
        # we have a float
        [gt_one, lt_one] = number.split("𒋙")
        for power, unit in enumerate(lt_one.split("𒃵")):
            unit = parse_number(unit)
            number += unit*(60**(-1*(pow+1)))
        for power, unit in enumerate(reversed(gt_one.split("𒃵"))):
            unit = parse_number(unit)
            number += unit*(60**(pow))
    else:
        for power, unit in enumerate(reversed(number.split("𒃵"))):
            unit = parse_number(unit)
            number += unit*(60**(pow))
    return number




def atom(token: str) -> 𒈬:
    "Numbers become numbers; every other token is a symbol."
    if token[0] in ["𒁹", "𒌋"]:
        # number
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return 𒅗(token)
