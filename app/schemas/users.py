from pydantic import BaseModel

class UserCreate(BaseModel):
    username : str

class UserResponse(BaseModel):
    id : int
    username : str

class UserUpdate(BaseModel):
    username : str