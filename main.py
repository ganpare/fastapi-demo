from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
import json

app = FastAPI()

# テンプレートとスタティックファイルの設定
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# メモリ内のデータストア（実際のアプリケーションではデータベースを使用します）
TASKS = []

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": TASKS}
    )

@app.post("/tasks")
async def create_task(task: str = Form(...)):
    TASKS.append(task)
    return {"message": "タスクが追加されました", "tasks": TASKS}

@app.get("/api/tasks")
async def get_tasks():
    return {"tasks": TASKS}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if 0 <= task_id < len(TASKS):
        TASKS.pop(task_id)
        return {"message": "タスクが削除されました", "tasks": TASKS}
    return {"error": "タスクが見つかりません"}
