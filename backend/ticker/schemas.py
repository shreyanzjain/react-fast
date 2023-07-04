from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class Stock(BaseModel):
    instrument: str
    date: datetime
    close: float
    high: float
    open: float
    low: float
    volume: int

    class Config:
        orm_mode = True