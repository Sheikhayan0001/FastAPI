# =============================================== CRUD OPERATION ==================================================
# CREATE API
# READ API
# UPDATE API
# DELETE API

# EXAMPLE = TODO API

from  fastapi import FastAPI
from pydantic_models import BaseModel

app = FastAPI()

todos = []

#====================================== created base ( SHEMA )  OF DATA ===============================================================
class Todo(BaseModel):
    id:int
    title:str
    completed:bool

#=========================================  CREATE API ======================================================================
# ROUTE

# saving data
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"TODO added","data":todo}

#========================================== READ API =========================================================================
# reading data
@app.get("/todos")
def get_todos():
    return todos

#=========================================== READ PERTICULAR ID ===========================================================
# for single data by path param
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos :
        if todo.id == todo_id:
            return todo
    return {"error":"Todo not found"}

#========================================= UPDATE API ===========================================================
# based on id 
@app.put("/todo/{todo_id}")
def update_todo(todo_id: int,update_todo): # replace 
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return {
                "message":"Data Updated",
                "data":update_todo
                }
    return {"eroor":"todo not found"}

#========================================== DELETE API ================================================================
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index , todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {
                "message":"Data Deleted"
            }
    return {"eroor":"todo not found"}

# INTERVIEW QUESTION
# All things we have done in temp memory not in real Database 

# Q1 what is crud operation ?
# Q2 Diff btw Get , Post , put ,Patch = Partial data update ?

