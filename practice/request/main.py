from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    description : Union [str, None] = None
    price : float
    tax : Union[float, None] = None

app = FastAPI()

@app.post('/items/')
async def create_item(item : Item):
    item_dict = item.dict()
    if item.price :
            price_with_task = item.price + item.tax
            item_dict.update({'Price with task': price_with_task})
            return item_dict
