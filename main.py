from fastapi import FastAPI
from api.usuario_api import router as usuario_router
from api.turno_api import router as turno_router
from api.comercio_api import router as comercio_router
from api.notificacion_api import router as notificacion_router

app = FastAPI()

app.include_router(usuario_router)
app.include_router(turno_router)
app.include_router(comercio_router)
app.include_router(notificacion_router)

@app.get("/")
def home():
    return {"msg": "API funcionando correctamente "}
