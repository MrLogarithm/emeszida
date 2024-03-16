import unittest

import emeszida
from emeszida import Sexagesimal

p = emeszida.EmeszidaParser
t = emeszida.EmeszidaTransformer()

TEMPLATE = """𒁾
{}
---
colophon"""

class TestNumerals(unittest.TestCase):
    """
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
    """
    def test_negatives(self):
        TEST_CASES = [
            (
                # +ve - +ve
                # 4 - 1 = -3
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal([(-3,0)]),
                }
            ),
            (
                # Alternate constructor for Sexagesimal
                # 4 - 1 = -3
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal([(3,0)], sign=-1),
                }
            ),
            (
                # Alternative constructor for Sexagesimal
                # 12 - 2,13 = -2,1
                "𒐖𒌋𒐗𒄿𒈾𒌋𒐖		𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((2,0),): Sexagesimal("-2,1"),
                }
            ),
            (
                # -ve * +ve
                # 4 - 1  = -3
                # -3 * 5 = -15
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰  𒐙		𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-15"),
                }
            ),
            (
                # Reciprocal of -ve
                # 4 - 1 = -3
                # -3 * 5 = -15
                # 1 / -15 = -0;4
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰  𒐙		𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰	𒅆	𒃻𒋃𒐕𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-0;4"),
                }
            ),
            (
                # +ve - +ve, multiple digits
                # 1,12 - 2,13 = -1,1
                "𒐖𒌋𒐗𒄿𒈾𒐕𒌋𒐖		𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((2,0),): Sexagesimal("-1,1"),
                }
            ),
            (
                # +ve - +ve, different number of digits 
                # 12 - 2,13 = -2,1
                "𒐖𒌋𒐗𒄿𒈾𒌋𒐖		𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((2,0),): Sexagesimal("-2,1"),
                }
            ),
            (
                # +ve - +ve, fraction
                # 10;5 - 21;13,4 = -11;8,4
                "𒎙𒐕𒋙𒌋𒐗𒐘𒄿𒈾𒌋𒋙𒐙		𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((2,0),): Sexagesimal("-11;8,4"),
                }
            ),
            (
                # +ve - +ve, fraction with carry
                # 10;13,4 - 21;5 = -10;51,56
                "𒎙𒐕𒋙𒐙𒄿𒈾𒌋𒋙𒌋𒐗𒐘		𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((2,0),): Sexagesimal("-10;51,56"),
                }
            ),
            (
                # +ve - -ve
                # 0 - 5 = -5
                # 4 - -5 = 9
                "𒐙𒄿𒈾𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰𒄿𒈾𒐘	𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-5"),
                    ((2,0),): Sexagesimal("9"),
                }
            ),
            (
                # -ve - -ve
                # 0 - 5 = -5
                # 4 - 10 = -6
                # -5 - -6 = 1
                "𒐙𒄿𒈾𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒌋𒄿𒈾𒐘	𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕\n𒃻𒋃𒐖𒄰𒄿𒈾𒃻𒋃𒐕𒄰	𒁀𒍣	𒃻𒋃𒐗𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-5"),
                    ((2,0),): Sexagesimal("-6"),
                    ((3,0),): Sexagesimal("1"),
                }
            ),
            (
                # -ve + -ve
                # 0 - 5 = -5
                # 4 - 10 = -6
                # -5 + -6 = -11
                "𒐙𒄿𒈾𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒌋𒄿𒈾𒐘	𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕\n𒃻𒋃𒐖𒄰𒀀𒈾𒃻𒋃𒐕𒄰	𒈭𒄩	𒃻𒋃𒐗𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-5"),
                    ((2,0),): Sexagesimal("-6"),
                    ((3,0),): Sexagesimal("-11"),
                }
            ),
            (
                # +ve + -ve
                # 4 - 1 = -3
                # 10 + -3 = 7
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰𒀀𒈾𒌋	𒈭𒄩	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-3"),
                    ((2,0),): Sexagesimal("7"),
                }
            ),
            (
                # -ve + +ve
                # 4 - 1 = -3
                # -3 + 10 = 7
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒌋𒀀𒈾𒃻𒋃𒐕𒄰	𒈭𒄩	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-3"),
                    ((2,0),): Sexagesimal("7"),
                }
            ),
            (
                # -ve * +ve
                # 4 - 1 = -3
                # -3 * 10 = -30
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰  𒌋	𒀀𒁺	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-3"),
                    ((2,0),): Sexagesimal("-30"),
                }
            ),
            (
                # +ve * -ve
                # 4 - 1 = -3
                # 1,4 * -3 = -3,12
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒐕 𒐘  𒃻𒋃𒐕𒄰	𒀀𒁺	𒃻𒋃𒐖𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-3"),
                    ((2,0),): Sexagesimal("-3,12"),
                }
            ),
            (
                # -ve * +ve
                # 4 - 1 = -3
                # 0 - 25 = -25
                # -3 * -25 = 1,15
                "𒐘𒄿𒈾𒐕		𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒎙𒐙𒄿𒈾𒑱	𒁀𒍣	𒃻𒋃𒐖𒄰	𒐕\n𒃻𒋃𒐕𒄰  𒃻𒋃𒐖𒄰	𒀀𒁺	𒃻𒋃𒐘𒄰	𒐕", 
                {
                    ((1,0),): Sexagesimal("-3"),
                    ((2,0),): Sexagesimal("-25"),
                    ((4,0),): Sexagesimal("1,15"),
                }
            ),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(TEMPLATE.format(string))
            program = t.transform(tree)
            program.execute()
            for register, value in expected_value.items():
                self.assertEqual(program.registers[register], value)

    def test_gt(self):
        TEST_CASES = [
            (emeszida.Sexagesimal([(2, 0)]) > emeszida.Sexagesimal([(1,0)]), True),
            (emeszida.Sexagesimal([(2, 0)]) < emeszida.Sexagesimal([(1,0)]), False),
            (emeszida.Sexagesimal([(1, 1)]) > emeszida.Sexagesimal([(2,0)]), True),
            (emeszida.Sexagesimal([(1, 1)]) < emeszida.Sexagesimal([(2,0)]), False),
            (emeszida.Sexagesimal([(1, 1), (0, 0)]) > emeszida.Sexagesimal([(59, 0)]), True),
            (emeszida.Sexagesimal([(1, 1), (0, 0)]) < emeszida.Sexagesimal([(59, 0)]), False),
            (emeszida.Sexagesimal([(1, 1), (0, 0)]) > emeszida.Sexagesimal([(60, 0)]), False),
            (emeszida.Sexagesimal([(1, 1), (0, 0)]) < emeszida.Sexagesimal([(60, 0)]), False),
            (emeszida.Sexagesimal([(1, 1), (5, 0)]) > emeszida.Sexagesimal([(1 ,1), (2, 0)]), True),
            (emeszida.Sexagesimal([(1, 1), (5, 0)]) < emeszida.Sexagesimal([(1 ,1), (2, 0)]), False),
            (emeszida.Sexagesimal([(0, 0), (1, -1)]) > emeszida.Sexagesimal([(0, 0), (0, -1), (1, -2)]), True),
            (emeszida.Sexagesimal([(0, 0), (1, -1)]) < emeszida.Sexagesimal([(0, 0), (0, -1), (1, -2)]), False),
            (emeszida.Sexagesimal([(0, 0), (1, -1)]) > emeszida.Sexagesimal([(0, 0), (2, -1), (1, -2)]), False),
            (emeszida.Sexagesimal([(0, 0), (1, -1)]) < emeszida.Sexagesimal([(0, 0), (2, -1), (1, -2)]), True),
            (emeszida.Sexagesimal("-2") < emeszida.Sexagesimal("1"), True),
            (emeszida.Sexagesimal("-2") < emeszida.Sexagesimal("2"), True),
            (emeszida.Sexagesimal("-2") < emeszida.Sexagesimal("3"), True),
            (emeszida.Sexagesimal("-2") > emeszida.Sexagesimal("1"), False),
            (emeszida.Sexagesimal("-2") > emeszida.Sexagesimal("2"), False),
            (emeszida.Sexagesimal("-2") > emeszida.Sexagesimal("3"), False),
            (emeszida.Sexagesimal("-2") < emeszida.Sexagesimal("-1"), True),
            (emeszida.Sexagesimal("-2") < emeszida.Sexagesimal("-10"), False),
            (emeszida.Sexagesimal("-2") < emeszida.Sexagesimal("-2"), False),
            (emeszida.Sexagesimal("-2") > emeszida.Sexagesimal("-2"), False),
            (emeszida.Sexagesimal("2") < emeszida.Sexagesimal("2"), False),
            (emeszida.Sexagesimal("2") > emeszida.Sexagesimal("2"), False),
            (emeszida.Sexagesimal("-2") < emeszida.Sexagesimal("1;5"), True),
            (emeszida.Sexagesimal("-2;5") < emeszida.Sexagesimal("1;5"), True),
            (emeszida.Sexagesimal("-2;5") < emeszida.Sexagesimal("-2"), True),
        ]

        for value, expected_value in TEST_CASES:
            self.assertEqual(value, expected_value)

    def test_addition(self):
        TEST_CASES = [
            ("𒋙𒐕𒌋𒐕𒀀𒈾𒐕𒋙𒐕	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(1, 0), (2, -1), (11, -2)])}),
            ## Carrying
            ("𒌍𒑱𒀀𒈾𒌍𒑱	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(1, 2), (0, 1), (0, 0)])}),
            ("𒐐𒀀𒈾𒌋	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal([(1, 1), (0, 0)])}),
            ("𒐐𒐝𒀀𒈾𒐕	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal([(1, 1), (0, 0)])}),
            ("𒐐𒐝𒀀𒈾𒌋𒐕	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(1, 1), (10, 0)])}),
            ("𒌋𒐙𒀀𒈾𒐕	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal([(16, 0)])}),
            ("𒐐𒐝𒑱𒀀𒈾𒐐𒐝	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰𒀀𒈾𒐕	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(1, 2), (0, 1), (0, 0)])}),
            ("𒐐𒐝𒑱𒀀𒈾𒐐𒐝	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕\n𒐕𒀀𒈾𒃻𒋃𒐕𒄰	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(1, 2), (0, 1), (0, 0)])}),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(TEMPLATE.format(string))
            program = t.transform(tree)
            program.execute()
            for register, value in expected_value.items():
                self.assertEqual(program.registers[register], value)

    def test_multiplication(self):
        TEST_CASES = [
            ("𒐕𒐏  𒎙𒐜𒎙	𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(47, 2), (13, 1), (20, 0)])}),
            ("𒐕  𒎙𒐜𒎙	𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(28, 1), (20, 0)])}),
            ("𒎙  𒐗	𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal([(1, 1), (0, 0)])}),
            ("𒌋𒐘𒌍  𒌋𒐘𒌍	𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(3, 3), (30, 2), (15, 1), (0, 0)])}),
            ("𒐕  𒋙𒑱𒑱𒌋	𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(0, 0), (0, -1), (0, -2), (10, -3)])}),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(TEMPLATE.format(string))
            program = t.transform(tree)
            program.execute()
            for register, value in expected_value.items():
                self.assertEqual(program.registers[register], value)

    def test_subtraction(self):
        TEST_CASES = [
            ("𒐕𒐏𒄿𒈾𒎙𒐜𒎙	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(26, 1), (40, 0)])}),
            ("𒋙𒐕𒌋𒐕𒄿𒈾𒐕𒋙𒐕	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(0, 0), (59, -1), (49, -2)])}),
            ("𒌍𒑱𒄿𒈾𒌍𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(0, 0)])}),
            ("𒌋𒄿𒈾𒐐	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal([(40, 0)])}),
            ("𒐐 𒐕𒄿𒈾𒐐𒐕𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(59, 0)])}),
            ("𒋙𒑱𒑱𒑱𒑱𒐕𒄿𒈾𒐕	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal("0;59,59,59,59,59")}),
            ("𒐐𒑱𒀀𒈾𒐕	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰𒄿𒈾𒐐𒐕𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", 
                {((1,0),): Sexagesimal([(59, 0)])}),
            ("𒐕𒄿𒈾𒐐𒐝	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰𒄿𒈾𒐐𒐝𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", 
                {((1,0),): Sexagesimal([(58, 1), (2, 0)])}),
            ("𒐐𒀀𒈾𒐝	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰𒄿𒈾𒐐𒐝	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", 
                {((1,0),): Sexagesimal([(0, 0)])}),
            # Negatives
            ("𒌋𒐕  𒐕	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal("-10")}),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(TEMPLATE.format(string))
            program = t.transform(tree)
            program.execute()
            for register, value in expected_value.items():
                self.assertEqual(program.registers[register], value)

    def test_reciprocal(self):
        TEST_CASES = [
            ("𒐕	𒅆	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal([(1, 0)])}),
            ("𒐛𒌍	𒅆	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(0, 0), (0, -1), (8, -2)])}),
            ("𒌋𒐙	𒅆	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(0, 0), (4, -1)])}),
            ("𒌋𒐙𒑱	𒅆	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(0, 0), (0, -1), (4, -2)])}),
            ("𒌋	𒅆	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal([(0, 0), (6, -1)])}),
            ("𒋙𒌋	𒅆	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(6, 0)])}),
            ("𒋙𒑱𒑱𒌋	𒅆	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(6, 2), (0, 1), (0, 0)])}),
            ("𒐛𒋙𒌍	𒅆	𒃻𒋃𒐕𒄰	𒐕", {((1,0),): Sexagesimal([(0, 0), (8, -1)])}),
            ("𒐖	𒅆	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰  𒌋	𒀀𒁺	𒃻𒋃𒐕𒄰	𒐕",  
                {((1,0),): Sexagesimal([(5, 0)])}),
            # Non-Terminating
            ("𒐛	𒅆	𒃻𒋃𒐕𒄰	𒐕",     {((1,0),): Sexagesimal("0;8,0,34,0,17,0,8,0,34")}),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(TEMPLATE.format(string))
            program = t.transform(tree)
            program.execute()
            for register, value in expected_value.items():
                self.assertEqual(program.registers[register], value)

    def test_sequence(self):
        TEST_CASES = [
            # "3000 to 1 add, from 3060 subtract = 59"
            ("𒐐𒑱𒀀𒈾𒐕	𒈭𒄩	𒃻𒋃𒐕𒄰	𒐕\n𒃻𒋃𒐕𒄰𒄿𒈾𒐐𒐕𒑱	𒁀𒍣	𒃻𒋃𒐕𒄰	𒐕", 
                {((1,0),): Sexagesimal([(59,0)])}),
        ]

        for string, expected_value in TEST_CASES:
            tree = p.parse(TEMPLATE.format(string))
            program = t.transform(tree)
            program.execute()
            for register, value in expected_value.items():
                self.assertEqual(program.registers[register], value)

if __name__ == "__main__":
    unittest.main()
