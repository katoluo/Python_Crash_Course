#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 8-5.py
#   Last Modified : 2021-01-06 22:27
#   Describe      : 
#
# ====================================================



def describe_city(cityname,contury='China'):
    print(cityname.title() + " is in " + contury.title())

describe_city('beijing')
describe_city('NewYork','American')
describe_city('chengdu')
