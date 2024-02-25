import unittest

import emeszida
p = emeszida.EmeszidaParser
t = emeszida.EmeszidaTransformer()

class TestNumerals(unittest.TestCase):
    def test_numbers(self):
        TEST_CASES = [
            #𒐕 = 60 (NB: how do we deal with unknown placevalues, or do we default to "1"?)
            ("𒋙𒐕", emeszida.Sexagesimal([(1, -1)])),
            ("𒋙𒌋𒐕", emeszida.Sexagesimal([(11, -1)])),
            ("𒋙𒌋𒐕𒌋𒐕", emeszida.Sexagesimal([(11, -1), (11, -2)])),
            ("𒐕", emeszida.Sexagesimal([(1, 0)])),
            ("𒐕𒐕", emeszida.Sexagesimal([(2, 0)])), # (or 𒐖 = 2, *one glyph)
            ("𒐕𒑱𒐕", emeszida.Sexagesimal([(1, 1), (1, 0)])),
            ("𒌋𒐕", emeszida.Sexagesimal([(11, 0)])),
            ("𒐕𒌋", emeszida.Sexagesimal([(1, 1), (10, 0)])),
            ("𒐕𒌋𒐕", emeszida.Sexagesimal([(1, 1), (11, 0)])),
            ("𒐕𒐕𒌋", emeszida.Sexagesimal([(2, 1), (10, 0)])),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(string)
            value = t.transform(tree)
            self.assertEqual(value, expected_value)

    def test_addition(self):
        TEST_CASES = [
            ("𒋙𒐕𒌋𒐕 𒐕𒋙𒐕 +", emeszida.Sexagesimal([(1, 0), (2, -1), (11, -2)])),
            # TODO cases which require carrying
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(string)
            value = t.transform(tree)
            self.assertEqual(value, expected_value)

if __name__ == '__main__':
    unittest.main()
