#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 8-6.py
#   Last Modified : 2021-01-06 23:18
#   Describe      : 
#
# ====================================================



def city_country(city, country):
    format = city + ', ' + country
    return format

message = city_country('BEIJING', 'CHINA')
print(message)
message = city_country('SHANGHAI', 'CHINA')
print(message)
message = city_country('GUANGZHOU', 'CHINA')
print(message)
