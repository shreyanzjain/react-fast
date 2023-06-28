from ticker import app
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ticker.models import Item

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/item/{item_id}", response_class=HTMLResponse)
def read_item(request: Request, item_id: int, item_name: str):
    return templates.TemplateResponse("item.html", 
                                      {"request": request, 
                                       "item_id": item_id, 
                                       "item_name": item_name})

@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_price": item.price}

@app.get("/files/{file_path:path}")
def read_path(file_path: str):
    return {"file_path": file_path}