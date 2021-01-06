#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 6-12.py
#   Last Modified : 2021-01-06 15:43
#   Describe      : 
#
# ====================================================



# 创建一个空的数组
aliens = []

alien = {
    'name': 'A',
    'color': 'green',
    'point': 5,
    'speed': 'slow',
}
aliens.append(alien)

alien = {
    'name': 'B',
    'color': 'yellow',
    'point': 10,
    'speed': 'med',
}
aliens.append(alien)

alien = {
    'name': 'C',
    'color': 'red',
    'point': 10,
    'speed': 'fast',
}
aliens.append(alien)

print(aliens)

# for循环打印
for alien_info in aliens:
    print("\nHere's what I know about " + alien_info['name'].title() + ":")
    for key, value in alien_info.items():
        print("\t" + key + ": " + str(value))
