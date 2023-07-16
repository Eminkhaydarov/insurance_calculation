from datetime import date

from pydantic import BaseModel


class CargoItem(BaseModel):
    cargo_type: str
    rate: str
