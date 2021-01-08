#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-4.py
#   Last Modified : 2021-01-07 23:08
#   Describe      : 
#
# ====================================================



file_name = 'guest_book.txt'

with open(file_name, 'w') as f:
    while True:
        name = input("输入名字(q for quit): ")
        if name == 'q':
            break
        print('Welcome.')
        f.write(name + '\n')
