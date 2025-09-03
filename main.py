import numbers
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health():
    return JSONResponse(content="Ok", status_code=200, media_type="text/plain")

class characteristics(BaseModel):
    ram_memory = numbers
    rom_memory = numbers


class phone(BaseModel):
    identifier = str
    brand = str
    model = str
    characteristics = characteristics

List_phones : List[phone] =[]

def serialize_phone(phone: phone):
    phones = []
    for characteristic in phone.characteristics:
        phones.append(characteristic.dict())
    return phones

def serialize_phones(phones_list: List[phone]):
    phones = []
    for phone in phones:
        phones.append(phone.model_dump(phones_list))
    return phones


@app.post("/phones")
def create_phones(phone: phone):
    List_phones.append(phone)

