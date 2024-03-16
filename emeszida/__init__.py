from lark import Lark
from lark import Transformer, Discard

from .sexagesimal import Sexagesimal
from .program import *

EmeszidaParser = Lark(r"""
    ?tablet: "𒁾" "\n" block* colophon

    block: stmt* "---" "\n"

    stmt: args TAB+ OPCODE TAB+ destination TAB+ line_number "\n"
        | "#" /[^\n]/* "\n" -> comment

    args: expr (DELIM? expr)*

    destination: register
                | number
                | EMPTY_REGISTER
    EMPTY_REGISTER: "𒋤"

    expr: number
         | register

    number: (digits* FRAC)? digits+

    register: "𒃻𒋃" expr "𒄰"

    OPCODE: "𒈭𒄩" // add
          | "𒁀𒍣" // subtract
          | "𒀀𒁺" // multiply
          | "𒅆"  // reciprocal
          | "𒈨"  // assign
          | "𒋫𒈥" // print
          | "𒇔𒈾" // goto
          | "jz" // jz

    line_number: number

    // ?colophon: location copy_status authorship date WS*
    // TODO: Are there stock phrases that should be used in the colophon?
    colophon: "colophon" WS* // Placeholder

    // Delimiters:

    DELIM: _DELIM
    _DELIM: "𒀀𒈾"
          | "𒄿𒈾"
          | "  "

    TAB: "\t"
       | "𒋰"

    // Numerals:

    digits: TENS ONES
          | ONES
          | TENS
          | ZERO
          | SPACE
    
    TENS: /[𒌋𒎙𒌍𒐏𒐐]/

    ONES: /[𒐕𒐖𒐗𒐘𒐙𒐚𒐛𒐜𒐝]/

    ZERO: "𒑱"

    FRAC: "𒋙"

    SPACE: " "

    %import common.WS
    """, start='tablet', parser="lalr")

class EmeszidaTransformer(Transformer):
    def tablet(self, args):
        blocks, colophon = args[:-1], args[-1]
        return Program(blocks, colophon)

    def block(self, stmts):
        return stmts

    def stmt(self, value):
        (args, opcode, destination, line_number) = value
        return Statement(args, opcode, destination, line_number)

    def line_number(self, value):
        (value,) = value
        return value

    def args(self, value):
        return value

    def destination(self, value):
        (value,) = value
        return value

    def expr(self, value):
        (value,) = value
        return value

    def register(self, value):
        (value,) = value
        if isinstance(value, Register):
            return Register(value)
        else:
            return Register(tuple(value.digits))

    def EMPTY_REGISTER(self, value):
        return None

    def number(self, digits):
        try:
            radix_point = digits.index('𒋙')
            digits = digits[:radix_point] + digits[radix_point+1:]
        except:
            radix_point = len(digits)
        exponents = [radix_point - idx - 1 for idx, digit in enumerate(digits)]
        value = Sexagesimal(list(zip(digits, exponents)))
        return value

    def digits(self, digits):
        if digits != []:
            return sum(digits)
        else:
            return Discard

    def ZERO(self, _):
        return 0

    def ONES(self, token):
        match token:
            case "𒐕":
                return 1
            case "𒐖":
                return 2
            case "𒐗":
                return 3
            case "𒐘":
                return 4
            case "𒐙":
                return 5
            case "𒐚":
                return 6
            case "𒐛":
                return 7
            case "𒐜":
                return 8
            case "𒐝":
                return 9

    def TENS(self, token):
        match token:
            case "𒌋":
                return 10
            case "𒎙":
                return 20
            case "𒌍":
                return 30
            case "𒐏":
                return 40
            case "𒐐":
                return 50

    def FRAC(self, _):
        return _.value

    def SPACE(self, _):
        return Discard
    
    ############################
    # Whitespace and delimiters:

    def comment(self, _):
        return Discard

    def TAB(self, _):
        return Discard

    def WS(self, _):
        return Discard
    
    def DELIM(self, _):
        return Discard
    
    def _DELIM(self, _):
        return Discard
