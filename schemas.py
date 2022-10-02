from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str
    email: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True