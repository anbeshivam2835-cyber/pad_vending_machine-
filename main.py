from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PadSelection(BaseModel):
    size: str

@app.get("/select-pad")
def select_pad(data:PadSelection):
    return {"message": "API Running"}

@app.post("/select-pad")
def select_pad(data: PadSelection):

    pads = {
        "regular": 10,
        "xl": 15,
        "xxl": 20
    }

    size = data.size.lower()

    if size not in pads:
        return {
            "success": False,
            "message": "Invalid pad size"
        }

    return {
        "success": True,
        "pad_size": size.upper(),
        "price": pads[size]
    }

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Nanba"}