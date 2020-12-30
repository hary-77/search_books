# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:50:18 2020

@author: 森下　源太
"""


data={"Ruby":"『すごいぞRuby』","python":"『みんなのpython』\n『まるわかりPython』\n『たのしいpython』","スクラム":"『スクラムマスターザブック』",
     "柴田淳":"『みんなのpython』"}


# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox




# 関数resultの定義
def result():
    messagebox.showinfo("検索","お探しの本は\n" + data[entry.get()] + "\nです。")
    entry.delete(0,tk.END)
    
# rootフレームの設定
root = tk.Tk()
root.title("書籍検索")
root.geometry("300x200")

# フレームの作成と設置
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

# 各種ウィジェットの作成
label = ttk.Label(frame, text="キーワードを入力してください：")
entry = ttk.Entry(frame)
button_execute = ttk.Button(frame, text="検索", command=result)

# 各種ウィジェットの設置
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button_execute.grid(row=1, column=1)

# Entryウィジェットへ文字列のセット(sample)
entry.insert(tk.END,"python")

root.mainloop()