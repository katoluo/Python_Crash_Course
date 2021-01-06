#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 6-6.py
#   Last Modified : 2021-01-06 13:35
#   Describe      : 
#
# ====================================================



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = [ 'jen', 'kato', 'phil' ]

for user in users:
    if user in favorite_languages.keys():
        print('感谢！')
    else:
        print('请参与调查！')
