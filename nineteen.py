from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class UserInput(BaseModel):
    name : str
    age:int
    number :Optional[str] = None 


@app.post("/userdetails")
def user_registration(user_input:UserInput):
    res_json = {"name" : user_input.name , "age":user_input.age , "number" : user_input.number}
    return res_json