from fastapi import FastAPI

app = FastAPI()

# Dynamic Routes 
# @app.get("/users/{user_id}")
# def get_users(user_id):
#     return {"user_id":user_id}


## Dynamic Routes with data types
@app.get("/users/{user_id}")
def get_users(user_id:int):
    return {"user_id":user_id}
