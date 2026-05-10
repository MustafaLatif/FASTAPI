from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    username : str 
    email : str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = {
        'from_attributes': True
    }

class PostCreate(BaseModel):
        title: str
        content: str
        user_id: str

class PostUpdate(BaseModel):
     title:str
     content: str
     user_id: int

class PostResponse(BaseModel):
         id: int
         title: str
         content: str
         created_at: datetime
         user_id: int

         model_config={
               "from_attributes" : True
         }
