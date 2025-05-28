from fastapi import APIRouter
from models.notificacion import Notificacion
from controllers.notificacion_controller import NotificacionController

router = APIRouter()
notificacion_controller = NotificacionController()

@router.get("/notificaciones")
def obtener_notificaciones():
    return notificacion_controller.listar_notificaciones()

@router.post("/notificaciones")
def crear_notificacion(notificacion: Notificacion):
    return notificacion_controller.crear_notificacion(notificacion)
