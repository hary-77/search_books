# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:46:38 2020

@author: 森下　源太
"""

tag={"Ruby":"Rubyの本","python":"みんなのpython\nPython本","スクラム":"スクラムマスターザブック"}
title={"みんな":"みんなのpython","python":"みんなのpython\nPython本"}
author={"柴田淳":"みんなのpython"}
publisher={"SBクリエイティブ":"みんなのpython"}


import sys
data=sys.argv[1:]

 

for i in data:
    try:
        print("\nタグ "+"『"+i+"』"+" の検索結果は:\n\n"+tag[i])
    except KeyError:
            try:
                print("\nタイトル "+"『"+i+"』"+" の検索結果は:\n\n"+title[i])
            except KeyError:
                    try:
                        print("\n著者 "+"『"+i+"』"+" の検索結果は:\n\n"+author[i])
                    except KeyError:
                        try:
                            print("\n出版社 "+"『"+i+"』"+" の検索結果は:\n\n"+publisher[i])
                        except KeyError:
                            print("\n"+"※『"+i+"』"+" というキーワードと一致する本は存在しません")
