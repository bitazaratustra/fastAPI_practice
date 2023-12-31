from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

#Creacion de una app con FastApi
app = FastAPI()

# Entidad users
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

class UserUpdate(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    age: Optional[int]

users_db = [User(id=1, name="Bita",surname='Balda', email='www.google.com', age=  37),
            User(id=2,name="Perro",surname='Alvarelo', email='www.perro.com', age=  31),
            User(id=3, name="Gato",surname='Gaudio', email='www.gato.com', age=  26),
            User(id=4, name="Paloma",surname='Delmar', email='www.paloma.com', age=  32)]

@app.get('/usersjson')
async def usersjson():
    return [{ "name" : "Bita", 'surname': 'Balda', 'email': 'balda@ex.com', 'age': 37},
            { "name" : "Perro", 'surname': 'Alvarelo', 'email': 'perro@ex.com', 'age': 31},
            { "name" : "Gato", 'surname': 'Gaudio', 'email': 'gato@ex.com','age': 26},
            { "name" : "Paloma", 'surname': 'Delmar', 'email': 'paloma@ex.com','age': 32}]

@app.get('/usersclass')
async def usersclass():
    return [User(name="Bita",surname='Balda', email='www.google.com', age=  37),
            User(name="Perro",surname='Alvarelo', email='www.perro.com', age=  31),
            User(name="Gato",surname='Gaudio', email='www.gato.com', age=  26),
            User(name="Paloma",surname='Delmar', email='www.paloma.com', age=  32)]

@app.get('/users')
async def user():
    return users_db


@app.get('/user/{id}',
         status_code=status.HTTP_302_FOUND)
async def user(id: int):
    return search_user(id)


@app.get('/user/',
          status_code=status.HTTP_302_FOUND)
async def user(id: int):
    return search_user(id)


@app.post('/user/',
           status_code=status.HTTP_201_CREATED,
           response_model=User)

async def user(user: User):
    user_db = search_user(user.id)
    if  user_db:
        raise HTTPException(status_code=status.HTTP_226_IM_USED,
                            detail=f'El Usuario {user.id} ya existe.')
    users_db.append(user)
    return user


@app.put('/user/',
          status_code=status.HTTP_200_OK)
async def user(user: UserUpdate):
    user_db = search_user(user.id)
    if isinstance(user, dict)==False:
        user = user.__dict__
    for key, value in user.items():
        if value is not None:
            setattr(user_db, key, value)
    return user_db


@app.delete('/user/{id}',
            status_code=status.HTTP_410_GONE)
async def user(id: int):
    user_db = search_user(id)
    users_db.remove(user_db)


def search_user(id:int):
    users = filter(lambda user: user.id == id, users_db)
    try:
        return list(users)[0]
    except:
        return
