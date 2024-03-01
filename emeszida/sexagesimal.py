class Sexagesimal(object):
    def __init__(self, digits):
        """
        digits should be a list of (mantissa, exponent) tuples, e.g.
        [(2, 1), (0, 0), (3, -1)], representing
        2x60^1 + 0x60^0 + 3*60^-1 = 120.05 = 𒐖𒑱𒋙𒐗
        """
        self.digits = Sexagesimal.normalize(digits)

    def zero_pad(self, other):
        """
        Given another Sexagesimal object, zero-pad both so they
        have the same number of significant digits:
        """
        a = self.digits
        b = other.digits
        # Prepend most significant digit:
        while (a_max_exp := a[0][1]) < (b_max_exp := b[0][1]):
            a = [(0, a_max_exp + 1)] + a
        while (a_max_exp := a[0][1]) > (b_max_exp := b[0][1]):
            b = [(0, b_max_exp + 1)] + b
        # Append least significant digit:
        while (a_min_exp := a[-1][1]) > (b_min_exp := b[-1][1]):
            a = a + [(0, a_min_exp - 1)]
        while (a_min_exp := a[-1][1]) < (b_min_exp := b[-1][1]):
            b = b + [(0, b_min_exp - 1)]
        return a, b

    def normalize(digits):
        carry = 0
        for idx in range(len(digits) - 1, -1, -1):
            mantissa, exponent = digits[idx]
            if carry:
                mantissa += carry
            if mantissa >= 60:
                mantissa -= 60
                carry = 1
            elif mantissa < 0:
                mantissa += 60
                carry = -1
            else:
                carry = 0
            digits[idx] = (mantissa, exponent)

        if carry:
            digits = [(carry, exponent + 1)] + digits

        # trim empty positions
        while digits[0][0] == 0 and digits[0][1] > 0:
            digits = digits[1:]
        while digits[-1][0] == 0 and digits[-1][1] < 0:
            digits = digits[:-1]

        return digits

    def __eq__(self, other):
        return self.digits == other.digits

    def __add__(self, other):
        a, b = Sexagesimal.zero_pad(self, other)
        result = Sexagesimal(
            [
                (a_mantissa + b_mantissa, exp)
                for (a_mantissa, exp), (b_mantissa, _) in zip(a, b)
            ]
        )
        return result

    def __sub__(self, other):
        a, b = Sexagesimal.zero_pad(self, other)
        result = Sexagesimal(
            [
                (a_mantissa - b_mantissa, exp)
                for (a_mantissa, exp), (b_mantissa, _) in zip(a, b)
            ]
        )
        return result

    def __repr__(self):
        return str(self)

    def __str__(self):
        # (mantissa, exponent) representation:
        # return str(self.digits)
        # decimal representation:
        # return str(sum(mantissa * 60**exponent for mantissa, exponent in self.digits))
        string = ','.join([
                str(mantissa)
                for mantissa, exponent in self.digits 
                if exponent >= 0
            ]) + ';' + ','.join([
                str(mantissa)
                for mantissa, exponent in self.digits 
                if exponent < 0
            ]).rstrip(';')
        return string
