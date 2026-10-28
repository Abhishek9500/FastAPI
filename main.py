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
Practice question :- (2)
