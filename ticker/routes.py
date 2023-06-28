from ticker import app, Item

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_price": item.price}