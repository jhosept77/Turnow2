from models.comercio import Comercio

class ComercioController:
    def __init__(self):
        self.comercios = []

    def listar_comercios(self):
        return self.comercios

    def crear_comercio(self, comercio: Comercio):
        self.comercios.append(comercio)
        return {"msg": "Comercio creado", "comercio": comercio}
