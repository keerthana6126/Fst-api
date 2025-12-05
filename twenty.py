from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


class Status(str,Enum):
    DONE='done'
    NOT_DONE = 'not_done'

class ItemInput(BaseModel):
    item : str

app = FastAPI()


database = []

@app.post("/add_item")
def todo_item_input(item_input:ItemInput):
    if  len(database) == 0:
        id = 1
    else :
        latest_item = database[-1]
        id = latest_item["id"] + 1
    current_item  = {"id" : id , "item" : item_input.item, "status": Status.NOT_DONE }
    database.append(current_item)
    return database


    

@app.put('/edit_status/')
def edit_status(item_id:int):
    for item_json in database:
        if item_json["id"]==item_id:
            item_json["status"] = Status.DONE
    return database

   

@app.delete("/delete/")
def delete_item(item_id:int):
    for item_json in database:
        if item_json["id"]==item_id:
            database.remove(item_json)
    return database
