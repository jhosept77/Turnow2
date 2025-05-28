from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: Optional[str] = None
    is_admin: bool = False

