from fastapi import FastAPI
import asyncio
app = FastAPI()

# Synchronous Programing

# @app.get("/home")
# def home():
#     return {"message": "Welcome to FastAPI"}

# Asynchronous Programing

@app.get("/home")
async def home():
    await asyncio.sleep(2)
    return {"message": "Welcome to FastAPI"}