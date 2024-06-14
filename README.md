# URL-auto-system
## 概要
このプログラムはstreamlitによるローカルホストアプリケーションです。jsonファイルの保存領域にURL、実行させたい時間を入力し、その情報をもとに任意の時間にURLを開くものとなっています。
## 開発環境
- OS Microsoft Windows 10 Home
- Python 3.12.0

## 設計
- display.py
  - アプリケーションの表示とスクリプトの実行
- system.py
    - pandas,webbrowser,scheduleなどのモジュールを使用
- run.py
    - ローカルホストを開くためのコマンドを実行するスクリプト
  
## 