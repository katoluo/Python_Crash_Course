#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 9-2.py
#   Last Modified : 2021-01-07 12:10
#   Describe      : 
#
# ====================================================



class Restaurant():
    '''空'''
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print("restaurant_name: " + self.name)
        print("cuisine_type: " + self.type)

    def open_restaurant(self):
        print("the " + self.name + " restaurant is opening.")

restaurant1 = Restaurant('goodeating_1', 'type_1')
restaurant2 = Restaurant('goodeating_2', 'type_2')
restaurant3 = Restaurant('goodeating_3', 'type_3')


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
