from fastapi import FastAPI
from database import engine
import models

#============= create table ==============
models.Base.metadata.create_all(bind=engine)

app = FastAPI

# route
@app.get("/")
def home():
    return{
        "message":"Blog API Started"
    }