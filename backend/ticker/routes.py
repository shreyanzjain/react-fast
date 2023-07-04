from ticker import app, models
from fastapi import Request, Query, Depends, UploadFile, HTTPException
from typing import Union, List
from typing_extensions import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from ticker import models, schemas
from sqlalchemy.orm import Session
from ticker.database import SessionLocal
import pandas as pd

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post('/data/upload')
def upload_form(file: Union[UploadFile, None] = None, db: Session = Depends(get_db)):
    try:
        df = pd.read_csv(file.file)
    except:
        raise HTTPException(status_code=415, detail='Media error')
    else:
        new_row = schemas.Stock
        for _, row in df.iterrows():
            new_row = schemas.Stock(instrument=row["instrument"],
                                    date=row["datetime"],
                                    close=row["close"],
                                    high=row["high"],
                                    low=row["low"],
                                    open=row["open"],
                                    volume=row["volume"])
            
            new_row_model = models.Stock(**new_row.dict())
            # if row already exists
            if db.query(models.Stock).filter(models.Stock.date == new_row_model.date).first() != None:
                pass
            else:
                db.add(new_row_model)
                db.commit()
                db.refresh(new_row_model)
        return new_row
    
@app.get('/data/all', response_model=List[schemas.Stock])
def get_data(db: Session = Depends(get_db), skip: int = 0, limit: int = 11, page: int = 0):
    return db.query(models.Stock).offset(skip + (15 * page)).limit(limit).all()