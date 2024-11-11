

from __future__ import division, print_function, unicode_literals

import math

from .lang_EU import Num2Word_EU

GENERIC_DOLLARS = ('dòlar', 'dòlars')
GENERIC_CENTS = ('cèntim', 'cèntims')
CURRENCIES_UNA = ('SLL', 'SEK', 'NOK', 'CZK', 'DKK', 'ISK',
                  'SKK', 'GBP', 'CYP', 'EGP', 'FKP', 'GIP',
                  'LBP', 'SDG', 'SHP', 'SSP', 'SYP', 'INR',
                  'IDR', 'LKR', 'MUR', 'NPR', 'PKR', 'SCR',
                  'ESP', 'TRY', 'ITL')
CENTS_UNA = ('EGP', 'JOD', 'LBP', 'SDG', 'SSP', 'SYP')


class Num2Word_CA(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euros'), ('cèntim', 'cèntims')),
        'ESP': (('pesseta', 'pessetes'), ('cèntim', 'cèntims')),
        'USD': (('dòlar', 'dòlars'), ('cèntim', 'cèntims')),
        'PEN': (('sol', 'sols'), ('cèntim', 'cèntims')),
        'CRC': (('colon', 'colons'), ('cèntim', 'cèntims')),
        'AUD': (('dòlar australià', 'dòlars australians'), ('cèntim', 'cèntims')),
        'CAD': (('dòlar canadenc', 'dòlars canadencs'), ('cèntim', 'cèntims')),
        'GBP': (('lliura', 'lliures'), ('penic', 'penics')),
        'RUB': (('ruble', 'rubles'), ('kopek', 'kopeks')),
        'SEK': (('corona sueca', 'corones sueques'), ('öre', 'öre')),
        'NOK': (('corona noruega', 'corones noruegues'), ('øre', 'øre')),
        'PLN': (('zloty', 'zlotys'), ('grosz', 'groszy')),
        'MXN': (('peso mexicà', 'pesos mexicans'), ('cèntim', 'cèntims')),
        'RON': (('leu romanès', 'lei romanesos'), ('ban', 'bani')),
        'INR': (('rupia índia', 'rupies índies'), ('paisa', 'paisas')),
        'HUF': (('fòrint', 'fòrints'), ('fillér', 'fillér')),
        'FRF': (('franc francès', 'francs francesos'), ('cèntim', 'cèntims')),
        'CNY': (('yuan xinès', 'yuans xinesos'), ('fen', 'jiaos')),
        'CZK': (('corona txeca', 'corones txeques'), ('haléř', 'haléř')),
        'NIO': (('còrdoba nicaragüenc', 'còrdobas nicaragüencs'), ('cèntim', 'cèntims')),
        'VES': (('bolívar veneçolà', 'bolívars veneçolans'), ('cèntim', 'cèntims')),
        'BRL': (('real brasiler', 'reals brasilers'), ('cèntim', 'cèntims')),
        'CHF': (('franc suís', 'francs suïssos'), ('cèntim', 'cèntims')),
        'JPY': (('ien japonès', 'iens japonesos'), ('sen', 'sen')),
        'KRW': (('won sud-coreà', 'wons sud-coreans'), ('jeon', 'jeon')),
        'KPW': (('won nord-coreà', 'wons nord-coreans'), ('chon', 'chon')),
        'TRY': (('lira turca', 'lires turques'), ('kuruş', 'kuruş')),
        'ZAR': (('rand sud-africà', 'rands sud-africans'), ('cèntim', 'cèntims')),
        'KZT': (('tenge kazakh', 'tenges kazakhs'), ('tïın', 'tïın')),
        'UAH': (('hrívnia ucraïnesa', 'hrívnies ucraïneses'), ('kopiyka', 'kopiykas')),
        'THB': (('baht tailandès', 'bahts tailandesos'), ('satang', 'satang')),
        'AED': (('dirham de l\'EAU', 'dirhams de l\'EAU'), ('fils', 'fils')),
        'AFN': (('afghani afganès', 'afghanis afganesos'), ('pul', 'puls')),
        'ALL': (('lek albanès', 'leke albanesos'), ('qindarkë', 'qindarka')),
        'AMD': (('dram armeni', 'drams armenis'), ('luma', 'lumas')),
        'ANG': (('florí de les Antilles Neerlandeses', 'florins de les Antilles Neerlandeses'), ('cèntim', 'cèntims')),
        'AOA': (('kwanza angolès', 'kwanzas angolesos'), ('cèntim', 'cèntims')),
        'ARS': (('peso argentí', 'pesos argentins'), ('cèntim', 'cèntims')),
        'AWG': (('florí arubà', 'florins arubans'), ('cèntim', 'cèntims')),
        'AZN': (('manat azerbaidjanès', 'manats azerbaidjanesos'), ('qəpik', 'qəpik')),
        'BBD': (('dòlar de Barbados', 'dòlars de Barbados'), ('cèntim', 'cèntims')),
        'BDT': (('taka bangladeixí', 'takas bangladeixís'), ('paisa', 'paisas')),
        'BGN': (('lev búlgar', 'leva búlgars'), ('stotinka', 'stotinki')),
        'BHD': (('dinar de Bahrain', 'dinars de Bahrain'), ('fils', 'fils')),
        'BIF': (('franc burundès', 'francs burundesos'), ('cèntim', 'cèntims')),
        'BMD': (('dòlar de Bermudes', 'dòlars de Bermudes'), ('cèntim', 'cèntims')),
        'BND': (('dòlar de Brunei', 'dòlars de Brunei'), ('cèntim', 'cèntims')),
        'BOB': (('bolivià', 'bolivians'), ('cèntim', 'cèntims')),
        'BSD': (('dòlar bahamià', 'dòlars bahamians'), ('cèntim', 'cèntims')),
        'BTN': (('ngultrum butanès', 'ngultrums butanesos'), ('chetrum', 'chetrum')),
        'BWP': (('pula botswanesa', 'pulas botswaneses'), ('thebe', 'thebes')),
        'BYN': (('ruble bielorús', 'rubles bielorussos'), ('kópek', 'kópeks')),
        'BZD': (('dòlar belizià', 'dòlars belizians'), ('cèntim', 'cèntims')),
        'CDF': (('franc congolès', 'francs congolesos'), ('cèntim', 'cèntims')),
        'CLP': (('peso xilè', 'pesos xilens'), ('cèntim', 'cèntims')),
        'COP': (('peso colombià', 'pesos colombians'), ('cèntim', 'cèntims')),
        'CUP': (('peso cubà', 'pesos cubans'), ('cèntim', 'cèntims')),
        'CVE': (('escut de Cap Verd', 'escuts de Cap Verd'), ('cèntim', 'cèntims')),
        'DJF': (('franc djiboutià', 'francs djiboutians'), ('cèntim', 'cèntims')),
        'DKK': (('corona danesa', 'corones daneses'), ('øre', 'øre')),
        'DOP': (('peso dominicà', 'pesos dominicans'), ('cèntim', 'cèntims')),
        'DZD': (('dinar algerià', 'dinars algerians'), ('cèntim', 'cèntims')),
        'EGP': (('lliura egípcia', 'lliures egípcies'), ('piastra', 'piastras')),
        'ERN': (('nakfa eritreu', 'nakfas eritreus'), ('cèntim', 'cèntims')),
        'ETB': (('birr etíop', 'birrs etíops'), ('cèntim', 'cèntims')),
        'FJD': (('dòlar fijià', 'dòlars fijians'), ('cèntim', 'cèntims')),
        'FKP': (('lliura de les Illes Falkland', 'lliures de les Illes Falkland'), ('penic', 'penics')),
        'GEL': (('lari georgià', 'laris georgians'), ('tetri', 'tetris')),
        'GHS': (('cedi ghanès', 'cedis ghanesos'), ('pesewa', 'pesewas')),
        'GIP': (('lliura de Gibraltar', 'lliures de Gibraltar'), ('penic', 'penics')),
        'GMD': (('dalasi gambià', 'dalasis gambians'), ('butut', 'bututs')),
        'GNF': (('franc guineà', 'francs guineans'), ('cèntim', 'cèntims')),
        'GTQ': (('quetzal guatemalenc', 'quetzals guatemalencs'), ('cèntim', 'cèntims')),
        'GYD': (('dòlar guyanès', 'dòlars guyanesos'), ('cèntim', 'cèntims')),
        'HKD': (('dòlar de Hong Kong', 'dòlars de Hong Kong'), ('cèntim', 'cèntims')),
        'HNL': (('lempira hondurenya', 'lempires hondurenyes'), ('cèntim', 'cèntims')),
        'HRK': (('kuna croata', 'kunes croates'), ('lipa', 'lipas')),
        'HTG': (('gourde haitià', 'gourdes haitians'), ('cèntim', 'cèntims')),
        'IDR': (('rupia indonèsia', 'rupies indonèsies'), ('cèntim', 'cèntims')),
        'ILS': (('nou séquel israelià', 'nous séquels israelians'), ('agorà', 'agorot')),
        'IQD': (('dinar iraquià', 'dinars iraquians'), ('fils', 'fils')),
        'IRR': (('rial iranià', 'rials iranians'), ('dinar', 'dinars')),
        'ISK': (('corona islandesa', 'corones islandeses'), ('aurar', 'aurar')),
        'JMD': (('dòlar jamaicà', 'dòlars jamaicans'), ('cèntim', 'cèntims')),
        'JOD': (('dinar jordà', 'dinars jordans'), ('piastra', 'piastras')),
        'KES': (('xíling kenyà', 'xílings kenyans'), ('cèntim', 'cèntims')),
        'KGS': (('som kirguís', 'soms kirguisos'), ('tyiyn', 'tyiyn')),
        'KHR': (('riel cambodjà', 'riels cambodjans'), ('cèntim', 'cèntims')),
        'KMF': (('franc de les Comores', 'francs de les Comores'), ('cèntim', 'cèntims')),
        'KWD': (('dinar kuwaití', 'dinars kuwaitís'), ('fils', 'fils')),
        'KYD': (('dòlar de les Illes Caiman', 'dòlars de les Illes Caiman'), ('cèntim', 'cèntims')),
        'LAK': (('kip laosià', 'kips laosians'), ('at', 'at')),
        'LBP': (('lliura libanesa', 'lliures libaneses'), ('piastra', 'piastras')),
        'LKR': (('rupia de Sri Lanka', 'rupies de Sri Lanka'), ('cèntim', 'cèntims')),
        'LRD': (('dòlar liberià', 'dòlars liberians'), ('cèntim', 'cèntims')),
        'LSL': (('loti de Lesotho', 'lotis de Lesotho'), ('sente', 'sente')),
        'LYD': (('dinar libi', 'dinars libis'), ('dirham', 'dirhams')),
        'MAD': (('dírham marroquí', 'dírhams marroquins'), ('santim', 'santimat')),
        'MDL': (('leu moldau', 'lei moldaus'), ('ban', 'bani')),
        'MGA': (('ariary malgaix', 'ariarys malgaixos'), ('iraimbilanja', 'iraimbilanja')),
        'MKD': (('denar macedoni', 'denars macedonis'), ('deni', 'deni')),
        'MMK': (('kyat de Myanmar', 'kyats de Myanmar'), ('pya', 'pyas')),
        'MNT': (('tugrik mongol', 'tugriks mongols'), ('möngö', 'möngö')),
        'MOP': (('pataca de Macau', 'pataques de Macau'), ('avo', 'avos')),
        'MRO': (('ouguiya maurità', 'ouguiyas mauritanes'), ('khoums', 'khoums')),
        'MRU': (('ouguiya maurità', 'ouguiyas mauritanes'), ('khoums', 'khoums')),  # Mantenido igual, cambio de código
        'MUR': (('rupia mauriciana', 'rupies mauricianes'), ('cèntim', 'cèntims')),
        'MVR': (('rufiyaa maldiva', 'rufiyaas maldives'), ('laari', 'laari')),
        'MWK': (('kwacha malauí', 'kwachas malauís'), ('tambala', 'tambalas')),
        'MYR': (('ringgit malai', 'ringgits malais'), ('sen', 'sen')),
        'MZN': (('metical moçambiquès', 'meticals moçambiquesos'), ('cèntim', 'cèntims')),
        'NAD': (('dòlar namibià', 'dòlars namibians'), ('cèntim', 'cèntims')),
        'NGN': (('naira nigerià', 'nairas nigerianes'), ('kobo', 'kobo')),
        'NPR': (('rupia nepalesa', 'rupies nepaleses'), ('paisa', 'paisas')),
        'NZD': (('dòlar neozelandès', 'dòlars neozelandesos'), ('cèntim', 'cèntims')),
        'OMR': (('rial omaní', 'rials omanís'), ('baisa', 'baisa')),
        'PAB': (('balboa panameny', 'balboas panamenys'), ('cèntim', 'cèntims')),
        'PGK': (('kina papuanova-guineana', 'kinas papuanova-guineanes'), ('toea', 'toea')),
        'PHP': (('peso filipí', 'pesos filipins'), ('cèntim', 'cèntims')),
        'PKR': (('rupia pakistanesa', 'rupies pakistaneses'), ('paisa', 'paisas')),
        'PLZ': (('zloty polonès', 'zlotys polonesos'), ('grosz', 'groszy')),
        'PYG': (('guaraní paraguaià', 'guaranís paraguaians'), ('cèntim', 'cèntims')),
        'QAR': (('rial qatarià', 'rials qataris'), ('dirham', 'dirhams')),
        'QTQ': (('quetzal guatemalenc', 'quetzals guatemalencs'), ('cèntim', 'cèntims')),  # Repetición, posible error
        'RSD': (('dinar serbi', 'dinars serbis'), ('para', 'para')),
        'RUR': (('ruble rus', 'rubles russos'), ('kopek', 'kopeks')),
        'RWF': (('franc ruandès', 'francs ruandesos'), ('cèntim', 'cèntims')),
        'SAR': (('riyal saudita', 'riyals saudites'), ('halala', 'halalas')),
        'SBD': (('dòlar de les Illes Salomó', 'dòlars de les Illes Salomó'), ('cèntim', 'cèntims')),
        'SCR': (('rupia de les Seychelles', 'rupies de les Seychelles'), ('cèntim', 'cèntims')),
        'SDG': (('lliura sudanesa', 'lliures sudaneses'), ('piastra', 'piastras')),
        'SGD': (('dòlar de Singapur', 'dòlars de Singapur'), ('cèntim', 'cèntims')),
        'SHP': (('lliura de Santa Helena', 'lliures de Santa Helena'), ('penic', 'penics')),
        'SLL': (('leone de Sierra Leone', 'leones de Sierra Leone'), ('cèntim', 'cèntims')),
        'SRD': (('dòlar surinamès', 'dòlars surinamesos'), ('cèntim', 'cèntims')),
        'SSP': (('lliura del Sudan del Sud', 'lliures del Sudan del Sud'), ('piastra', 'piastras')),
        'STD': (('dobra de São Tomé i Príncipe', 'dobras de São Tomé i Príncipe'), ('cèntim', 'cèntims')),
        'SVC': (('colon salvadorenc', 'colons salvadorencs'), ('cèntim', 'cèntims')),
        'SYP': (('lliura siriana', 'lliures sirianes'), ('piastra', 'piastras')),
        'SZL': (('lilangeni swazi', 'emalangeni swazis'), ('cèntim', 'cèntims')),
        'TJS': (('somoni tadjik', 'somonis tadjiks'), ('diram', 'dirams')),
        'TMT': (('manat turcman', 'manats turcmans'), ('tenge', 'tenge')),
        'TND': (('dinar tunisià', 'dinars tunisians'), ('mil·lèsim', 'mil·lèsims')),
        'TOP': (('paʻanga tongà', 'paʻangas tongans'), ('seniti', 'seniti')),
        'TTD': (('dòlar de Trinidad i Tobago', 'dòlars de Trinidad i Tobago'), ('cèntim', 'cèntims')),
        'TWD': (('nou dòlar taiwanès', 'nous dòlars taiwanesos'), ('cèntim', 'cèntims')),
        'TZS': (('xíling tanzà', 'xílings tanzans'), ('cèntim', 'cèntims')),
        'UAG': (('hrívnia ucraïnesa', 'hrívnies ucraïneses'), ('kopiyka', 'kopiykas')),  # Repetición, posible error
        'UGX': (('xíling ugandès', 'xílings ugandesos'), ('cèntim', 'cèntims')),
        'UYU': (('peso uruguaià', 'pesos uruguaians'), ('cèntim', 'cèntims')),
        'UZS': (('sum uzbek', 'sums uzbeks'), ('tiyin', 'tiyin')),
        'VEF': (('bolívar venezolà fort', 'bolívars venezolans forts'), ('cèntim', 'cèntims')),
        'VND': (('dong vietnamita', 'dongs vietnamites'), ('xu', 'hào')),
        'VUV': (('vatu de Vanuatu', 'vatus de Vanuatu'), ('no té', 'no té')),  # Sin subdivisión
        'WST': (('tala samoà', 'talas samoans'), ('sene', 'sene')),
        'XAF': (('franc CFA BEAC', 'francs CFA BEAC'), ('cèntim', 'cèntims')),
        'XCD': (('dòlar del Carib Oriental', 'dòlars del Carib Oriental'), ('cèntim', 'cèntims')),
        'XOF': (('franc CFA BCEAO', 'francs CFA BCEAO'), ('cèntim', 'cèntims')),
        'XPF': (('franc CFP', 'francs CFP'), ('cèntim', 'cèntims')),
        'YER': (('rial iemenita', 'rials iemenites'), ('fils', 'fils')),
        'YUM': (('dinar iugoslau', 'dinars iugoslaus'), ('para', 'para')),
        'ZMW': (('kwacha zambià', 'kwachas zambians'), ('ngwee', 'ngwee')),
        'ZRZ': (('zaire zairenc', 'zaires zairencs'), ('likuta', 'makuta')),
        'ZWL': (('dòlar zimbabuès', 'dòlars zimbabuesos'), ('cèntim', 'cèntims')),
    }

    # //CHECK: Is this sufficient??
    GIGA_SUFFIX = None
    MEGA_SUFFIX = "ilió"

    def setup(self):
        lows = ["quatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menys "
        self.pointword = "coma"
        self.errmsg_nonnum = "type(%s) no és [long, int, float]"
        self.errmsg_floatord = "El float %s no pot ser tractat com a" \
            " ordinal."
        self.errmsg_negord = "El número negatiu %s no pot ser tractat" \
            " com a ordinal."
        self.errmsg_toobig = (
            "abs(%s) ha de ser inferior a %s."
        )
        self.gender = "m"
        self.exclude_title = ["i", "menys", "coma"]
        self.mid_numwords = [
            (1000, "mil"),
            (100, "cent"),
            (90, "noranta"),
            (80, "vuitanta"),
            (70, "setanta"),
            (60, "seixanta"),
            (50, "cinquanta"),
            (40, "quaranta"),
            (30, "trenta")
        ]
        self.low_numwords = [
            "vint-i-nou", "vint-i-vuit", "vint-i-set", 
            "vint-i-sis", "vint-i-cinc", "vint-i-quatre", 
            "vint-i-tres", "vint-i-dos", "vint-i-u", 
            "vint", "dinou", "divuit", "disset", 
            "setze", "quinze", "catorze", "tretze", 
            "dotze", "onze", "deu", "nou", "vuit", 
            "set", "sis", "cinc", "quatre", "tres", 
            "dos", "u", "zero"
        ]
        self.ords = {
            1: "primer",
            2: "segon",
            3: "tercer",
            4: "quart",
            5: "cinquè",
            6: "sisè",
            7: "setè",
            8: "vuitè",
            9: "novè",
            10: "desè",
        }


    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "un"

        if nnum < cnum:
            if cnum < 100:
                return "%s-%s" % (ctext, ntext), cnum + nnum
            return "%s %s" % (ctext, ntext), cnum + nnum
        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-3] + "ns"

        #print(nnum)
        if nnum == 100:
            ntext += "s"
        else:
            #print(ntext)
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 0:
            text = ""
        elif value <= 10:
            text = self.ords[value]
        else:
            text = self.to_cardinal(value)
            
            if text.endswith("e"):
                text = text.replace("e","è")
            else:
                text += "è"

        return text.strip()


    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        result = ""

        if value == 1:
            result = "1a" if self.gender == 'f' else "1r"
        elif value == 2:
            result = "2a" if self.gender == 'f' else "2n"
        elif value == 3:
            result = "3a" if self.gender == 'f' else "3r"
        elif value == 4:
            result = "4a" if self.gender == 'f' else "4t"
        else:
            result = "%d%s" % (value ,"a" if self.gender == 'f' else "è")
        return result

    def to_currency(self, val, currency='EUR', cents=True, separator=' amb',
                    adjective=False):
        result = super(Num2Word_CA, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        
        list_result = result.split(separator + " ")

        if currency in CURRENCIES_UNA:

            # "una liura", "vintiuna lliures"...
            #list_result[0] = list_result[0].replace("u", "una")

            # "doscentes lliures"
            list_result[0] = list_result[0].replace("cents", "centes")

        list_result[0] = list_result[0].replace("vint-i-u", "vint-i-un")

        #list_result[0] = list_result[0].replace("u", "un")

        # "CENTS" PART (list_result[1])

        #if currency in CENTS_UNA:

        #    list_result[1] = list_result[1].replace("un", "una")

        list_result[1] = list_result[1].replace("vint-i-u", "vint-i-un")

        #list_result[1] = list_result[1].replace("u", "un")

        # join back "dollars" part with "cents" part
        result = (separator + " ").join(list_result)

        return result
