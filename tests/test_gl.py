from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (1, 'un'),
    (2, 'dous'),
    (3, 'tres'),
    (5, 'cinco'),
    (10, 'dez'),
    (11, 'once'),
    (12, 'doce'),
    (16, 'dezaseis'),
    (19, 'dezanove'),
    (20, 'vinte'),
    (21, 'vinte e un'),
    (26, 'vinte e seis'),
    (28, 'vinte e oito'),
    (30, 'trinta'),
    (31, 'trinta e un'),
    (40, 'corenta'),
    (42, 'corenta e dous'),
    (44, 'corenta e catro'),
    (50, 'cincuenta'),
    (55, 'cincuenta e cinco'),
    (60, 'sesenta'),
    (67, 'sesenta e sete'),
    (70, 'setenta'),
    (79, 'setenta e nove'),
    (80, 'oitenta'),
    (89, 'oitenta e nove'),
    (95, 'noventa e cinco'),
    (99, 'noventa e nove'),
    (100, 'cen'),
    (101, 'cento un'),
    (199, 'cento noventa e nove'),
    (200, 'douscentos'),
    (203, 'douscentos tres'),
    (287, 'douscentos oitenta e sete'),
    (300, 'trescentos'),
    (356, 'trescentos cincuenta e seis'),
    (400, 'catrocentos'),
    (434, 'catrocentos trinta e catro'),
    (500, 'cincocentos'),
    (578, 'cincocentos setenta e oito'),
    (600, 'seiscentos'),
    (689, 'seiscentos oitenta e nove'),
    (700, 'setecentos'),
    (729, 'setecentos vinte e nove'),
    (800, 'oitocentos'),
    (894, 'oitocentos noventa e catro'),
    (900, 'novecentos'),
    (999, 'novecentos noventa e nove'),
    (1000, 'mil'),
    (1001, 'mil un'),
    (1097, 'mil noventa e sete'),
    (1104, 'mil cento catro'),
    (1243, 'mil douscentos corenta e tres'),
    (2000, 'dous mil'),
    (2024, 'dous mil vinte e catro'),
    (2385, 'dous mil trescentos oitenta e cinco'),
    (3766, 'tres mil setecentos sesenta e seis'),
)

TEST_CASES_ORDINAL = (
    (1, 'primeiro'),
    (2, 'segundo'),
    (3, 'terceiro'),
    (4, 'cuarto'),
    (5, 'quinto'),
    (8, 'oitavo'),
    (10, 'décimo'),
)

TEST_CASES_ORDINAL_NUM = (
    (1, '1º'),
    (2, '2º'),
    (3, '3º'),
    (4, '4º'),
    (5, '5º'),
    (8, '8º'),
    (12, '12º'),
    (14, '14º'),
    (28, '28º'),
    (100, '100º'),
    (1000, '1000º'),
)

TEST_CASES_TO_CURRENCY = (
    (1.00, 'un euro con cero céntimos'),
    (2.00, 'dous euros con cero céntimos'),
    (8.00, 'oito euros con cero céntimos'),
    (12.00, 'doce euros con cero céntimos'),
    (21.00, 'vinte e un euros con cero céntimos'),
    (100.00, 'cen euros con cero céntimos'),
)


class Num2WordsGLTest(TestCase):

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='gl'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='gl', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='gl', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='gl', to='currency'),
                test[1]
            )
