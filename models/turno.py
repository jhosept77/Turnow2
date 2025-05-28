from pydantic import BaseModel
from datetime import datetime

class Turno(BaseModel):
    id: int
    usuario_id: int
    comercio_id: int
    servicio_id: int
    fecha_hora: datetime
    estado: str 