#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 8-3.py
#   Last Modified : 2021-01-06 22:06
#   Describe      : 
#
# ====================================================



def make_shirt(size, word):
    """说明T恤的尺码和字样"""
    print("size: " + str(size) + '\n' + "word: " + word)

make_shirt(10, '你好')
make_shirt(word='你好', size=10)
