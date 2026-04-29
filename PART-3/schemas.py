from pydantic import BaseModel, Field
from typing import Optional

#Base Schema
class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=5)
    price: float = Field(gt=0)
    in_stock: bool = True

#Input Schema (POST)
class ProductCreate(ProductBase):
    pass

#Update Schema (PUT - full updates)
class ProductUpdate(BaseModel):
     name: str = Field(min_length=3, max_length=100)
     description: str = Field(min_length=5)
     price: float = Field(gt=0)
     in_stock: bool

#Partial update (PATCH)
class ProductPatch(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, min_length=5)
    price: Optional[float] = Field(default=None, gt=0)
    in_stock: Optional[bool] = None

#Output Schema (Response)
class ProductResponse(ProductBase):
    id: int 