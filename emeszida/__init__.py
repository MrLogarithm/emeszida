from lark import Lark
from lark import Transformer, Discard

# TODO accept both GESH2 and DISH?
EmeszidaParser = Lark(r"""
    TENS: /[𒌋𒎙𒌍𒐏𒐐]/

    ONES: /[𒐕𒐖𒐗𒐘𒐙𒐚𒐛𒐜𒐝]/

    ZERO: "𒑱"

    FRAC: "𒋙"

    digits: TENS ONES
          | ONES
          | TENS
          | ZERO
    
    number: (digits* FRAC)? digits+


    ?expr: expr_ WS*

    ?expr_: add
         | sub
         | number

    add: expr expr "+"

    sub: expr expr "-"


    PRINT: "print"

    print_stmt: expr PRINT

    ?stmt: expr
         | print_stmt


    %import common.WS

    """, start='stmt', parser="lalr")

class Sexagesimal(object):
    def __init__(self, digits):
        """
        digits should be a list of (mantissa, exponent) tuples, e.g.
        [(2, 1), (0, 0), (3, -1)], representing 
        2x60^1 + 0x60^0 + 3*60^-1 = 120.05 = 𒐕𒐕𒑱𒋙𒐕𒐕𒐕
        """
        self.digits = digits

    def __eq__(self, other):
        return self.digits == other.digits

    def zero_pad(self, other):
        """
        Given another Sexagesimal object, zero-pad both so they
        have the same number of significant digits:
        """
        a = self.digits
        b = other.digits
        # Prepend most significant digit:
        while (a_max_exp := a[0][1]) < (b_max_exp := b[0][1]):
            a = [(0, a_max_exp+1)] + a
        while (a_max_exp := a[0][1]) > (b_max_exp := b[0][1]):
            b = [(0, b_max_exp+1)] + b
        # Append least significant digit:
        while (a_min_exp := a[-1][1]) > (b_min_exp := b[-1][1]):
            a = a + [(0, a_min_exp-1)]
        while (a_min_exp := a[-1][1]) < (b_min_exp := b[-1][1]):
            b = b + [(0, b_min_exp-1)]
        return a, b

    def __add__(self, other):
        a, b = Sexagesimal.zero_pad(self, other)
        # TODO carry in case of overflow
        result = Sexagesimal([(a_mantissa + b_mantissa, exp) for (a_mantissa, exp), (b_mantissa, _) in zip(a, b)])
        return result

    def __sub__(self, other):
        raise NotImplementedError()

    def __repr__(self):
        return str(self)

    def __str__(self):
        # (mantissa, exponent) representation:
        return str(self.digits)
        # decimal representation:
        # return str(sum(mantissa * 60**exponent for mantissa, exponent in self.digits))

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

    def digits(self, digits):
        return sum(digits)

    def FRAC(self, _):
        return _.value

    def add(self, terms):
        a, b = terms
        return a + b

    def sub(self, terms):
        a, b = terms
        return a - b

    def expr_(self, _):
        (_,) = _
        return _
    def expr(self, _):
        (_,) = _
        return _

    def print_stmt(self, stmt):
        expr, _ = stmt
        print(expr)

