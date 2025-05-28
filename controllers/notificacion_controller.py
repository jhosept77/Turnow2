from models.notificacion import Notificacion

class NotificacionController:
    def __init__(self):
        self.notificaciones = []

    def listar_notificaciones(self):
        return self.notificaciones

    def crear_notificacion(self, notificacion: Notificacion):
        self.notificaciones.append(notificacion)
        return {"msg": "Notificación creada", "notificacion": notificacion}
