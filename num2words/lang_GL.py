# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, print_function, unicode_literals

import math

from .lang_EU import Num2Word_EU

GENERIC_DOLLARS = ('dólar', 'dólares')
GENERIC_CENTS = ('céntimo', 'céntimos')
CURRENCIES_UNA = ('SLL', 'SEK', 'NOK', 'CZK', 'DKK', 'ISK',
                  'SKK', 'GBP', 'CYP', 'EGP', 'FKP', 'GIP',
                  'LBP', 'SDG', 'SHP', 'SSP', 'SYP', 'INR',
                  'IDR', 'LKR', 'MUR', 'NPR', 'PKR', 'SCR',
                  'ESP', 'TRY', 'ITL')
CENTS_UNA = ('EGP', 'JOD', 'LBP', 'SDG', 'SSP', 'SYP')


class Num2Word_GL(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euros'), ('céntimo', 'céntimos')),
        'ESP': (('peseta', 'pesetas'), ('céntimo', 'céntimos')),
        'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'GBP': (('libra', 'libras'), ('penique', 'peniques')),
        'BRL': (('real', 'reais'), GENERIC_CENTS),
    }

    GIGA_SUFFIX = None
    MEGA_SUFFIX = "illón"

    def setup(self):
        lows = ["catro", "tres", "dous", "un"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menos "
        self.pointword = "coma"
        self.errmsg_nonnum = "type(%s) non é [long, int, float]"
        self.errmsg_floatord = "O float %s non pode ser tratado como ordinal."
        self.errmsg_negord = "O número negativo %s non pode ser tratado como ordinal."
        self.errmsg_toobig = (
            "abs(%s) debe ser inferior a %s."
        )
        self.gender_stem = "o"
        self.exclude_title = ["e", "menos", "coma"]
        self.mid_numwords = [
            (1000, "mil"),
            (100, "cen"),
            (90, "noventa"),
            (80, "oitenta"),
            (70, "setenta"),
            (60, "sesenta"),
            (50, "cincuenta"),
            (40, "corenta"),
            (30, "trinta")
        ]
        self.low_numwords = [
            "vinte e nove", "vinte e oito", "vinte e sete",
            "vinte e seis", "vinte e cinco", "vinte e catro",
            "vinte e tres", "vinte e dous", "vinte e un",
            "vinte", "dezanove", "dezaoito", "dezasete",
            "dezaseis", "quince", "catorce", "trece", "doce",
            "once", "dez", "nove", "oito", "sete", "seis",
            "cinco", "catro", "tres", "dous", "un", "cero"
        ]
        self.ords = {
            1: "primeir",
            2: "segund",
            3: "terceir",
            4: "cuart",
            5: "quint",
            6: "sext",
            7: "sétim",
            8: "oitav",
            9: "noven",
            10: "décim",
        }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "un"
        elif cnum == 100 and not nnum % 1000 == 0:
            ctext += "t" + self.gender_stem

        if nnum < cnum:
            if cnum < 100:
                return "%s e %s" % (ctext, ntext), cnum + nnum
            return "%s %s" % (ctext, ntext), cnum + nnum
        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-3] + "lóns"

        if nnum == 100:
            if cnum == 2:
                ctext = "dous"
                ntext = "centos"
            elif cnum == 3:
                ctext = "tres"
                ntext = "centos"
            elif cnum == 4:
                ctext = "catro"
                ntext = "centos"
            elif cnum == 5:
                ctext = "cincocentos"
                ntext = ""
            elif cnum == 6:
                ctext = "seiscentos"
                ntext = ""
            elif cnum == 7:
                ctext = "setecentos"
                ntext = ""
            elif cnum == 8:
                ctext = "oitocentos"
                ntext = ""
            elif cnum == 9:
                ctext = "novecentos"
                ntext = ""
            if ntext:
                ntext = ntext
            else:
                return (ctext, cnum * nnum)
        else:
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 0:
            text = ""
        elif value <= 10:
            text = "%s%s" % (self.ords[value], self.gender_stem)
        elif value <= 12:
            text = (
                "%s%s%s" % (self.ords[10], self.gender_stem,
                            self.to_ordinal(value - 10))
            )
        elif value <= 100:
            dec = (value // 10) * 10
            text = (
                "%s%s %s" % (self.ords[dec], self.gender_stem,
                             self.to_ordinal(value - dec))
            )
        else:
            text = self.to_cardinal(value) + "º"
        return text.strip()

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, "º" if self.gender_stem == 'o' else "ª")

    def to_currency(self, val, currency='EUR', cents=True, separator=' con',
                    adjective=False):
        result = super(Num2Word_GL, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)

        # En gallego, se usa "un" en lugar de "uno"
        list_result = result.split(separator + " ")

        # Para monedas femeninas
        if currency in CURRENCIES_UNA:
            list_result[0] = list_result[0].replace("un ", "unha ")
            list_result[0] = list_result[0].replace("dous", "dúas")
            list_result[0] = list_result[0].replace("centos", "centas")

        # Para céntimos femeninos
        if currency in CENTS_UNA:
            list_result[1] = list_result[1].replace("un ", "unha ")

        result = (separator + " ").join(list_result)

        return result
