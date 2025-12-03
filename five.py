from enum import Enum

from fastapi import FastAPI


app = FastAPI()

class Name(str, Enum):
    keerthana = "keerthana"
    ganesh= "ganesh"

@app.get("/names/{name}")
def get_model(name: Name):
  return {"name" : name}
    
