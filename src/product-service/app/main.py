from http.client import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#mock database
products = []
current_id = 1

class Product():
  id: int
  name: str
  description: str
  price: float

### ENDPOINTS #####
@app.get("/products")
def get_products():
  return products

@app.post("/products")
def create_products(product: Product):
  global current_id
  new_product = {
    "id": current_id,
    "name": product.name,
    "price": product.price,
    "description": product.description
  }
  products.append(new_product)
  current_id += 1
  return product

#GET /products/{id}: Get a specific product by ID.
@app.get("/products/{id}")
def get_product(id: int):
  for product in products:
    if id == product["id"]:
      return product
    raise HTTPException(status_code=404, detail = "Product not found")

#PUT /products/{id}: Update a product.

#DELETE /products/{id}: Delete a product.
