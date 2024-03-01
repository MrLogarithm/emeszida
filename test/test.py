import unittest

import emeszida

p = emeszida.EmeszidaParser
t = emeszida.EmeszidaTransformer()


class TestNumerals(unittest.TestCase):
    def test_numbers(self):
        TEST_CASES = [
            # 1 through 61:
            ("𒐕", emeszida.Sexagesimal([(1, 0)])),
            ("𒐖", emeszida.Sexagesimal([(2, 0)])),
            ("𒐗", emeszida.Sexagesimal([(3, 0)])),
            ("𒐘", emeszida.Sexagesimal([(4, 0)])),
            ("𒐙", emeszida.Sexagesimal([(5, 0)])),
            ("𒐚", emeszida.Sexagesimal([(6, 0)])),
            ("𒐛", emeszida.Sexagesimal([(7, 0)])),
            ("𒐜", emeszida.Sexagesimal([(8, 0)])),
            ("𒐝", emeszida.Sexagesimal([(9, 0)])),
            ("𒌋", emeszida.Sexagesimal([(10, 0)])),
            ("𒌋𒐕", emeszida.Sexagesimal([(11, 0)])),
            ("𒌋𒐖", emeszida.Sexagesimal([(12, 0)])),
            ("𒌋𒐗", emeszida.Sexagesimal([(13, 0)])),
            ("𒌋𒐘", emeszida.Sexagesimal([(14, 0)])),
            ("𒌋𒐙", emeszida.Sexagesimal([(15, 0)])),
            ("𒌋𒐚", emeszida.Sexagesimal([(16, 0)])),
            ("𒌋𒐛", emeszida.Sexagesimal([(17, 0)])),
            ("𒌋𒐜", emeszida.Sexagesimal([(18, 0)])),
            ("𒌋𒐝", emeszida.Sexagesimal([(19, 0)])),
            ("𒎙", emeszida.Sexagesimal([(20, 0)])),
            ("𒎙𒐕", emeszida.Sexagesimal([(21, 0)])),
            ("𒎙𒐖", emeszida.Sexagesimal([(22, 0)])),
            ("𒎙𒐗", emeszida.Sexagesimal([(23, 0)])),
            ("𒎙𒐘", emeszida.Sexagesimal([(24, 0)])),
            ("𒎙𒐙", emeszida.Sexagesimal([(25, 0)])),
            ("𒎙𒐚", emeszida.Sexagesimal([(26, 0)])),
            ("𒎙𒐛", emeszida.Sexagesimal([(27, 0)])),
            ("𒎙𒐜", emeszida.Sexagesimal([(28, 0)])),
            ("𒎙𒐝", emeszida.Sexagesimal([(29, 0)])),
            ("𒌍", emeszida.Sexagesimal([(30, 0)])),
            ("𒌍𒐕", emeszida.Sexagesimal([(31, 0)])),
            ("𒌍𒐖", emeszida.Sexagesimal([(32, 0)])),
            ("𒌍𒐗", emeszida.Sexagesimal([(33, 0)])),
            ("𒌍𒐘", emeszida.Sexagesimal([(34, 0)])),
            ("𒌍𒐙", emeszida.Sexagesimal([(35, 0)])),
            ("𒌍𒐚", emeszida.Sexagesimal([(36, 0)])),
            ("𒌍𒐛", emeszida.Sexagesimal([(37, 0)])),
            ("𒌍𒐜", emeszida.Sexagesimal([(38, 0)])),
            ("𒌍𒐝", emeszida.Sexagesimal([(39, 0)])),
            ("𒐏", emeszida.Sexagesimal([(40, 0)])),
            ("𒐏𒐕", emeszida.Sexagesimal([(41, 0)])),
            ("𒐏𒐖", emeszida.Sexagesimal([(42, 0)])),
            ("𒐏𒐗", emeszida.Sexagesimal([(43, 0)])),
            ("𒐏𒐘", emeszida.Sexagesimal([(44, 0)])),
            ("𒐏𒐙", emeszida.Sexagesimal([(45, 0)])),
            ("𒐏𒐚", emeszida.Sexagesimal([(46, 0)])),
            ("𒐏𒐛", emeszida.Sexagesimal([(47, 0)])),
            ("𒐏𒐜", emeszida.Sexagesimal([(48, 0)])),
            ("𒐏𒐝", emeszida.Sexagesimal([(49, 0)])),
            ("𒐐", emeszida.Sexagesimal([(50, 0)])),
            ("𒐐𒐕", emeszida.Sexagesimal([(51, 0)])),
            ("𒐐𒐖", emeszida.Sexagesimal([(52, 0)])),
            ("𒐐𒐗", emeszida.Sexagesimal([(53, 0)])),
            ("𒐐𒐘", emeszida.Sexagesimal([(54, 0)])),
            ("𒐐𒐙", emeszida.Sexagesimal([(55, 0)])),
            ("𒐐𒐚", emeszida.Sexagesimal([(56, 0)])),
            ("𒐐𒐛", emeszida.Sexagesimal([(57, 0)])),
            ("𒐐𒐜", emeszida.Sexagesimal([(58, 0)])),
            ("𒐐𒐝", emeszida.Sexagesimal([(59, 0)])),
            ("𒐕𒑱", emeszida.Sexagesimal([(1, 1), (0, 0)])),
            ("𒐕𒐕", emeszida.Sexagesimal([(1, 1), (1, 0)])),
            # Fractions
            ("𒋙𒐕", emeszida.Sexagesimal([(1, -1)])),
            ("𒋙𒌋𒐕", emeszida.Sexagesimal([(11, -1)])),
            ("𒋙𒌍𒐕", emeszida.Sexagesimal([(31, -1)])),
            ("𒋙𒌍𒐕𒐕", emeszida.Sexagesimal([(31, -1), (1, -2)])),
            ("𒋙𒌋𒐕𒐏𒐕", emeszida.Sexagesimal([(11, -1), (41, -2)])),
            ("𒋙𒌋𒐕𒌍𒐕𒌋", emeszida.Sexagesimal([(11, -1), (31, -2), (10, -3)])),
            ("𒌋𒋙𒐕", emeszida.Sexagesimal([(10, 0), (1, -1)])),
            ("𒐕𒋙𒌍𒐕", emeszida.Sexagesimal([(1, 0), (31, -1)])),
            (
                "𒐕𒌍𒋙𒌍𒐕𒐕",
                emeszida.Sexagesimal([(1, 1), (30, 0), (31, -1), (1, -2)]),
            ),
            (
                "𒐕𒐕𒋙𒌋𒐕𒐏𒐕",
                emeszida.Sexagesimal([(1, 1), (1, 0), (11, -1), (41, -2)]),
            ),
            (
                "𒐕𒐏𒋙𒌋𒐕𒌍𒐕𒌋",
                emeszida.Sexagesimal(
                    [(1, 1), (40, 0), (11, -1), (31, -2), (10, -3)]
                ),
            ),
            # Zero
            ("𒐕𒑱𒐕", emeszida.Sexagesimal([(1, 2), (0, 1), (1, 0)])),
            ("𒐕𒑱", emeszida.Sexagesimal([(1, 1), (0, 0)])),
            # Misc
            ("𒌋𒐕𒌍𒐕𒌋", emeszida.Sexagesimal([(11, 2), (31, 1), (10, 0)])),
            ("𒐕𒌋", emeszida.Sexagesimal([(1, 1), (10, 0)])),
            ("𒐕𒌋𒐕", emeszida.Sexagesimal([(1, 1), (11, 0)])),
            ("𒐕𒐕𒌋", emeszida.Sexagesimal([(1, 2), (1, 1), (10, 0)])),
            ("𒐖𒌋", emeszida.Sexagesimal([(2, 1), (10, 0)])),
            ("𒌋𒑱𒌋𒐕", emeszida.Sexagesimal([(10, 2), (0, 1), (11, 0)])),
            # Spaces
            ("𒌋𒐕", emeszida.Sexagesimal([(11, 0)])),
            ("𒌋 𒐕", emeszida.Sexagesimal([(10, 1), (1, 0)])),
            ("𒌋𒌋𒐕", emeszida.Sexagesimal([(10, 1), (11, 0)])),
            ("𒌋 𒌋𒐕", emeszida.Sexagesimal([(10, 1), (11, 0)])),
            ("𒌋 𒌋 𒐕", emeszida.Sexagesimal([(10, 2), (10, 1), (1, 0)])),
            ("𒌋𒌋 𒐕",  emeszida.Sexagesimal([(10, 2), (10, 1), (1, 0)])),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(string)
            value = t.transform(tree)
            self.assertEqual(value, expected_value)

    def test_addition(self):
        TEST_CASES = [
            ("𒋙𒐕𒌋𒐕 𒀀𒈾 𒐕𒋙𒐕 𒈭𒄩", emeszida.Sexagesimal([(1, 0), (2, -1), (11, -2)])),
            ## Carrying
            ("𒌍𒑱 𒀀𒈾 𒌍𒑱 𒈭𒄩", emeszida.Sexagesimal([(1, 2), (0, 1), (0, 0)])),
            ("𒐐 𒀀𒈾 𒌋 𒈭𒄩", emeszida.Sexagesimal([(1, 1), (0, 0)])),
            ("𒐐𒐝 𒀀𒈾 𒐕 𒈭𒄩", emeszida.Sexagesimal([(1, 1), (0, 0)])),
            ("𒐐𒐝 𒀀𒈾 𒌋𒐕 𒈭𒄩", emeszida.Sexagesimal([(1, 1), (10, 0)])),
            ("𒐐𒐝𒑱 𒀀𒈾 𒐐𒐝 𒀀𒈾 𒐕 𒈭𒄩  𒈭𒄩", emeszida.Sexagesimal([(1, 2), (0, 1), (0, 0)])),
            ("𒐐𒐝𒑱 𒀀𒈾 𒐐𒐝 𒈭𒄩  𒀀𒈾 𒐕 𒈭𒄩", emeszida.Sexagesimal([(1, 2), (0, 1), (0, 0)])),
            ("𒌋𒐙 𒀀𒈾 𒐕 𒈭𒄩", emeszida.Sexagesimal([(16, 0)])),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(string)
            value = t.transform(tree)
            self.assertEqual(value, expected_value)

    def test_subtraction(self):
        TEST_CASES = [
            ("𒐕𒐏 𒄿𒈾 𒎙𒐜𒎙 𒁀𒍣", emeszida.Sexagesimal([(26, 1), (40, 0)])),
            ("𒋙𒐕𒌋𒐕 𒄿𒈾 𒐕𒋙𒐕 𒁀𒍣", emeszida.Sexagesimal([(0, 0), (59, -1), (49, -2)])),
            ("𒌍𒑱 𒄿𒈾 𒌍𒑱 𒁀𒍣", emeszida.Sexagesimal([(0, 0)])),
            ("𒌋 𒄿𒈾 𒐐 𒁀𒍣", emeszida.Sexagesimal([(40, 0)])),
            ("𒐐𒑱 𒀀𒈾 𒐕 𒈭𒄩  𒄿𒈾 𒐐𒐕𒑱 𒁀𒍣", emeszida.Sexagesimal([(59, 0)])),
            ("𒐐 𒐕 𒄿𒈾 𒐐𒐕𒑱 𒁀𒍣", emeszida.Sexagesimal([(59, 0)])),
            (
                "𒋙𒑱𒑱𒑱𒑱𒐕 𒄿𒈾 𒐕 𒁀𒍣",
                emeszida.Sexagesimal(
                    [(0, 0), (59, -1), (59, -2), (59, -3), (59, -4), (59, -5)]
                    ),
            ),
            ("𒐕 𒄿𒈾 𒐐𒐝 𒁀𒍣  𒄿𒈾 𒐐𒐝𒑱 𒁀𒍣", emeszida.Sexagesimal([(58, 1), (2, 0)])),
            ("𒐐 𒀀𒈾 𒐝 𒈭𒄩  𒄿𒈾 𒐐𒐝 𒁀𒍣", emeszida.Sexagesimal([(0, 0)])),
            # Negatives?
            # ("𒐕 𒌋𒐕 𒁀𒍣", emeszida.Sexagesimal([(-10, 0)])),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(string)
            value = t.transform(tree)
            self.assertEqual(value, expected_value)


if __name__ == "__main__":
    unittest.main()
