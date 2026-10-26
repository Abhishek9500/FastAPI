from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name:str=None):
    return {
        "name":name,
    }

## default query
@app.get("/products")
def get_products(limit:int = 10):
    return {"products":limit}

## multiple query parameter
@app.get("/items")
def get_items(name:str=None,price:int=0):
    return{
        "name":name,
        "price":price
    }