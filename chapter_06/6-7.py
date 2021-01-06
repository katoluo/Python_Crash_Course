#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 6-7.py
#   Last Modified : 2021-01-06 15:23
#   Describe      : 
#
# ====================================================




me = {
    'first_name':'kato',
    'last_name':'luo',
    'age':20,
    'city':'MeiZhou',
}

you = {
    'first_name':'zahrawind',
    'last_name':'zhan',
    'age':'19',
    'city':'MeiZhou',
}

she = {
    'first_name':'aragne',
    'last_name':'unknown',
    'age':'unknown',
    'city':'unknown',
}

people = []
people.append(me)
people.append(you)
people.append(she)

print('\tfirst_name' + '\tlast_name' + '\tage' + '\tcity')
for value in people:
    print('\t' + value['first_name'] + '\t' + value['last_name']
          + '\t' + str(value['age']) + '\t' + value['city'])


