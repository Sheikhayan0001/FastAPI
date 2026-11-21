#======================================= REQUEST BODY ========================================
#USED: user input data ---> send to backend
# sign up , form submit
from  fastapi import  FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic Validation
class User(BaseModel):
    name:str
    age:int

#post means sending data to other
@app.post("/create-user")
# now what we get from request body
# def create_user(name:str,age:int):
#     return{
#         "name":name,
#         "age":age
#     }

# realife scenerio we used int this way
# IN DICTIONARY NO ERROR HANDELING IS THERE WE CAN PERFORM MANUALLY
# NO PROPER STRUCTURE
# USE JSON FORMATE 
# def create_user(user:dict):
#     return{
#         "message":"user created",
#         "data":user
#     }

# 02 Using Pydantic to validate data is correct or not
# Auto validation
# Iput data in structure way
def create_user(user:User):
    return{
        "message":"user created",
        "data":user
    }
