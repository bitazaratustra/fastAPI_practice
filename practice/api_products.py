from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4 as uuid


class Product(BaseModel):
    id : Optional[str]
    name : str
    buy_price : float
    sell_price : float
    provider : str

app = FastAPI()

products = []

@app.get('/')
def index():
    return {'Message': 'Welcome to Products API'}


@app.get('/product')
def get_product():
    return products

@app.post('/product')
def create_product(product: Product):
    product.id = str(uuid())
    products.append(product)
    return {'Message': 'Product succefully created'}


@app.get('/product/{product_id}')
def get_product_by_id(product_id: str):
    result = list(filter(lambda p: p.id == product_id, products))
    if len(result):
        return result[0]
    raise HTTPException(status_code=404, detail=f'The product with the ID {product_id} was not found')
