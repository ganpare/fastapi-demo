from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
import json

from app.database import get_db, engine
from app import models

# データベーステーブルの作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# テンプレートとスタティックファイルの設定
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": [task.title for task in tasks]}
    )

@app.post("/tasks")
async def create_task(task: str = Form(...), db: Session = Depends(get_db)):
    db_task = models.Task(title=task)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    tasks = db.query(models.Task).all()
    return {"message": "タスクが追加されました", "tasks": [task.title for task in tasks]}

@app.get("/api/tasks")
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return {"tasks": [task.title for task in tasks]}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="タスクが見つかりません")
    db.delete(task)
    db.commit()
    tasks = db.query(models.Task).all()
    return {"message": "タスクが削除されました", "tasks": [task.title for task in tasks]}
