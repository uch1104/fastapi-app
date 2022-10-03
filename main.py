from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from db import SessionLocal
from schemas import UserCreate, UserResponse

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 特定のユーザーの情報取得
@app.get("/user/{user_id}", response_model=UserResponse)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# すべてのユーザーの情報取得
@app.get("/user/list/", response_model=list[UserResponse])
def fetch_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


# 新しいユーザーの登録
@app.post("/user/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# ユーザー情報の更新
@app.put("/user/{user_id}")
def update_user(user_id: int, request: UserCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, user_id, request)


# ユーザーの削除
@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db, user)
