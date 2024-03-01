from lark import Lark
from lark import Transformer, Discard

from .sexagesimal import Sexagesimal

# TODO accept both GESH2 and DISH?
EmeszidaParser = Lark(r"""
    TENS: /[𒌋𒎙𒌍𒐏𒐐]/

    ONES: /[𒐕𒐖𒐗𒐘𒐙𒐚𒐛𒐜𒐝]/

    ZERO: "𒑱"

    FRAC: "𒋙"

    SPACE: " "

    digits: TENS ONES
          | ONES
          | TENS
          | ZERO
          | SPACE
    
    number: (digits* FRAC)? digits+



    ?expr: add
         | sub
         | mul
         | number
         // | VARIABLE
         // | function_call

    add: expr "𒀀𒈾" expr "𒈭𒄩"

    sub: expr "𒄿𒈾" expr "𒁀𒍣"

    mul: expr "𒀀𒁺" expr


    ?expression_stmt: expr

    VARIABLE: /[a-z]+/

    assignment_stmt: VARIABLE "=" expr

    // loop_stmt: "do" block "until" condition 
    // function_def_stmt: "do" block "until" condition 

    PRINT: "print"

    print_stmt: expr PRINT


    ?stmt: expression_stmt
         | assignment_stmt
         | print_stmt

    %import common.WS
    %ignore "  "

    """, start='stmt', parser="lalr")


class EmeszidaTransformer(Transformer):
    def WS(self, _):
        return Discard

    def number(self, digits):
        try:
            radix_point = digits.index('𒋙')
            digits = digits[:radix_point] + digits[radix_point+1:]
        except:
            radix_point = len(digits)
        exponents = [radix_point - idx - 1 for idx, digit in enumerate(digits)]
        value = Sexagesimal(list(zip(digits, exponents)))
        return value

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

    def digits(self, digits):
        if digits != []:
            return sum(digits)
        return Discard

    def add(self, terms):
        a, b = terms
        return a + b

    def sub(self, terms):
        a, b = terms
        return b - a

    def mul(self, terms):
        a, b = terms
        return a * b

    def expr_(self, _):
        (_,) = _
        return _
    def expr(self, _):
        (_,) = _
        return _

    def VARIABLE(self, _):
        return _.value

    #def assignment_stmt(self, stmt):
        # TODO get current scope and store value
        #variable, expr = stmt
        #print(variable, expr)

    def print_stmt(self, stmt):
        expr, _ = stmt
        print(expr)

