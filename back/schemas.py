from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    password: str
    is_active: bool

class Movie(BaseModel):
    id: int
    tmdb_id: int
    user_id: int


    class Config:
        form_attributes = True