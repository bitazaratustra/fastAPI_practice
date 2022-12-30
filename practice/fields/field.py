from typing import Union

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item (BaseModel):
    name : str
    description : Union[str, None] = Field (
        default = None, title="The description of the item", max_length=300
    )
    price : float = Field(gt=0, description="The price must be grater than zero")
    tax : Union [float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embded=False, default=None)):
    results = {'item_id': item_id, 'item': item}
    return results