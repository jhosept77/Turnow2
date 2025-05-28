from pydantic import BaseModel
from typing import List

class Comercio(BaseModel):
    id: int
    nombre: str
    direccion: str
    telefono: str
    servicios: List[str]
