class Sexagesimal(object):
    def __init__(self, digits, sign=None):
        """
        digits should be a list of (mantissa, exponent) tuples, e.g.
        [(2, 1), (0, 0), (3, -1)], representing
        2x60^1 + 0x60^0 + 3*60^-1 = 120.05 = 𒐖𒑱𒋙𒐗
        """
        if isinstance(digits, list):
            self.digits, self.sign = Sexagesimal.normalize(digits)
        else:
            if digits[0] == "-":
                self.sign = -1
                digits = digits[1:]
            else:
                self.sign = 1
            if ";" in digits:
                integer, fraction = digits.split(";")
                integer = integer.split(",")
                fraction = fraction.split(",")
            else:
                integer = digits.split(",")
                fraction = []
            self.digits = []
            for exponent, digit in enumerate(integer[::-1]):
                self.digits = [(int(digit), exponent)] + self.digits
            for exponent, digit in enumerate(fraction):
                self.digits = self.digits + [(int(digit), -exponent-1)]
        if sign:
            self.sign = sign

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
        while digits[0][1] < 0:
            digits = [(0, digits[0][1] + 1)] + digits
        while digits[-1][1] > 0:
            digits = digits + [(0, digits[-1][1] - 1)]

        carry = 0
        for idx in range(len(digits) - 1, -1, -1):
            mantissa, exponent = digits[idx]
            if carry:
                mantissa += carry
                carry = 0
            while mantissa >= 60:
                mantissa -= 60
                carry += 1
            while mantissa < 0 and idx != 0:
                mantissa += 60
                carry -= 1
            digits[idx] = (mantissa, exponent)

        if carry:
            digits = [(carry, exponent + 1)] + digits

        # trim empty positions
        while digits[0][0] == 0 and digits[0][1] > 0:
            digits = digits[1:]
        while digits[-1][0] == 0 and digits[-1][1] < 0:
            digits = digits[:-1]

        sign = -1 if digits[0][0] < 0 else 1
        if sign == -1:
            digits[0] = (-digits[0][0], digits[0][1])

        #raise Exception("Negative numbers have not been invented yet.")

        return digits, sign

    def __gt__(self, other, idx=0):
        if self.sign == 1 and other.sign == -1:
            return True
        elif self.sign == -1 and other.sign == 1:
            return False
        elif self.sign == -1 and other.sign == -1:
            return Sexagesimal(self.digits, sign=1) < Sexagesimal(other.digits, sign=1)


        m1, e1 = self.digits[idx]
        m2, e2 = other.digits[idx]
        if e1 > e2 or (m1 > m2 and e1 == e2):
            return True
        elif e1 == e2 and m1 == m2:
            if idx + 1 < len(self.digits) and idx + 1 < len(other.digits):
                return self.__gt__(other, idx=idx + 1)
            elif idx + 1 < len(self.digits):
                return True
            else:
                # Equal
                return False
        return False

    def reciprocal(self):
        result = []
        exponent = 0

        N = Sexagesimal(self.digits)

        dividend = Sexagesimal([(1, 0)])
        while dividend != Sexagesimal([(0, 0)]):
            if N > dividend:
                dividend = dividend * Sexagesimal([(1, 1)])
                result.append((0, exponent))
                exponent -= 1
            else:
                quotient = Sexagesimal([(1, 0)])
                while dividend > quotient * N:
                    quotient += Sexagesimal([(1, 0)])
                if quotient * N > dividend:
                    quotient -= Sexagesimal([(1, 0)])
                remainder = dividend - (quotient * N)
                for m, e in quotient.digits:
                    result.append((m, exponent+e))
                exponent -= 1
                dividend = remainder
                # TODO if we have already seen this remainder, break and autofill repeated digits
            if exponent < -10:
                break
        return Sexagesimal(result, sign=self.sign)

    def __eq__(self, other):
        return self.digits == other.digits and self.sign == other.sign

    def __add__(self, other):
        if self.sign == 1 and other.sign == -1:
            return self - Sexagesimal(other.digits, sign=1)
        if self.sign == -1 and other.sign == 1:
            return other - Sexagesimal(self.digits, sign=1)
        a, b = Sexagesimal.zero_pad(self, other)
        result = Sexagesimal(
            [
                (a_mantissa + b_mantissa, exp)
                for (a_mantissa, exp), (b_mantissa, _) in zip(a, b)
            ]
        )
        if self.sign == -1 and other.sign == -1:
            result.sign = -1
        return result

    def __sub__(self, other):
        if other.sign == -1:
            return self + Sexagesimal(other.digits, sign=1)
        if other > self:
            return Sexagesimal((other - self).digits, -1)

        a, b = Sexagesimal.zero_pad(self, other)
        result = Sexagesimal(
            [
                (a_mantissa - b_mantissa, exp)
                for (a_mantissa, exp), (b_mantissa, _) in zip(a, b)
            ]
        )
        return result

    def __mul__(self, other):
        terms = []
        for mantissa, exponent in other.digits:
            term = []
            for m, e in self.digits:
                term += [(m*mantissa, exponent+e)]
            for idx in range(exponent):
                term += [(0, idx)]
            terms.append(Sexagesimal(term))
        result = sum(terms, Sexagesimal([(0, 0)]))
        return Sexagesimal(result.digits, self.sign * other.sign)

    def __repr__(self):
        return str(self)

    def __str__(self):
        # (mantissa, exponent) representation:
        # return str(self.digits)
        # decimal representation:
        # return str(sum(mantissa * 60**exponent for mantissa, exponent in self.digits))
        string = (
                ','.join([
                    str(mantissa)
                    for mantissa, exponent in self.digits 
                    if exponent >= 0
                ]) + ';' + ','.join([
                    str(mantissa)
                    for mantissa, exponent in self.digits 
                    if exponent < 0
                ])
            ).rstrip(';')
        if self.sign == -1:
            string = f"-{string}"
        return string
