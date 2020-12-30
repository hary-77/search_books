# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:49:18 2020

@author: 森下　源太
"""


def n_gram(minpy, n):
    return [ minpy[idx:idx + n] for idx in range(len(minpy) - n + 1)]



minpy ="みんなのpython"


tit="みんなのpyton" #入力



for i in n_gram(minpy,2):
    if i in tit:
        print("みんなのpython")
        break
    else:
        print("Not Found")


