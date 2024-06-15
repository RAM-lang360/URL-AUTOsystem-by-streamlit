import webbrowser as wb
import streamlit as st
def zoom_open(URL):
    try:
        print("実行")
        wb.open(URL)
    except:
        st.error("URLが正しくありません")

