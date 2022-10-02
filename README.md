# 開発環境構築

## ライブラリのインストール
```
pip install -r requirements.txt
```

## データベース作成
ローカルの Mysql に db.py に記載されている情報に合わせてデータベースを作成する
```
USER = 'user'
PASSWORD = 'password'
SERVER = '127.0.0.1'
PORT = '3306'
DB = 'fastapi_db'
```

## マイグレーション
```
alembic upgrade head 
```

## サーバの起動
```
uvicorn main:app --reload 
```