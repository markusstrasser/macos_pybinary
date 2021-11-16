import uvicorn
import multiprocessing
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    multiprocessing.freeze_support() 
    #multiprocessing freeze to not recursively run the server in the build (Adress already in use).
    uvicorn.run("main:app", host="0.0.0.0", port=44000, reload=True)
