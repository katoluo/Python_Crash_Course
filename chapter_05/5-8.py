#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 5-8.py
#   Last Modified : 2021-01-05 21:43
#   Describe      : 
#
# ====================================================



users = [ 'one', 'two', 'three', 'four', 'admin' ]

for username in users:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")
