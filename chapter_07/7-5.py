#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 7-5.py
#   Last Modified : 2021-01-06 17:27
#   Describe      : 
#
# ====================================================



prompt = "年龄(quit for 退出): "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    
    if age < 3:
        print("免费")
    elif age >= 3 and age < 12:
        print("10美元")
    else:
        print("15美元")
