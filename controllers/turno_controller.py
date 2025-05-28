from models.turno import Turno

class TurnoController:
    def __init__(self):
        self.turnos = []

    def listar_turnos(self):
        return self.turnos

    def crear_turno(self, turno: Turno):
        self.turnos.append(turno)
        return {"msg": "Turno creado", "turno": turno}
