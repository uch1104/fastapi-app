from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from db import Base, SessionLocal, engine
from schemas import User

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/user/list", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/user/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.put("/user/{user_id}")
def update_user(user_id: int, request: User, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, request)


@app.delete("/user/{user_id}")
def delete_article(id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, id)
