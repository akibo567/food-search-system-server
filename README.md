# グルメ検索システムのバックエンド
このリポジトリはバックエンドのものになります。
フロントエンドのリポジトリはhttps://github.com/akibo567/food-search-system-front
で、フロントとバックエンド両方の起動が必要となります。

また、事前にGeolocation APIとsessionStorageの利用を許可する必要があります。


## 概要
ぐるなびAPIを用いて、現在地周辺の飲食店を検索します。

## 動作環境
Python 3.9.5
pip 22.3.1

## 起動方法(バックエンド)
1. `.env.sample`を`.env`にコピーして、`.env`を編集しぐるなびのAPIキーを設定する
2. `flask run`でアプリが`http://127.0.0.1:5000`に起動する

