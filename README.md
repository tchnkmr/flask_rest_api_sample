# Flask Rest API Sample

Flask,Flask_SQLAlchemyを使用したREST APIのサンプルです。

## API一覧

|処理|メソッド|エンドポイント|
|:---|:------|:------------|
|ユーザ一覧取得|GET|/api/users|
|ユーザ登録|POST|/api/users|
|ユーザ取得|GET|/api/users/:id|
|ユーザ更新|PUT|/api/users/:id|
|ユーザ削除|DELETE|/api/users/:id|

## 設定方法

1. 本プロジェクトのclone

  `git clone https://github.com/tchnkmr/flask_rest_api_sample.git`

1. DBのインストール

  お好きなのなんでも

1. テーブル作成

  sql/create_table.sqlを実行してテーブル作成

1. モジュールインストール

  使用するDBドライバーをrequirements.txtに追加すること

  `pip install -r requirments.txt`

1. DBの接続情報設定

  config.cfg の SQLALCHEMY_DATABASE_URI に追加

1. 起動

  `python run.py`

1. 各エンドポイントへのアクセス

  client.py に書くエンドポイントへのアクセスを行うメソッドがあるのでそれを、それを使用してアクセスする
