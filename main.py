from fastapi import FastAPI

app = FastAPI()

# @app.post("/create-user")
# def create_user(name:str,age:int):
#     return{
#         "name":name,
#         "age":age
#     }


# @app.post("/create-user")
# def create_user(user:dict):
#     return{
        
#         "message":"User created !",
#         "data":user
#     }

from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(user:User):
    return{
        "message":"User created !",
        "data":user
    }
