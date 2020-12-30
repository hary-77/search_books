# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:09:54 2020

@author: 森下　源太
"""





ti={("みんな"):{"みんなのpython"},("python"):{"みんなのpython","Python本"}}
aut={("柴田淳"):{"みんなのpython"}}
pub={("SBクリエイティブ"):{"みんなのpython"}}
tag={("Ruby"):{"Rubyの本"},("python"):{"みんなのpython","Python本"},("スクラム"):{"スクラムマスターザブック"}}

input1=["a"]    #データ入力（タイトル）
input2=["a"]    #データ入力（著者）
input3=["a"]    #データ入力（出版社）
input4=["R"]    #データ入力（タグ）


la=[]
lb=[]
lc=[]
ld=[]


for a in input1:
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



if len(la)==0 and len(lb)==0 and len(lc)==0 and len(ld)==0:
    print("Not Found\n入力ミスがないか確認してください")
    
else:            
    ra=set(la)
    rb=set(lb)
    rc=set(lc)
    rd=set(ld)


    union=ra|rb|rc|rd

    for i in union:
        print(i)
    
