from fastapi import FastAPI

app = FastAPI()

# Home Route

@app.get("/")
def home():
    return {"message":"Welcome to Home Route"}


## About route

@app.get("/about")

def about():
    return {"message":"this is about route"}

# User Route

@app.get("/users")

def users():
    return {
        "users":["mohit","rohit","Amit"]
    }