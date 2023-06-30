from ticker import app
from fastapi import Request, Query
from typing import Union, List
from typing_extensions import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ticker.models import Item
from fastapi.staticfiles import StaticFiles


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/item/{list_id}", response_class=HTMLResponse)
def read_item(request: Request, list_id: int):
    items = [
        {
            "id": 1,
            "name": "shreyans"
        },
        {
            "id": 2,
            "name": "kashish"
        }
    ]
    return templates.TemplateResponse("item.html", {"request": request, "items": items,
                                                    "list_id": list_id})

@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict() }

@app.get("/files/{file_path:path}")
def read_path(file_path: str):
    return {"file_path": file_path}

@app.get("/multi_query_params")
def multi_params(q: Annotated[Union[List[str], None], Query()] = None):
    return {"q": q}