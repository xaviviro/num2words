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

GENERIC_DOLLARS = ('dolar', 'dolar')
GENERIC_CENTS = ('zentimo', 'zentimo')


class Num2Word_EUS(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euro'), ('zentimo', 'zentimo')),
        'USD': (('dolar', 'dolar'), ('zentimo', 'zentimo')),
        'GBP': (('libera', 'libera'), ('penique', 'penique')),
    }

    GIGA_SUFFIX = None
    MEGA_SUFFIX = "ilioi"

    def setup(self):
        lows = ["laur", "hiru", "bi", "bat"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "ken "
        self.pointword = "koma "
        self.errmsg_nonnum = "type(%s) ez da [long, int, float]"
        self.errmsg_floatord = "%s float zenbakia ezin da ordenala izan."
        self.errmsg_negord = "%s zenbaki negatiboa ezin da ordenala izan."
        self.errmsg_toobig = (
            "abs(%s) %s baino txikiagoa izan behar da."
        )
        self.gender = "m"
        self.exclude_title = ["eta", "ken", "koma"]
        self.mid_numwords = [
            (1000, "mila"),
            (100, "ehun"),
            (80, "laurogei"),
            (60, "hirurogei"),
            (40, "berrogei"),
            (20, "hogei")
        ]
        self.low_numwords = [
            "hogeita bederatzi", "hogeita zortzi", "hogeita zazpi",
            "hogeita sei", "hogeita bost", "hogeita lau",
            "hogeita hiru", "hogeita bi", "hogeita bat",
            "hogei", "hemeretzi", "hemezortzi", "hamazazpi",
            "hamasei", "hamabost", "hamalau", "hamahiru",
            "hamabi", "hamaika", "hamar", "bederatzi", "zortzi",
            "zazpi", "sei", "bost", "lau", "hiru",
            "bi", "bat", "zero"
        ]
        self.ords = {
            1: "lehenengo",
            2: "bigarren",
            3: "hirugarren",
            4: "laugarren",
            5: "bosgarren",
            6: "seigarren",
            7: "zazpigarren",
            8: "zortzigarren",
            9: "bederatzigarren",
            10: "hamargarren",
        }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "bat"

        if nnum < cnum:
            if cnum < 100:
                # Para decenas (20, 40, 60, 80), usar forma contracta
                if cnum == 20:
                    return "hogeita %s" % ntext, cnum + nnum
                elif cnum == 40:
                    return "berrogeita %s" % ntext, cnum + nnum
                elif cnum == 60:
                    return "hirurogeita %s" % ntext, cnum + nnum
                elif cnum == 80:
                    return "laurogeita %s" % ntext, cnum + nnum
                return "%s eta %s" % (ctext, ntext), cnum + nnum
            return "%s %s" % (ctext, ntext), cnum + nnum
        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-1] + "ioi"

        if nnum == 100:
            if cnum == 2:
                return "berrehun", cnum * nnum
            elif cnum == 3:
                return "hirurehun", cnum * nnum
            elif cnum == 4:
                return "laurehun", cnum * nnum
            elif cnum == 5:
                return "bostehun", cnum * nnum
            elif cnum == 6:
                return "seiehun", cnum * nnum
            elif cnum == 7:
                return "zazpiehun", cnum * nnum
            elif cnum == 8:
                return "zortziehun", cnum * nnum
            elif cnum == 9:
                return "bederatziehun", cnum * nnum
            ntext = ntext
        else:
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 0:
            text = ""
        elif value <= 10:
            text = self.ords[value]
        else:
            text = self.to_cardinal(value) + "garren"

        return text.strip()

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%d." % value

    def to_currency(self, val, currency='EUR', cents=True, separator=' eta',
                    adjective=False):
        result = super(Num2Word_EUS, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)

        return result
