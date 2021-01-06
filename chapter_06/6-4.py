#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 6-4.py
#   Last Modified : 2021-01-06 13:16
#   Describe      : 
#
# ====================================================



vocabulary = {
    'for':'loop',
    'if':'test condition',
    'else':'condition fail',
    'range':'range_number',
    'list':'list function',
}

#print('for: ' + vocabulary['for'])
#print('if: ' + vocabulary['if'])
#print('else: ' + vocabulary['else'])
#print('range: ' + vocabulary['range'])
#print('list: ' + vocabulary['list'])

for key, value in vocabulary.items():
    print(key + ': ' + value)

