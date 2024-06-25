from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int
    user_name: str
    last_name: str
    email: EmailStr = Field(max_length = 128)


class UserIn(BaseModel):
    user_name: str
    last_name: str
    email: EmailStr = Field(max_length = 128)
    password: str = Field(min_length = 6)