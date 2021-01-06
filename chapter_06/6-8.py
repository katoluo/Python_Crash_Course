#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 6-8.py
#   Last Modified : 2021-01-06 15:35
#   Describe      : 
#
# ====================================================



pets = []

pet = {
    'type': 'fish',
    'name': 'john',
    'owner': 'guido',
}
pets.append(pet)

pet = {
    'type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
}
pets.append(pet)

pet = {
    'type': 'dog',
    'name': 'peso',
    'owner': 'eric',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
