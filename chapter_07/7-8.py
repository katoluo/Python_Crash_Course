#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 7-8.py
#   Last Modified : 2021-01-06 18:00
#   Describe      : 
#
# ====================================================



sandwich_orders = [ 'sandwich_one', 'sandwich_two','sandwich_three']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)
