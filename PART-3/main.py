from fastapi  import FastAPI, HTTPException, status, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from schemas import ProductPatch, ProductCreate, ProductResponse, ProductUpdate

app = FastAPI()

#fake database
products = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

#CREATE
@app.get("/products", response_model=ProductResponse,status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    new_product = {
        "id": len(products)+1,
        **product.model_dump()
    }
    products.append(new_product)
    return new_product

#GET ALL (with querry params)
@app.get("products", response_model=list[ProductResponse])
def get_products(
    min_price: float = Query(default=0),
    max_price: float = Query(default=10000),
    in_stock: Optional[bool] = None
):
    result = []
    for product in products:
        if product["price"] < min_price or product["price"] > max_price:
            continue
        if in_stock is not None and product["in_stock"] != in_stock:
            continue
        result.append(product)

        return result
    
#GET ONE
@app.get("/products/{product_id}", response_model=ProductResponse)
def  get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
        
        raise HTTPException(status_code=404, detail="product not  found")

#UPDATE (PUT - FULL REPLACE)
@app.get("/products/{product_id}", response_model= ProductResponse)
def update_product(product_id: int , updated_product: ProductUpdate):
    for product in products:
        if product["id"] ==product_id:
            product.update(updated_product.model_dump())
            return product
        
    raise HTTPException(status_code=404, detail="product not  found")

#PATCH (partial update)
@app.get("products/{product_id}", response_model=ProductResponse)
def patch_product(product_id: int , updated_update: ProductPatch):
      for product in products:
        if product["id"] == product_id:

            update_data = update_product.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                product[key] = value

            return product

      raise HTTPException(status_code=404, detail="Product not found")

#DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted = products.pop(index)
            return {"message": "Deleted", "data": deleted}

    raise HTTPException(status_code=404, detail="Product not found")

