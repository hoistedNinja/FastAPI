from typing import Optional
from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(q:Optional[str] = None, skip: int=0,limit: int = 10):
    return{"q":q,"skip":skip,"limit":limit}


# dependency injection of common parameters on two functions read_item and read_users

@app.get("/items/")
async def read_items(commons:dict= Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons:dict=Depends(common_parameters)):
    return commons
