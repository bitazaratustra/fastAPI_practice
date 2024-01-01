from typing import Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix='/products',
                   tags=['Products'],
                   responses={404: {"message": "Not found"} })

products_list = ['producto1', 'producto2', 'producto3']

@router.get('/')
async def products():
    return products_list


@router.get('/{id}')
async def products(id:int):
    return products_list[id]
