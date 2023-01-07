from fastapi import FastAPI
from . import models
from . import schemas
from sqlalchemy import create_engine

app = FastAPI()
SQLALCHAMY_DATABASE_URL = 'sqlite:///database.db:'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={'check_same_thread': False})

models.Base.metadata.create_all(engine)

@app.post('/blogs')
def Blog (Base):
    return
