from pydantic import BaseModel
from typing import Dict


class Item(BaseModel):
    name: str


class Player(BaseModel):
    hp: int
    inventory: Dict[str, Item] = dict()
