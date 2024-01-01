from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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

def search_user(username:str):
    if username in users_auth_db:
        return User(**users_auth_db[username])

async def current_user(token: str = Depends(oauth)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Credenciales no autorizadas',
                            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario Inactivo')
    return user

@app.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_auth_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return {"acces_token": user.username, "token_type": "bearer"}

@app.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user
