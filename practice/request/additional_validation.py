from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
async def read_item(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results
