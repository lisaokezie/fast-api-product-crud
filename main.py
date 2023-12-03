from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

product_db = {}

class Category(Enum):
    ELECTRONICS = 1
    FASHION = 2
    HOME_APPLIANCES = 3
    SPORTS = 4
    MEDIA = 5
    HEALTH = 6
    OUTDOOR = 7
    GROCERIES = 8

class Product(BaseModel):
    product_id: int = None
    name: str
    description: str
    price: float
    category: Category 

@app.get("/")
def read_root():
    return {"response": "welcome to product API"}

# List all products
@app.get("/product", response_model=list[Product])
def get_products():
    return list(product_db.values())

# Get product by id
@app.get("/product/{product_id}", response_model=Product)
def get_product(product_id: int):
    if product_id not in product_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_db[product_id]

# Create product
@app.post("/product", response_model=Product)
def create_product(product: Product):
    product_id = len(product_db) + 1
    product.product_id = product_id
    product_db[product_id] = product
    print(product_db)
    return product

# Updates product with the given id
@app.put("/product/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    if product_id not in product_db:
        raise HTTPException(status_code=404, detail="Product not found")
    product.product_id = product_id
    product_db[product_id] = product
    print(product_db)
    return product_db[product_id]

# Deletes the product with the given id
@app.delete("/product/{product_id}", response_model=bool)
def delete_product(product_id: int):
    if product_id not in product_db:
        raise HTTPException(status_code=404, detail="Product not found")
    product_db.pop(product_id)
    return True
    