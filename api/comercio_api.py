from fastapi import APIRouter
from models.comercio import Comercio
from controllers.comercio_controller import ComercioController

router = APIRouter()
comercio_controller = ComercioController()

@router.get("/comercios")
def obtener_comercios():
    return comercio_controller.listar_comercios()

@router.post("/comercios")
def crear_comercio(comercio: Comercio):
    return comercio_controller.crear_comercio(comercio)
