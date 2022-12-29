from typing import Union

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(default=None, title="The ID of the item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results



# Multple body parameters

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@app.put("/items/multiple/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


@app.put("/items/importance/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body(default=None)):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.put("/items/multiple_bodies_params{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(default=1, gt=0),
    q: Union[str, None] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
