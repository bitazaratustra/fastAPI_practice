from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/items/1/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items/2/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item




# In this case the query parameter "needy" is mandatory
# of course you can use other types like optional or with
# a opcion suggested
