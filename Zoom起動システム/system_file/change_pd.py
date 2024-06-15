import pandas as pd
import json
# CSVファイルの読み込み(pandasを返す)
def change_pd():
    with open(r'C:\Users\eva10\OneDrive\デスクトップ\創作物一覧\Zoom起動システム\test.json', 'r', encoding='utf-8') as file:
        reader = json.load(file)
    pd_data = pd.DataFrame(reader)
    json_data = pd_data.to_json(orient='records')  # 'records'は行ごとに辞書として格納
    print(json_data)
    return pd_data
# CSVファイルへの書き込み
