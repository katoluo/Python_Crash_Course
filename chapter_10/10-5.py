#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-5.py
#   Last Modified : 2021-01-07 23:13
#   Describe      : 
#
# ====================================================



file_name = '10_5.txt'
message = "What's your name? "
why = 'why are you like programing? '

with open(file_name, 'w') as f:
    while True:
        name = input(message)
        reason = input(why)
        f.write(name + ': ' + reason + '\n')
        choice = input("Continue(q for quit)? ")
        if choice == 'q':
            break
