from fastapi import FastAPI,status

app = FastAPI()

@app.post("/user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"User created !"
    }

## Custom Responses

from fastapi.responses import JSONResponse

@app.get("/custom")
def custom_Response():
    return JSONResponse(
        status_code=200,
        content={
            "message":"Custome json respnse",
            "success":True
        }
    )

# HTTPException

from fastapi import HTTPException

users={
    1:{"name":"Abhiehk"},
    2:{"name":"abhi"}
}

@app.get("/user")
def get_user(user_id:int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not Found"
        )
    return users[user_id]

