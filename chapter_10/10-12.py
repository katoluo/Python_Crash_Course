#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-12.py
#   Last Modified : 2021-01-08 10:34
#   Describe      : 
#
# ====================================================

import json

file_name = '10_12.json'
try:
    with open(file_name) as r_obj:
        num = json.load(r_obj)
except FileNotFoundError:
    with open(file_name, 'w') as w_obj:
        num = input('输入喜欢的一个数字: ')
        json.dump(num, w_obj)
else:
    print('I konw your favorite number! It is ' + num)
