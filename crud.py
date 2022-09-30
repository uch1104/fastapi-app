from sqlalchemy.orm import Session

from schemas import User
import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
    

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: User):
    db_user = models.User(user_name=user.user_name , email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, request: User):
    user = db.query(models.User).filter(models.User.id == user_id)
    user.update({
        models.User.user_name: request.user_name,
        models.User.email: request.email
    })
    db.commit()
    updated_user = db.query(models.User).filter(models.User.id == user_id).first()
    print('aaa')
    return updated_user


def delete_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id)
    user.delete()
    db.commit()
    return {'message': 'success'}
