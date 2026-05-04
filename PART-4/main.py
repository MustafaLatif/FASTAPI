from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# ✅ In-memory DB
products_db = [
    {
        "id": 1,
        "name": "mustafa",
        "age": 21,
        "content": "this is practice session"
    }
]

# ✅ Schema
class Product(BaseModel):
    name: str
    age: int
    content: str = Field(min_length=10, max_length=100)


# ✅ Create
@app.post("/products")
def create_product(product: Product):
    new_product = product.dict()
    new_product["id"] = len(products_db) + 1
    products_db.append(new_product)
    return new_product


# ✅ Get all
@app.get("/products")
def get_products():
    return products_db


# ✅ Get single
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# ✅ Delete
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            products_db.remove(product)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")