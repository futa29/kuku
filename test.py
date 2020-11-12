import tkinter as tk
from tkinter import messagebox
#import winsound
import random as ra

#占いリスト
uranai_list = ["大吉","中吉","吉","凶"]

#最初の画面
def base_view():

    #占いボタンが押された時、最初の画面を消し、次の画面を生成
    def ura_button():
        base.destroy()
        next_view()
        
    #表示
    base = tk.Tk()
    base.geometry("310x300")
    base.title("占いアプリ")
    input_label = tk.Label(base,text="★占いアプリ★")
    input_label.place(x=110, y=100)

    #ボタン
    button = tk.Button(base,text=" 占 う",command=ura_button)
    button.place(x=120, y=160)
    base.mainloop()

#占い結果画面
def next_view():

    #メッセージボックスを呼び出す
    def message():
        boolean = tk.messagebox.askyesno("確認","トップ画面に戻りますか？")
        #はいを押されると今の画面を消しつつ、トップ画面に戻る　いいえは何もしない
        if boolean == True:
            next.destroy()
            base_view()
        else:
            pass

    #チョイスで占いリストから、ランダムで値を取得する
    ura = ra.choice(uranai_list)

    #大吉なら高いビープ音、凶なら低いビープ音を鳴らす
    if ura == "大吉":
        winsound.Beep(2500,500)
    elif ura == "凶":
        winsound.Beep(400,500)
    


    #表示
    next = tk.Tk()
    next.geometry("300x300")
    next.title("結果画面")
    input_label = tk.Label(next,text=ura,font=("",20))
    input_label.place(x=130, y=100)

    #ボタン
    #メッセージボックスを呼び出す
    button = tk.Button(next,text="戻る",command=message)
    button.place(x=120, y=160)
    next.mainloop()



