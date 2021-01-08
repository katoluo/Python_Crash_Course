#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-10.py
#   Last Modified : 2021-01-08 10:25
#   Describe      : 
#
# ====================================================

import json

file_name = '10_11.json'

try:
    num = input('输入一个喜欢的数字: ')
    num = int(num)
except ValueError:
    print('输入错误，退出程序。')
else:
    with open(file_name, 'w') as f_obj:
        json.dump(num, f_obj)

with open(file_name) as f_obj:
    num = json.load(f_obj)
    print("I konw your favorite number! It's " + str(num))
