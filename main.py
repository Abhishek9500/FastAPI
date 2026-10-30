from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed origins (front-end url)

origins=[
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #allowed frontend,
    allow_credentials = True,
    allow_methods = ["*"], # GET,PUT,POST,DELETE
    allow_headers = ["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS ENABLE API"
    }