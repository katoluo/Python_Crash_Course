#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 7-2.py
#   Last Modified : 2021-01-06 16:37
#   Describe      : 
#
# ====================================================



number = input("有多少人用餐: ")
number = int(number)

if number > 8:
    print("没有空桌。")
else:
    print("有空桌。")
