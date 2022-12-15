from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]

@app.get('/items/')
async def read_items(skip: int = 0, limit: int =10):
    return fake_items_db[skip:skip + limit]


@app.get('/items/{item_id}')
async def read_items(item_id : str, q : str or None = None):
    if q:
        return {'Item_id': item_id, 'q' : q}
    return {'Item_id': item_id}
