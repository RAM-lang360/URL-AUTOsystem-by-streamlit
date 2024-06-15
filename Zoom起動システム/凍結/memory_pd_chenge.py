import streamlit as st
import numpy as np
import psutil
import time
def get_memory_usage():
    # 現在のプロセスのメモリ使用量を取得（バイト単位）
    process = psutil.Process()
    memory_info = process.memory_info()
    
    # バイトをメガバイトに変換
    memory_usage_mb = memory_info.rss / (1024 * 1024)
    return memory_usage_mb/100

def pd_chenge(chart,time_list):
    memory = time_list
    data_dict={
        "時間/秒":time_list,
        "メモリ使用量(MB)":memory}
    data_array = np.array(list(data_dict.values()))
    # グラフの描画
    