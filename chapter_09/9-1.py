#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 9-1.py
#   Last Modified : 2021-01-07 12:06
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

restaurant = Restaurant('goodeating_res', 'good_type')

print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
