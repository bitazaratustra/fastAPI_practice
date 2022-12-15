from fastapi import FastAPI

app = FastAPI()

@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str, q: str or None = None, short : bool = False):
    item = {'Owner_id': user_id, 'Item_id': item_id}
    if q :
        item.update({'q': q})
    if not short:
        item.update({'Description': 'This is an amazing item thas has a long description'})
    return item
