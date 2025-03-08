# データベース設計ドキュメント

## 概要
このアプリケーションでは、PostgreSQLデータベースを使用してタスクを管理しています。

## データベース接続情報
- データベース: PostgreSQL 14
- データベース名: taskdb
- ユーザー名: user
- パスワード: password
- ホスト: db (Docker内部) / localhost (ローカル開発時)
- ポート: 5432

## テーブル構造

### tasks テーブル
タスク情報を管理するメインテーブル

| カラム名    | 型        | 制約        | 説明                    |
|------------|-----------|-------------|------------------------|
| id         | Integer   | Primary Key | タスクの一意識別子       |
| title      | String    | Not Null    | タスクのタイトル        |
| created_at | DateTime  | Not Null    | タスク作成日時          |

## マイグレーション管理
データベースのマイグレーションはAlembicを使用して管理しています。

### マイグレーションの実行方法
```bash
# マイグレーションファイルの作成
docker-compose exec web alembic revision --autogenerate -m "create tasks table"

# マイグレーションの実行
docker-compose exec web alembic upgrade head
```

## アプリケーションでの使用方法
SQLAlchemyを使用してデータベースとのやり取りを行っています。

```python
# タスクの作成
db_task = models.Task(title="新しいタスク")
db.add(db_task)
db.commit()

# タスクの取得
tasks = db.query(models.Task).all()

# タスクの削除
task = db.query(models.Task).filter(models.Task.id == task_id).first()
db.delete(task)
db.commit()
```

## バックアップとリストア
データはDockerボリューム `postgres_data` に永続化されています。必要に応じてバックアップを作成することをお勧めします。

```bash
# バックアップの作成
docker-compose exec db pg_dump -U user taskdb > backup.sql

# リストア
docker-compose exec db psql -U user taskdb < backup.sql
