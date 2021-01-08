#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : file_reader.py
#   Last Modified : 2021-01-07 21:12
#   Describe      : 
#
# ====================================================



with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
