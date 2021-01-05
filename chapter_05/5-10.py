#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 5-10.py
#   Last Modified : 2021-01-05 21:57
#   Describe      : 
#
# ====================================================



current_users = [ 'one', 'two', 'three', 'Four', 'five']
new_users = [ 'four', 'FIve', 'six', 'seven', 'eight' ]

current_users_lower = [value.lower() 
                       for value in current_users]

for username in new_users:
    if username.lower() in current_users_lower:
        print("已存在，重新输入用户名。")
    else:
        print("用户名未被使用。")
