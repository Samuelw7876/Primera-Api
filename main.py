# main.py
from fastapi import FastAPI, Header, HTTPException
from auth import autenticar_usuario, verificar_token
from services import *
from models import *

app = FastAPI(title="API de Logística Global", description="Orquestación de servicios REST para la empresa Logística Global.", version="1.0")

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Logística Global. Visita /docs para ver las rutas disponibles."}

@app.post("/autenticar-usuario")
def login(datos: Usuario):
    return autenticar_usuario(datos.nombre_usuario, datos.contrasena)

@app.post("/registrar-servicio")
def crear_servicio(servicio: Servicio, token: str = Header(...)):
    verificar_token(token, ["Administrador"])
    return registrar_servicio(servicio)

@app.get("/informacion-servicio/{id}")
def ver_servicio(id: int, token: str = Header(...)):
    verificar_token(token, ["Administrador", "Orquestador"])
    servicio = obtener_servicio(id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio

@app.delete("/eliminar-servicio/{id}")
def eliminar(id: int, token: str = Header(...)):
    verificar_token(token, ["Administrador"])
    eliminar_servicio(id)
    return {"mensaje": "Servicio eliminado"}

@app.put("/actualizar-servicio/{id}")
def actualizar(id: int, servicio: Servicio, token: str = Header(...)):
    verificar_token(token, ["Administrador"])
    actualizado = actualizar_servicio(id, servicio)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return actualizado

@app.patch("/actualizar-parcial/{id}")
def actualizar_parcial(id: int, descripcion: str, token: str = Header(...)):
    verificar_token(token, ["Administrador"])
    return patch_servicio(id, descripcion)

@app.post("/orquestar")
def orquestar(data: Orquestacion, token: str = Header(...)):
    verificar_token(token, ["Orquestador", "Administrador"])
    return {"mensaje": f"Orquestando {data.servicio_destino} con {data.parametros_adicionales}"}