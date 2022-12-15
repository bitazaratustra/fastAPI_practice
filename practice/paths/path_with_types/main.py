from fastapi import FastAPI

app= FastAPI()

@app.get('/items/{item_id}')
async def read_items(item_id: int):
    return {'item': item_id}
