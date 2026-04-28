from pydantic import BaseModel, Field
from typing import Optional

#Base schemas (common fields)
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

# For crearting post (input)
class PostCreate(PostBase):
    pass

# For response (output)
class PostResponse(PostBase):
    id: int
