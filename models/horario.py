from pydantic import BaseModel
from datetime import time

class Horario(BaseModel):
    id: int
    comercio_id: int
    dia_semana: str  # Ejemplo: "Lunes", "Martes", etc.
    apertura: time
    cierre: time
