from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="100002"
)

user = User(
    id=1,
    name="Abc",
    address=address, #I have taken address from the line no 15.This is how it works
)

#using dictionary method
user_data = {
    "id": 1,
    "name": "Abc",
    "address": {
        "street": "321 Local street",
        "city": "Paris",
        "postal_code":"200002"
    }
}

user = User(**user_data)
print(user)