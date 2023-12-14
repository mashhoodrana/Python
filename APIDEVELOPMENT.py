from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

@app.get("/")
def root():
    response = {"Hello World"}
    return response

if __name__ == "__main__":
    uvicorn.run(app)





# In-memory task storage (replace with a database in a real-world scenario)
tasks_db = []

class Task(BaseModel):
    title: str
    description: str
    due_date: Optional[str] = None

@app.post("/tasks/create", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

@app.get("/tasks/all", response_model=List[Task])
def get_all_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.put("/tasks/update/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db[task_id] = updated_task
    return updated_task

@app.delete("/tasks/delete/{task_id}", response_model=dict)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    
    deleted_task = tasks_db.pop(task_id)
    return {"message": "Task deleted successfully", "deleted_task": deleted_task}


if __name__ == "__main__":
    uvicorn.run(app)
    