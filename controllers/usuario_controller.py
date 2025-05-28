from models.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.usuarios = []

    def listar_usuarios(self):
        return self.usuarios

    def crear_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        return {"msg": "Usuario creado", "usuario": usuario}

    def actualizar_usuario(self, usuario_id: int, usuario: Usuario):
        if 0 <= usuario_id < len(self.usuarios):
            self.usuarios[usuario_id] = usuario
            return {"msg": "Usuario actualizado", "usuario": usuario}
        return {"msg": "Usuario no encontrado"}, 404
