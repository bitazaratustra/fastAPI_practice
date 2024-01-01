from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt

app = FastAPI()
oauth = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_auth_db = {
        "bitabalda": {
        'username': 'bitabalda',
        'full_name': 'Bita Baldasseroni',
        'email': 'bitabalda@ec.com',
        'disabled': False,
        "password": "12345"
    },
         "luisesteban": {
        'username': 'luisesteban',
        'full_name': 'Luis Esteban',
        'email': 'luisesteban@ec.com',
        'disabled': False,
        "password": "123"
    },
          "Esteban": {
        'username': 'esteban',
        'full_name': 'Esteban Balda',
        'email': 'ebita@ec.com',
        'disabled': False,
        "password": "123"
    }
}



def search_user_db(username:str):
    if username in users_auth_db:
        return UserDB(**users_auth_db[username])

@app.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_auth_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return {"acces_token": user.username, "token_type": "bearer"}
