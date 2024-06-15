import streamlit as st
import pandas as pd
import psutil
import time
import matplotlib.pyplot as plt
import numpy as np

# グローバルでの Pyplot 使用の警告を無効化
st.set_option('deprecation.showPyplotGlobalUse', False)

def get_memory_usage():
    # 現在のプロセスのメモリ使用量を取得（バイト単位）
    process = psutil.Process()
    memory_info = process.memory_info()
    
    # バイトをメガバイトに変換
    memory_usage_mb = memory_info.rss / (1024 * 1024)
    return memory_usage_mb / 100

def pd_chenge(time_list):
    memory = get_memory_usage()
    data_dict = {
        "メモリ使用量(MB)": memory
    }
    
    # 辞書をNumPyの配列に変換
    data_array = np.array(list(data_dict.values()))

    # time_list をNumPyの配列に変換
    time_array = np.array(time_list)

    # Matplotlibを使用してプロット
    fig, ax = plt.subplots()
    ax.plot(time_array, data_array)
    ax.set_xlabel('時間/秒')
    ax.set_ylabel('メモリ使用量(MB)')

    # Streamlitの図に追加
    st.pyplot(fig)

# Streamlitアプリケーションの作成
st.title('メモリ使用量の折れ線グラフ')
time_list = []
i = 0

while True:
    i += 1
    time_list.append(i)
    pd_chenge(time_list)
    time.sleep(1)
