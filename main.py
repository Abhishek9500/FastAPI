'''
Practice question :- (1)

Create a Pydantic model named Student with these fields:
- name: string
- age: integer
- branch: string
- marks: float
Then create a POST /create_student endpoint that accepts a Student object and returns its data.

----------> Solution

from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

Students = []

class Student(BaseModel):
    name:str
    age:int
    branch:str
    marks:float = Field(gt=0)


@app.get("/student")
def get_student():
    return Students

@app.post("/student")
def create_student(student:Student):
    Students.append(student)
    return{
        "message":"Student created successfully",
        "data":student
    }

'''

'''
Practice question :- (2)

Create a ProductResponse model with these fields:
- id: integer
- name: string
- price: float
Then create a GET /products/{product_id} endpoint with response_model=ProductResponse.

'''
from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

Products = []

class Product(BaseModel):
    id:int
    name:str
    cost_price:float=Field(ge=0)
    selling_price:float=Field(ge=0)

class ProductResponse(BaseModel):
    id:int
    name:str
    selling_price:float


@app.post("/products")
def create_products(product:Product):
    Products.append(product)
    return{
        "message":"Product created successfully !",
        "data":product
    }

@app.get("/products/{product_id}",response_model=ProductResponse)
def get_products(product_id:int):
    for product in Products:
        if product.id == product_id:
            return product
    return {
        "error":"Product not found !"
    }
    
