# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:39:15 2020

@author: 森下　源太
"""



from PIL import Image
import numpy as np

img_minpy=Image.open("C:\pbl\images\minpy.jpg")
width, heigit = img_minpy.size

from collections import defaultdict

ti= defaultdict(list)                          #ディクショナリ（タイトル）
ti["み"].append("みんなのpython")
ti["みん"].append("みんなのpython")
ti["みんな"].append("みんなのpython")
ti["みんなの"].append("みんなのpython")
ti["みんなのpython"].append("みんなのpython")
ti["python"].append("みんなのpython")
ti["py"].append("みんなのpython")
ti["p"].append("みんなのpython")

ti["python"].append("python本")
ti["py"].append("python本")
ti["p"].append("python本")





aut= defaultdict(list)                          #ディクショナリ（著者）
aut["柴田淳"].append("みんなのpython")
aut["柴"].append("みんなのpython")
aut["柴田"].append("みんなのpython")
aut["淳"].append("みんなのpython")
aut["柴田　淳"].append("みんなのpython")
aut["しばたりょう"].append("みんなのpython")
aut["し"].append("みんなのpython")
aut["しばた"].append("みんなのpython")
aut["りょう"].append("みんなのpython")
aut["しばた　りょう"].append("みんなのpython")




pub= defaultdict(list)                          #ディクショナリ（出版社）
pub["SBクリエイティブ"].append("みんなのpython")
pub["ｓｂクリエイティブ"].append("みんなのpython")
pub["S"].append("みんなのpython")
pub["SB"].append("みんなのpython")
pub["s"].append("みんなのpython")
pub["sb"].append("みんなのpython")
pub["クリエイティブ"].append("みんなのpython")





tag= defaultdict(list)                            #ディクショナリ（タグ）
tag["python"].append("みんなのpython")
tag["p"].append("みんなのpython")
tag["py"].append("みんなのpython")
tag["pyt"].append("みんなのpython")
tag["Python"].append("みんなのpython")
tag["PYTHON"].append("みんなのpython")

tag["python"].append("python本")
tag["p"].append("python本")
tag["py"].append("python本")
tag["pyt"].append("python本")
tag["Python"].append("python本")
tag["PYTHON"].append("python本")


tag["Ruby"].append("Rubyの本")
tag["R"].append("Rubyの本")
tag["Ru"].append("Rubyの本")
tag["ruby"].append("Rubyの本")
tag["r"].append("Rubyの本")
tag["ru"].append("Rubyの本")

tag["スクラム"].append("スクラムマスターザブック")
tag["すくらむ"].append("スクラムマスターザブック")
tag["ス"].append("スクラムマスターザブック")
tag["す"].append("スクラムマスターザブック")



input1=["p"]                #データ入力（タイトル）
input2=[]                  #データ入力（著者）
input3=[]                  #データ入力（出版社）
input4=["R","す","p"]      #データ入力（タグ）


la=[]     #代入リスト（タイトル）
lb=[]     #代入リスト（著者）
lc=[]     #代入リスト（出版社）
ld=[]     #代入リスト（タグ）


for a in input1:                    #リスト生成
    try:
        la.extend(list(ti[a]))
    except KeyError:
        pass    
for b in input2:
    try:
        lb.extend(list(aut[b]))
    except KeyError:
        pass
for c in input3:
    try:
        lc.extend(list(pub[c]))
    except:
        pass
for d in input4:
    try:
        ld.extend(list(tag[d]))
    except KeyError:
        pass



if len(la)==0 and len(lb)==0 and len(lc)==0 and len(ld)==0:                                    #検索で一件もヒットしない場合の出力
    print("入力内容: ","タイトル",input1," / 著者",input2," / 版社",input3," / タグ",input4,"\n")
    print("＊Not Found\n　入力ミスがないか確認してください")
    
else:                                                                                          #検索出力
    print("入力内容: ","タイトル",input1," / 著者",input2," / 版社",input3," / タグ",input4,"\n")

    count=0                        #カウンター
              
    ra=set(la)                     #リスト型→セット型変換
    rb=set(lb)
    rc=set(lc)
    rd=set(ld)


    union=ra|rb|rc|rd              #和集合
    listunion=list(union)
    
    for i in listunion:
        count+=1
        print(count,".",str(i))
    print("\n\n検索ヒット数: ", str(len(union)), "件")
    if "みんなのpython" in listunion:
        img_minpy.show("C:\pbl\images\minpy.jpg")