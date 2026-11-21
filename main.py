from fastapi import FastAPI

# LEC 01 =========================================== BASIC STRUCTURE =============================================================
# API Routes
app = FastAPI()

#Home route
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

#About route
@app.get("/about")
def about():
    return {"message": "This is the about page."}

# Users Page
# @app.get("/users")
# def users():
#     return {
#         "users" : ["Mohit", "ayan","arman"]
#     }

# LEC 02 PATH PARAMETER ============================================== ================================================

# Taking specific user Based on Parameters
# 01 DYANAMIC ROUTE

# @app.get("/users/{user_id}")
# def get_users(user_id):
    # return {"users" : user_id}

# 02 TYPE VALIDATION =  DATATYPE INPUT = int , str
# WORK = fetch data by its usre by ID  usrer_id 

# @app.get("/users/{user_id}")
# def get_users(user_id : int):
#     return {"users" : user_id}

# LEC  03 QUERY PARAMETER =====================================================
# QUERY PARAM = /user?name=mohit kind of this 
# used in pagination
# used for searching sorting and filtering used by = insta , amazon etc
# 01 OPTIONAL PARAMETERS = to handle errors

@app.get("/users")
def users(name: str = None): # if name was not there just show null
    return{"Name":name}
# {
#   "Name": null
# }

# 02 DEFAULT VALUE
@app.get("/products")
def users(limit: int = 10): 
    return{"limit": limit}

# 03 Multiple Query parameter
@app.get("/items")
def items(name: str = None, price: int=0):
    return{
        "Name": name,
        "Price":price
    }


