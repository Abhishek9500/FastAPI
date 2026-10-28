from fastapi import FastAPI,Request

app = FastAPI()

@app.middleware("http")
async def log_request(request:Request,call_next):
    print("method:",request.method)

    print("URL:",request.url)

    response = await call_next(request)

    print("status code",response.status_code)

    return response

@app.get("/")
def home():
    return{
        "message":"Hello world"
    }