import streamlit as st
from system_file.time_check import time_function
def pd_list_M(pd_data):
    name_list=pd_data["Name"]
    return name_list

def pd_json_C(pd_data):
    json_data = pd_data.to_json(orient='records')  # 'records'は行ごとに辞書として格納
    with open(r"C:\Users\eva10\OneDrive\デスクトップ\創作物一覧\Zoom起動システム\test.json", "w") as f:
        f.write(json_data)
        
def zoom_kidou(select_name, pd_data):
    week = pd_data.loc[pd_data["Name"] == select_name, "day of week"].values[0]
    hour=pd_data.loc[pd_data["Name"] == select_name, "hour"].values[0]
    minite=pd_data.loc[pd_data["Name"] == select_name, "minite"].values[0]
    URL=pd_data.loc[pd_data["Name"] == select_name, "URL"].values[0]
    specified_time=(f"{(hour)}:{minite}")
    
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

    time_function(specified_time, week,URL)
