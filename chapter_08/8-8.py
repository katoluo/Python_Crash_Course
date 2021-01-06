#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2021  All rights reserved
#
#   Author        : kato
#   Email         : 1123629751@qq.com
#   File Name     : 8-8.py
#   Last Modified : 2021-01-06 23:48
#   Describe      : 
#
# ====================================================



def make_album(singer, album, num=0):
    if num == 0:
        return { 'singer':singer, 'album':album }
    else:
        return { 'singer':singer, 'album':album, 'num':num }


while True:
    singer = input("输入歌手名(q for quit): ")
    album = input("输入专辑名(q for quit): ")
    if singer == 'q' and album == 'q':
        break
    num = input("输入专辑歌曲数(0表示不知道): ")
    print(make_album(singer, album, num))
    
