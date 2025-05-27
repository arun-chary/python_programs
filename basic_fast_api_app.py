
# pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for the request body
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Pydantic model for the response
class ItemOut(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.is_offer:
        item_dict.update({"description": f"{item.name} is on offer!"})
    return item_dict

@app.get("/items/{item_id}", response_model=ItemOut)
async def read_item(item_id: int, q: str | None = None):
    return {"name": f"Item {item_id}", "price": 19.99, "description": f"Details for item {item_id}. Query: {q}"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
