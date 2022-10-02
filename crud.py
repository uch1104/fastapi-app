from sqlalchemy.orm import Session

from schemas import UserCreate
import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
    

def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: UserCreate):
    db_user = models.User(user_name=user.user_name , email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id)
    db_user.update({
        models.User.user_name: user.user_name,
        models.User.email: user.email
    })
    db.commit()
    updated_user = db.query(models.User).filter(models.User.id == user_id).first()
    return updated_user


def delete_user(db: Session, user: UserCreate):
    db.delete(user)
    db.commit()
    return {'message': 'success'}
