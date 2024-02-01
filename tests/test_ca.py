from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (1, 'u'),
    (2, 'dos'),
    (3, 'tres'),
    (5.5, 'cinc coma cinc'),
    (11, 'onze'),
    (12, 'dotze'),
    (16, 'setze'),
    (17.42, 'disset coma quatre dos'),
    (19, 'dinou'),
    (20, 'vint'),
    (21, 'vint-i-u'),
    (26, 'vint-i-sis'),
    (27.312, 'vint-i-set coma tres u dos'),
    (28, 'vint-i-vuit'),
    (30, 'trenta'),
    (31, 'trenta-u'),
    (40, 'quaranta'),
    (44, 'quaranta-quatre'),
    (50, 'cinquanta'),
    (53.486, 'cinquanta-tres coma quatre vuit sis'),
    (55, 'cinquanta-cinc'),
    (60, 'seixanta'),
    (67, 'seixanta-set'),
    (70, 'setanta'),
    (79, 'setanta-nou'),
    (89, 'vuitanta-nou'),
    (95, 'noranta-cinc'),
    (100, 'cent'),
    (101, 'cent u'),
    (199, 'cent noranta-nou'),
    (203, 'dos-cents tres'),
    (287, 'dos-cents vuitanta-set'),
    (300.42, 'tres-cents coma quatre dos'),
    (356, 'tres-cents cinquanta-sis'),
    (400, 'quatre-cents'),
    (434, 'quatre-cents trenta-quatre'),
    (578, 'cinc-cents setanta-vuit'),
    (689, 'sis-cents vuitanta-nou'),
    (729, 'set-cents vint-i-nou'),
    (894, 'vuit-cents noranta-quatre'),
    (999, 'nou-cents noranta-nou'),
    (1000, 'mil'),
    (1001, 'mil u'),
    (1097, 'mil noranta-set'),
    (1104, 'mil cent quatre'),
    (1243, 'mil dos-cents quaranta-tres'),
    (2385, 'dos mil tres-cents vuitanta-cinc'),
    (3766, 'tres mil set-cents seixanta-sis'),
    (4196, 'quatre mil cent noranta-sis'),
    (4196.42, 'quatre mil cent noranta-sis coma quatre dos'),
    (5846, 'cinc mil vuit-cents quaranta-sis'),
    (6459, 'sis mil quatre-cents cinquanta-nou'),
    (7232, 'set mil dos-cents trenta-dos'),
    (8569, 'vuit mil cinc-cents seixanta-nou'),
    (9539, 'nou mil cinc-cents trenta-nou'),
    (1000000, 'un milió'),
    (1000001, 'un milió u'),
    (4000000, 'quatre milions'),
    (10000000000000, 'deu bilions'),  # "Billón" en el sistema de numeración de escala larga.
    (100000000000000, 'cent bilions'),
    (1000000000000000000, 'un bilió'),  # "Trillón" en inglés es "bilió" en catalán.
    (1000000000000000000000, 'mil bilions'),
    (10000000000000000000000000, 'deu bilions de bilions')  # "Cuatrillón" no tiene un término directo en catalán.
)

TEST_CASES_ORDINAL = (
    (1, 'primer'),
    (8, 'vuitè'),
    (12, 'dotzè'),
    (14, 'catorzè'),
    (28, 'vint-i-vuitè'),
    (100, 'centè'),
    (12345, 'dotze mil tres-cents quaranta-cinquè'),
)

TEST_CASES_ORDINAL_NUM = (
    (1, '1r'),
    (2, '2n'),
    (3, '3r'),
    (4, '4t'),
    (5, '5è'),
    (8, '8è'),
    (12, '12è'),
    (14, '14è'),
    (28, '28è'),
    (100, '100è'),
    (1000, '1000è'),
    (1000000, '1000000è')
)

TEST_CASES_TO_CURRENCY = (
    (1.00, 'un euro amb zero cèntims'),
    (1.01, 'un euro amb un cèntim'),
    (2.00, 'dos euros amb zero cèntims'),
    (8.00, 'vuit euros amb zero cèntims'),
    (12.00, 'dotze euros amb zero cèntims'),
    (21.00, 'vint-i-un euros amb zero cèntims'),
    (81.25, 'vuitanta-un euros amb vint-i-cinc cèntims'),
    (350.90, 'tres-cents cinquanta euros amb noranta cèntims'),
    (100.00, 'cent euros amb zero cèntims'),
)

TEST_CASES_TO_CURRENCY_ESP = (
    (1.00, 'una pesseta amb zero cèntims'),
    (1.01, 'una pesseta amb un cèntim'),
    (2.00, 'dues pessetes amb zero cèntims'),
    (8.00, 'vuit pessetes amb zero cèntims'),
    (12.00, 'dotze pessetes amb zero cèntims'),
    (21.00, 'vint-i-una pessetes amb zero cèntims'),
    (81.25, 'vuitanta-una pessetes amb vint-i-cinc cèntims'),
    (350.90, 'tres-centes cinquanta pessetes amb noranta cèntims'),
    (100.00, 'cent pessetes amb zero cèntims'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'un dòlar amb zero cèntims'),
    (2.00, 'dos dòlars amb zero cèntims'),
    (8.00, 'vuit dòlars amb zero cèntims'),
    (12.00, 'dotze dòlars amb zero cèntims'),
    (21.00, 'vint-i-un dòlars amb zero cèntims'),
    (81.25, 'vuitanta-un dòlars amb vint-i-cinc cèntims'),
    (350.90, 'tres-cents cinquanta dòlars amb noranta cèntims'),
    (100.00, 'cent dòlars amb zero cèntims'),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, 'una lliura amb zero penics'),
    (1.01, 'una lliura amb un penic'),
    (2.00, 'dues lliures amb zero penics'),
    (8.00, 'vuit lliures amb zero penics'),
    (12.00, 'dotze lliures amb zero penics'),
    (21.00, 'vint-i-una lliures amb zero penics'),
    (81.25, 'vuitanta-una lliures amb vint-i-cinc penics'),
    (350.90, 'tres-centes cinquanta lliures amb noranta penics'),
    (100.00, 'cent lliures amb zero penics'),
    (4150.83, 'quatre mil cent cinquanta lliures amb vuitanta-tres penics'),
)


class Num2WordsESTest(TestCase):

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='ca'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='ca', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='ca', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='ca', to='currency'),
                test[1]
            )

    def test_currency_esp(self):
        for test in TEST_CASES_TO_CURRENCY_ESP:
            self.assertEqual(
                num2words(test[0], lang='ca', to='currency', currency='ESP'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='ca', to='currency', currency='USD'),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang='ca', to='currency', currency='GBP'),
                test[1]
            )
