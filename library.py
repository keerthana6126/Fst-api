from fastapi import FastAPI
from pydantic import BaseModel




app=FastAPI()

class ItemInput(BaseModel):
    book_name : str
    author_name: str
    published_year:int


database=[]

@app.post("/add_books")
def add_book_details(item_input:ItemInput):
    if  len(database) == 0:
        id = 1
    else :
        latest_item = database[-1]
        id = latest_item["id"] + 1
    current_item  = {"id" : id , "book_name" : item_input.book_name, "author_name":item_input.author_name, "published_year": item_input.published_year }
    database.append(current_item)
    return database


@app.delete("/delete")
def delete_item(item_id:int):
    for item_json in database:
        if item_json["id"]==item_id:
            database.remove(item_json)
    return database



@app.get("/book_details/{item_id}")
def single_book(item_id: int):
    for item_json in database:
        if item_json["id"] == item_id:
            return item_json
        

@app.get("/books")
def get_all_books():
    return database

        
    

@app.put("/update_book/{item_id}")
def update_book(item_id: int, item_input: ItemInput):
    for item_json in database:
        if item_json["id"] == item_id:
            item_json["book_name"] = item_input.book_name
            item_json["author_name"] = item_input.author_name
            return item_json

   