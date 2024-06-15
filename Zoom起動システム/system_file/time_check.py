import schedule as sc
import time
import streamlit as st
from system_file.zoom_fun import zoom_open
def time_function(specified_time,week,URL):
    timeHolder = st.sidebar.empty()
    stop_button =st.sidebar.button("stop")
    if stop_button:
        st.stop()
    if week=="su":
        sc.every().sunday.at(specified_time).do(zoom_open,URL)
    elif week=="ma":
        sc.every().monday.at(specified_time).do(zoom_open,URL)
    elif week=="tu":
        sc.every().tuesday.at(specified_time).do(zoom_open,URL)
    elif week=="we":
        sc.every().wednesday.at(specified_time).do(zoom_open,URL)
    elif week=="th":
        sc.every().thursday.at(specified_time).do(zoom_open,URL)
    elif week=="fr":
        sc.every().friday.at(specified_time).do(zoom_open,URL)
    elif week=="sa":
        sc.every().saturday.at(specified_time).do(zoom_open,URL)
    else:
        st.error("Week is not correct")
        st.stop()


    while True:
        timeHolder.write("実行中")
        sc.run_pending()
        time.sleep(60)  # スケジュールがない場合は1秒待機
