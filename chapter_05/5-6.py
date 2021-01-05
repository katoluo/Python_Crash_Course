#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 5-6.py
#   Last Modified : 2021-01-05 21:23
#   Describe      : 
#
# ====================================================

age = 22

if age < 2:
    print("婴儿")
elif age >= 2 and age < 4:
    print("蹒跚学步")
elif age >= 4 and age < 13:
    print("儿童")
elif age >= 13 and age < 20:
    print("青少年")
elif age >= 20 and age < 65:
    print("成年人")
else:
    print("老年人")


