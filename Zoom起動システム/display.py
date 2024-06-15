import streamlit as st
from system_file.change_pd import change_pd
from system_file.display_system import pd_list_M,pd_json_C,zoom_kidou
import webbrowser as wb
def main():
    def opens():
        wb.open("https://google.com/")
    testbutton=st.button("Open")
    if testbutton:
        opens()
    pd_data =change_pd()
    st.title("URL自動実行システム")
    st.write("時刻とURLを設定して自動でサイトを開くシステムです")
    st.header("要素表")
    st.write("タブを選んで編集できます。二桁以下の時刻を入力する際は0を入力した後時刻を入れてください")
    st.write("ex) 9時の場合 09:00")
    st.write("曜日を編集できます。語の頭文字2文字を入力してください")
    st.write("ex)日→su, 月→mo,火→tu,水→we,木→th,金→fr,土→sa")
    edited_df = st.data_editor(pd_data, num_rows="dynamic")
    st.session_state["name_list"]=pd_list_M(edited_df)
    save_button=st.button("Save")
    if save_button:
        pd_json_C(edited_df)

    # サイドバーの選択ボックスにname_listを使用
    selected_class = st.sidebar.selectbox("select class", st.session_state["name_list"])
    zikou_button = st.sidebar.button("zikkou")
    if zikou_button:
        zoom_kidou(selected_class,pd_data)

if __name__ == "__main__":
    main()