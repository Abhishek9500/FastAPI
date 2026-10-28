from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

def get_message():
    return "Welcome to FastApi"

@app.get("/home")
def home(data:str=Depends(get_message)):
    return {"data":data}

@app.get("/about")
def about(message:str=Depends(get_message)):
    return message


def verify_token(token:str=Header(None)):
    if token != "Abhi1234":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return{
        "user":"Authorized User"
    }

@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return{
        "message":"secure data accessed",
        "user":user
    }


