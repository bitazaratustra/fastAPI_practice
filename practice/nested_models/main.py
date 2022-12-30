from typing import List, Union, Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list = []


# Use "set" to create an unique class element item

class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
