#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 7-4.py
#   Last Modified : 2021-01-06 17:22
#   Describe      : 
#
# ====================================================



prompt = "输入配料: "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print("添加" + message)

