from pydantic import BaseModel

class User(BaseModel):
    user_name: str
    email: str

    class Config:
        orm_mode = True