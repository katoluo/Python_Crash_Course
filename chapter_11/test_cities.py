#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : test_cities.py
#   Last Modified : 2021-01-08 15:32
#   Describe      : 
#
# ====================================================



import unittest

from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        res = city_country('Shanghai', 'China')
        self.assertEqual(res, 'Shanghai, China')

unittest.main()
