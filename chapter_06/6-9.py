#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 6-9.py
#   Last Modified : 2021-01-06 15:38
#   Describe      : 
#
# ====================================================



favorite_places = {
    'znn': ['chengdu', 'shanghai', 'hangzhou'],
    'yl': ['chengdu', 'huang montains'],
    'other': ['xian', 'xinjiang', 'nanji']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
