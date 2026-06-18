# Cara jalankan:
#    uvicorn main:app --reload
# Buka http://127.0.0.1:8000
# Docs otomatis: http://127.0.0.1:8000/docs
# Coba GET /items, POST /items, dll pake docs atau curl
#
# Contoh curl:
#   curl http://127.0.0.1:8000/items
#   curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"nama":"Monitor","harga":3000}'

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# data dummy (nanti ganti pake database beneran)
items = {
    1: {"nama": "Laptop", "harga": 15000},
    2: {"nama": "Mouse", "harga": 200},
    3: {"nama": "Keyboard", "harga": 500},
}


# 1. GET — ambil data

@app.get("/")
def root():
    return {"message": "Hello FastAPI!"}


@app.get("/items")
def get_all_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan")
    return {"id": item_id, **items[item_id]}


@app.get("/items/{item_id}/nama")
def get_item_name(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan")
    return {"nama": items[item_id]["nama"]}


# 2. Query parameter — filter / search

@app.get("/search")
def search_items(q: str = Query(None, min_length=1), min_harga: Optional[int] = None):
    hasil = {}
    for id_, item in items.items():
        if q and q.lower() not in item["nama"].lower():
            continue
        if min_harga and item["harga"] < min_harga:
            continue
        hasil[id_] = item
    return hasil


# 3. Request body pake Pydantic

class ItemCreate(BaseModel):
    nama: str
    harga: int
    deskripsi: Optional[str] = None


class ItemUpdate(BaseModel):
    nama: Optional[str] = None
    harga: Optional[int] = None


# 4. POST — bikin data baru

@app.post("/items")
def create_item(item: ItemCreate):
    new_id = max(items.keys()) + 1 if items else 1
    items[new_id] = item.model_dump()
    return {"id": new_id, **item.model_dump()}


# 5. PUT — update data

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan")

    update_data = item.model_dump(exclude_unset=True)
    items[item_id].update(update_data)
    return {"id": item_id, **items[item_id]}


# 6. DELETE — hapus data

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan")
    items.pop(item_id)
    return {"message": f"Item {item_id} berhasil dihapus"}


# 7. Response model — kontrol output

class ItemResponse(BaseModel):
    id: int
    nama: str
    harga: int


@app.get("/items-typed", response_model=list[ItemResponse])
def get_items_typed():
    return [{"id": id_, **data} for id_, data in items.items()]
