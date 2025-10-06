from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


tasks = []

# Create a new task
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Task added!", "task": task}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# Get a single task by id
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Task deleted!"}
