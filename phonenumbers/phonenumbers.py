# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import
import re

import jaconvV2


class TelFormatter(object):

    def _get_re_freagment(file):
        with open(file) as f:
            lines = f.readlines()
        return "|".join(map(lambda s: s.split('\n')[0], lines))

    AREA_CODES = _get_re_freagment(file='phonenumbers/data/area_codes.txt')
    SPECIAL_CODES_10 = _get_re_freagment(file='phonenumbers/data/special_codes_10.txt')
    SPECIAL_CODES_11 = _get_re_freagment(file='phonenumbers/data/special_codes_11.txt')
    CELLPHONE_CODES = _get_re_freagment(file='phonenumbers/data/special_codes_10.txt')

    AREA_CODE_REGEXP = fr'\A({AREA_CODES})(\d{{1,4}})(\d{{4}})\Z'
    SPECIAL_CODE_10_REGEXP= fr'\A({SPECIAL_CODES_10})(\d{{6}})\Z'
    SPECIAL_CODE_11_REGEXP= fr'\A({SPECIAL_CODES_11})(\d{{7}})\Z'
    CELLPHONE_CODE_10_REGEXP= fr'\A({CELLPHONE_CODES})(\d{{3}})(\d{{4}})\Z'
    CELLPHONE_CODE_REGEXP= fr'\A({CELLPHONE_CODES})([1-9]\d{{3}})(\d{{4}})\Z'

    @classmethod
    def format(cls, tel):
        return "-".join(cls.split(tel=tel))

    @classmethod
    def split(self, tel):
        tel = self.preprocess(tel)
        if len(tel) == 10:
            if re.match(self.AREA_CODE_REGEXP, tel):
                f = re.findall(self.AREA_CODE_REGEXP, tel)
                return tuple(tuple(*f[:2]))
            elif re.match(self.SPECIAL_CODE_10_REGEXP, tel):
                f = re.findall(self.SPECIAL_CODE_10_REGEXP, tel)
                return tuple(tuple(*f[:1]))
            elif re.match(self.CELLPHONE_CODE_10_REGEXP, tel):
                f = re.findall(self.CELLPHONE_CODE_10_REGEXP, tel)
                return tuple(tuple(*f[:2]))
            else:
                raise Exception("Invalid telephone number")
        elif len(tel) == 11:
            if re.match(self.CELLPHONE_CODE_REGEXP, tel):
                f = re.findall(self.CELLPHONE_CODE_REGEXP, tel)
                return tuple(tuple(*f[:2]))
            elif re.match(self.SPECIAL_CODE_11_REGEXP, tel):
                f = re.findall(self.SPECIAL_CODE_11_REGEXP, tel)
                return tuple(tuple(*f[:1]))
            else:
                raise Exception("Invalid telephone number")
        else:
            raise Exception("Invalid telephone number")

    @classmethod
    def preprocess(self, tel):
        return re.sub('[^\d]', '', jaconvV2.z2h(tel, digit=True))
