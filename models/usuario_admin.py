from pydantic import BaseModel

class UsuarioAdmin(BaseModel):
    id: int
    nombre: str
    email: str
    permisos: list[str]
