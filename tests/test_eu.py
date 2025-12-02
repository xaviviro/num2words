from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (1, 'bat'),
    (2, 'bi'),
    (3, 'hiru'),
    (5, 'bost'),
    (10, 'hamar'),
    (11, 'hamaika'),
    (12, 'hamabi'),
    (16, 'hamasei'),
    (19, 'hemeretzi'),
    (20, 'hogei'),
    (21, 'hogeita bat'),
    (26, 'hogeita sei'),
    (28, 'hogeita zortzi'),
    (30, 'hogeita hamar'),
    (31, 'hogeita hamaika'),
    (34, 'hogeita hamalau'),
    (40, 'berrogei'),
    (42, 'berrogeita bi'),
    (44, 'berrogeita lau'),
    (50, 'berrogeita hamar'),
    (55, 'berrogeita hamabost'),
    (60, 'hirurogei'),
    (67, 'hirurogeita zazpi'),
    (70, 'hirurogeita hamar'),
    (79, 'hirurogeita hemeretzi'),
    (80, 'laurogei'),
    (85, 'laurogeita bost'),
    (89, 'laurogeita bederatzi'),
    (95, 'laurogeita hamabost'),
    (99, 'laurogeita hemeretzi'),
    (100, 'ehun'),
    (101, 'ehun bat'),
    (199, 'ehun laurogeita hemeretzi'),
    (200, 'berrehun'),
    (203, 'berrehun hiru'),
    (287, 'berrehun laurogeita zazpi'),
    (300, 'hirurehun'),
    (356, 'hirurehun berrogeita hamasei'),
    (400, 'laurehun'),
    (434, 'laurehun hogeita hamalau'),
    (500, 'bostehun'),
    (578, 'bostehun hirurogeita hemezortzi'),
    (600, 'seiehun'),
    (689, 'seiehun laurogeita bederatzi'),
    (700, 'zazpiehun'),
    (729, 'zazpiehun hogeita bederatzi'),
    (800, 'zortziehun'),
    (894, 'zortziehun laurogeita hamalau'),
    (900, 'bederatziehun'),
    (999, 'bederatziehun laurogeita hemeretzi'),
    (1000, 'mila'),
    (1001, 'mila bat'),
    (1097, 'mila laurogeita hamazazpi'),
    (1104, 'mila ehun lau'),
    (1243, 'mila berrehun berrogeita hiru'),
    (2000, 'bi mila'),
    (2024, 'bi mila hogeita lau'),
    (2385, 'bi mila hirurehun laurogeita bost'),
    (3766, 'hiru mila zazpiehun hirurogeita sei'),
)

TEST_CASES_ORDINAL = (
    (1, 'lehenengo'),
    (2, 'bigarren'),
    (3, 'hirugarren'),
    (4, 'laugarren'),
    (5, 'bosgarren'),
    (8, 'zortzigarren'),
    (10, 'hamargarren'),
    (12, 'hamabigarren'),
    (14, 'hamalaugarren'),
    (28, 'hogeita zortzigarren'),
    (100, 'ehungarren'),
)

TEST_CASES_ORDINAL_NUM = (
    (1, '1.'),
    (2, '2.'),
    (3, '3.'),
    (4, '4.'),
    (5, '5.'),
    (8, '8.'),
    (12, '12.'),
    (14, '14.'),
    (28, '28.'),
    (100, '100.'),
    (1000, '1000.'),
)

TEST_CASES_TO_CURRENCY = (
    (1.00, 'bat euro eta zero zentimo'),
    (2.00, 'bi euro eta zero zentimo'),
    (8.00, 'zortzi euro eta zero zentimo'),
    (12.00, 'hamabi euro eta zero zentimo'),
    (21.00, 'hogeita bat euro eta zero zentimo'),
    (100.00, 'ehun euro eta zero zentimo'),
)


class Num2WordsEUTest(TestCase):

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='eu'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='eu', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='eu', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='eu', to='currency'),
                test[1]
            )
