#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 8-7.py
#   Last Modified : 2021-01-06 23:32
#   Describe      : 
#
# ====================================================



def make_album(singer, album, num=0):
    if num == 0:
        return { 'singer':singer, 'album':album }
    else:
        return { 'singer':singer, 'album':album, 'num':num }

message = make_album('歌手1', '专辑1')
print(message)

message = make_album('歌手2', '专辑2', 3)
print(message)

message = make_album('歌手3', '专辑3', num=9)
print(message)
