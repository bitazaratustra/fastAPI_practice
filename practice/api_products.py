from fastapi import FastAPI
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
    return {'Message': f'Product with ID {product_id} not be founded'}
