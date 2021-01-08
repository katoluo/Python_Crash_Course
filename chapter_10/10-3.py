#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-3.py
#   Last Modified : 2021-01-07 23:03
#   Describe      : 
#
# ====================================================



file_name = 'guest.txt'

with open(file_name, 'w') as f:
    name = input("输入名字: ")
    f.write(name + '\n')
