from fastapi import APIRouter
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController

router = APIRouter()
usuario_controller = UsuarioController()

@router.get("/usuarios")
def obtener_usuarios():
    return usuario_controller.listar_usuarios()

@router.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return usuario_controller.crear_usuario(usuario)

@router.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: Usuario):
    return usuario_controller.actualizar_usuario(usuario_id, usuario)
