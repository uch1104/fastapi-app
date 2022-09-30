from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255), index=True)
    email = Column(String(255), index=True)
