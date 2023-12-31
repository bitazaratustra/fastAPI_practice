from fastapi import FastAPI

#Creacion de una app con FastApi
app = FastAPI()

@app.get('/')
def read_root():
    web_repo="https://github.com/bitazaratustra/fastAPI_practice"
    return {f'Bienvenido!!!  Para mas información : {web_repo}'}
