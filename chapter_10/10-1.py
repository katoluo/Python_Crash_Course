#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-1.py
#   Last Modified : 2021-01-07 22:43
#   Describe      : 
#
# ====================================================



file_name = 'learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('\n')

with open(file_name) as file_object:
    for content in file_object:
        print(content.rstrip())

print('\n')

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
