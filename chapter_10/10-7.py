#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-7.py
#   Last Modified : 2021-01-08 00:55
#   Describe      : 
#
# ====================================================



message = '输入的不是数字，程序退出.'

print("加法运算: ")

while True:
    try:
        num_1 = input("输入第一个数字: ")
        num_1 = int(num_1)
        num_2 = input("输入第二个数字: ")
        num_2 = int(num_2)
    except ValueError:
        print(message)
    else:
        res = num_1 + num_2
        print("res = " + str(res))
        choice = input("Continue(q for quit)? ")
        if choice == 'q':
            break



