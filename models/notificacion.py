from pydantic import BaseModel
from datetime import datetime

class Notificacion(BaseModel):
    id: int
    usuario_id: int
    mensaje: str
    fecha_envio: datetime
    leida: bool = False
