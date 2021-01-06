#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 8-11.py
#   Last Modified : 2021-01-07 00:25
#   Describe      : 
#
# ====================================================



def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    great_magicians = []
    while names:
        magician = names.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        names.append(great_magician)
    
    return names


magicians = ['znn','david','amy']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)
