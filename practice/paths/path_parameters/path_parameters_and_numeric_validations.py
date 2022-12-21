from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'File Path': file_path}


from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
