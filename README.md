# FastAPI Demo

このリポジトリは、FastAPIを使ったデモプロジェクトです。以下に概要、セットアップ手順、及び使用方法を記載します。

## 概要

- FastAPI、Docker、PostgreSQL、pgAdminを利用したWebアプリケーションのデモです。
- <code>docker-compose.yml</code> により、アプリケーション（web）、データベース（db）、pgAdminサービスが構成されています。
- pgAdminは、[http://localhost:5050](http://localhost:5050) からアクセス可能です。

## セットアップ

1. Dockerおよびdocker-composeをインストールしてください。
2. リポジトリをクローンまたはダウンロードし、<code>fastapi-demo</code>ディレクトリに移動します。
3. 以下のコマンドを実行して、コンテナをビルド・起動します。

   ```
   docker-compose up --build -d
   ```

## 使用方法

- **Web サービス**: [http://localhost:8000](http://localhost:8000) でアプリケーションが稼働します。
- **pgAdmin**: [http://localhost:5050](http://localhost:5050) でデータベース管理ツールにアクセスできます。
  - pgAdminのデフォルトログイン情報:
    - Email: admin@example.com
    - Password: admin
- **PostgreSQL**: 使用しているデータベースは<code>postgres:14</code>イメージにより構築されています。接続情報は<code>docker-compose.yml</code>にて設定されています。

## 更新内容

- pgAdminの設定を更新し、<code>PGADMIN_CONFIG_ENCRYPTION_KEY</code>および<code>PGADMIN_CONFIG_TIMEOUT</code>を適切に設定しました。
- Dockerコンテナを使って、プロジェクト全体を自動ビルド・起動できる環境が整いました。
- GitHubのリモートリポジトリが作成され、内容が最新の状態でプッシュされています。

## リモートリポジトリ

リモートリポジトリはGitHubに作成され、プロジェクトの最新の内容が反映されています。

## トラブルシューティング

問題が発生した場合は、各Dockerサービスのログを確認してください。必要に応じて、以下のコマンドでコンテナの再構築・再起動を行ってください。

   ```
   docker-compose down && docker-compose up --build -d
   ```

## ライセンス

このプロジェクトはMITライセンスのもとで公開されています.
