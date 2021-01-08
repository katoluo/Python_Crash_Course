#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 10-2.py
#   Last Modified : 2021-01-07 22:50
#   Describe      : 
#
# ====================================================



file_name = 'learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    contents = contents.rstrip()
    print(contents.replace('Python', 'C'))

print('\n')

with open(file_name) as file_object:
    for content in file_object:
        content = content.rstrip()
        print(content.replace('Python', 'C'))

print('\n')

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))
