#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 6-5.py
#   Last Modified : 2021-01-06 13:31
#   Describe      : 
#
# ====================================================



river = {
    'river1':'country1',
    'river2':'country2',
    'river3':'country3',
}

for key, value in river.items():
    print('The ' + key + ' runs through ' + value)

for key in river:
    print(key)

for value in river.values():
    print(value)
