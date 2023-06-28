from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None