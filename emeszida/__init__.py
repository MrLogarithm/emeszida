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
         | recip
         | number
         | NAME
         | function_call
         | "(" expr ")"

    add: expr "𒀀𒈾" expr "𒈭𒄩"

    sub: expr "𒄿𒈾" expr "𒁀𒍣"

    mul: expr "𒀀𒁺" expr

    recip: "𒅆" expr

    function_call: "𒍦" (expr "𒅇")* expr? "𒍧" NAME "do"


    ?expression_stmt: expr

    NAME: /[a-z]+/

    assignment_stmt: NAME "=" expr

    loop_stmt: "loop" block "until" expr

    function_def_stmt: NAME "func" NAME* "take" block "def"

    print_stmt: expr "print"


    block: "𒍦" stmt* "𒍧"

    ?stmts: stmt*

    ?stmt: expression_stmt
         | assignment_stmt
         | loop_stmt
         | function_def_stmt
         | print_stmt

    %import common.WS
    %ignore "  "

    """, start='stmts', parser="lalr")


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

    def recip(self, term):
        (term,) = term
        return term.reciprocal()

    def expr_(self, _):
        (_,) = _
        return _
    def expr(self, _):
        (_,) = _
        return _

    def NAME(self, _):
        return _.value

    #def assignment_stmt(self, stmt):
        # TODO get current scope and store value
        #variable, expr = stmt
        #print(variable, expr)

    #def print_stmt(self, expr):
        #print(expr)

