#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 7-6.py
#   Last Modified : 2021-01-06 17:40
#   Describe      : 
#
# ====================================================



# 以7-5为例
# - 在 while 循环中使用条件测试来结束循环。
prompt = "年龄(quit for 退出): "

age = ''
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)

        if age < 3:
            print("免费")
        elif age >= 3 and age < 12:
            print("10美元")
        else:
            print("15美元")


# 使用变量 active 来控制循环结束的时机
prompt = "年龄(quit for 退出): "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("免费")
        elif age >= 3 and age < 12:
            print("10美元")
        else:
            print("15美元")

# 使用 break 语句在用户输入 'quit' 时退出循环。
# 看 7-5

