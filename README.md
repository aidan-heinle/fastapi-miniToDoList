# fastapi-miniToDoList
Simple FastAPI for managing tasks. This is a learner project and will be expanded on more!

# Features
- Create tasks (POST /tasks)
- View all tasks (GET /tasks)
- View a single task by ID (GET /tasks/{id})
- Delete tasks (DELETE /tasks/{id})

  # Installation
  - Install dependencies: "pip install fastapi uvicorn"

  # Running the API
  - uvicorn app:app --reload
    > the API will run at http://127.0.0.1:8000
    > Interactive API documentation available at http://127.0.0.1:8000/docs
