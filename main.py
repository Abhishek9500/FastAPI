from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import User

app = FastAPI()

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)


# Pydantic request and response models
class UserCreate(BaseModel):
    name: str
    age: int
    email: str


class UserResponse(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

# CREATE USER
@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    new_user = User(**user.model_dump())

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception:
        db.rollback()
        raise

    return {
        "message":"User Created",
        "data":new_user
    }


# GET ALL USERS
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# GET ONE USER
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

# UPDATE USER
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    updated_user: UserCreate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    duplicate = (
        db.query(User)
        .filter(
            User.email == updated_user.email,
            User.id != user_id
        )
        .first()
    )

    if duplicate:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    user.name = updated_user.name
    user.age = updated_user.age
    user.email = updated_user.email

    try:
        db.commit()
        db.refresh(user)
    except Exception:
        db.rollback()
        raise

    return user


# DELETE USER
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()
    return {
        "message":"User deleted !",
        "data":user
    }