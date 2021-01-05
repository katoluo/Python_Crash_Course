#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 5-11.py
#   Last Modified : 2021-01-05 22:56
#   Describe      : 
#
# ====================================================



numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(str(num) + "th")
