#!/usr/bin/env python3
"""シンプルなサンプルプログラム"""

import requests
from datetime import datetime


def fetch_data(url: str) -> dict:
    """URLからJSONデータを取得"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"エラー: {e}")
        return {}


def main():
    """メイン処理"""
    print(f"プログラム実行開始: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # JSONPlaceholderのサンプルAPIにアクセス
    data = fetch_data("https://jsonplaceholder.typicode.com/todos/1")
    
    if data:
        print(f"取得されたデータ: {data}")
    else:
        print("データ取得に失敗しました")


if __name__ == "__main__":
    main()
