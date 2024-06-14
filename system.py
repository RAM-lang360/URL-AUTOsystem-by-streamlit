import pandas as pd
import json
import streamlit as st
import schedule as sc
import webbrowser as wb
import time

#jsonファイルの読み込み、書き出し
#pandasファイルに変換
def init():
    with open(r"data.json","r",encoding="UTF-8") as file:
        reader = json.load(file)
    sc_data=pd.DataFrame(reader)
    return sc_data
#ドロップダウンメニュー用
def pick_up_name():
    sc_data=init()
    name_list=sc_data["Name"]
    return name_list
#スケジュールデータの保存
def save_schedule_data(new_schedule_data):
    json_data = new_schedule_data.to_json(orient='records')  # 'records'は行ごとに辞書として格納
    with open(r"data.json", "w") as file:
            file.write(json_data)


#URL自動起動
#URLを起動
def open_url(url):
    try:
        print("実行")
        wb.open(url)
    except:
        st.error("URLが正しくありません")
#pdから特定の情報を取得
def pick_up_infromation(name):
    week_list = ["su","mo","tu","we","th","fr","sa"]
    sc_data=init()
    week=sc_data.loc[sc_data["Name"] ==name, "day of week"].values[0]
    hour=sc_data.loc[sc_data["Name"] ==name, "hour"].values[0]
    minite=sc_data.loc[sc_data["Name"] ==name, "minite"].values[0]
    url=sc_data.loc[sc_data["Name"] == name,"URL"].values[0]
    
    if len(hour)<2:
        st.error("hour must be two figures exm(9->09)")
        st.stop()
    elif int(hour)<0 or int(hour)>24:
        st.error("hour must be enter 00~24")
        st.stop()
    if len(minite)<2:
        st.error("minite must be two figures exm(9->09)")
        st.stop()
    elif int(minite)<0 or int(minite)>59:
        st.error("minite must be enter 00~24")
        st.stop()
    if week not in week_list:
        st.error('week most be "su","mo","tu","we","th","fr","sa"')
        st.stop()
    #schedule関数の方に合わせるよう成形
    sp_time=(f"{(hour)}:{minite}")
    return week,sp_time,url

#特定の時間に処理を実行
def time_fuction(week,sp_time,url):
    if week=="su":
        sc.every().sunday.at(sp_time).do(open_url,url)
    elif week=="ma":
        sc.every().monday.at(sp_time).do(open_url,url)
    elif week=="tu":
        sc.every().tuesday.at(sp_time).do(open_url,url)
    elif week=="we":
        sc.every().wednesday.at(sp_time).do(open_url,url)
    elif week=="th":
        sc.every().thursday.at(sp_time).do(open_url,url)
    elif week=="fr":
        sc.every().friday.at(sp_time).do(open_url,url)
    elif week=="sa":
        sc.every().saturday.at(sp_time).do(open_url,url)
    else:
        st.error("Week is not correct")
        st.stop()
    while True:
        sc.run_pending()
        time.sleep(60)
#Zoom起動
def zoom_start(name):
    week,sp_time,url=pick_up_infromation(name)
    time_fuction(week,sp_time,url)

