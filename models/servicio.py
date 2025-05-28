from pydantic import BaseModel

class Servicio(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
