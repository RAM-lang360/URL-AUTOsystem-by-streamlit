import streamlit as st
import webbrowser as wb
import time 
from system import *
def main():
    schedule_data =init()
    st.title("URL自動実行システム")
    st.write("・タブを選んで編集できます。二桁以下の時刻を入力する際は0を入力した後時刻を入れてください")
    st.text("      ex) 9時の場合 09:00")
    st.write("・曜日を編集できます。語の頭文字2文字を入力してください")
    st.text("      ex)日→su, 月→mo,火→tu,水→we,木→th,金→fr,土→sa")
    edited_df = st.data_editor(schedule_data, num_rows="dynamic")
    save_button=st.button("Save")
    if save_button:
        save_schedule_data(edited_df)

    # サイドバーの選択ボックスにname_listを使用
    st.session_state["name_list"]=pick_up_name()
    selected_class = st.sidebar.selectbox("select class", st.session_state["name_list"])
    zikou_button = st.sidebar.button("zikkou")
    if zikou_button:
        zoom_start(selected_class)

if __name__ == "__main__":
    main()