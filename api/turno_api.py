from fastapi import APIRouter
from models.turno import Turno
from controllers.turno_controller import TurnoController

router = APIRouter()
turno_controller = TurnoController()

@router.get("/turnos")
def obtener_turnos():
    return turno_controller.listar_turnos()

@router.post("/turnos")
def crear_turno(turno: Turno):
    return turno_controller.crear_turno(turno)
