#===================================== PYDANTIC MODEL ======================================
# DEFINE SCHEMA
# TELLS USER HOW MUCH FIELD IT TAKE 
# PROPER INPUT VALIDATION
# AUTOMATIC ERROR HANDELING
# POST API = DOES NOW RUN IN BROWSER IT RUN IN SWAGGER
# USING CLASS FOR PROPER INPUT FIELD VALIDATION

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Defining Schema
class User(BaseModel):
    name:str
    age:int
    email:str

# POST route
@app.post("/create_user")
def create_user(user:User): # GETTING USER DATA INTO USER
    return{
        "message":"User Created",
        "data":user
    }