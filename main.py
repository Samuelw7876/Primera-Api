from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

servicios = {}
usuarios = {
    "admin": {"rol": "Administrador"},
    "orquestador": {"rol": "Orquestador"},
    "usuario": {"rol": "Usuario"}
}

class Servicio(BaseModel):
    nombre: str
    descripcion: str
    endpoints: List[str]

class Orquestacion(BaseModel):
    servicio_destino: str
    parametros_adicionales: Optional[dict] = None

class Reglas(BaseModel):
    reglas: str

class Credenciales(BaseModel):
    nombre_usuario: str
    contrasena: str

class Autorizacion(BaseModel):
    recursos: List[str]
    rol_usuario: str

@app.post("/autenticar-usuario")
def autenticar_usuario(cred: Credenciales):
    if cred.nombre_usuario in usuarios:
        return {"token": f"token-{cred.nombre_usuario}", "rol": usuarios[cred.nombre_usuario]["rol"]}
    raise HTTPException(status_code=401, detail="Usuario inválido")

@app.post("/autorizar-acceso")
def autorizar_acceso(auth: Autorizacion):
    if auth.rol_usuario in ["Administrador", "Orquestador", "Usuario"]:
        return {"acceso": "autorizado"}
    raise HTTPException(status_code=403, detail="Acceso denegado")

@app.post("/registrar-servicio")
def registrar_servicio(servicio: Servicio):
    servicios[servicio.nombre] = servicio
    return {"mensaje": "Servicio registrado"}

@app.get("/informacion-servicio/{id}")
def informacion_servicio(id: str):
    if id in servicios:
        return servicios[id]
    raise HTTPException(status_code=404, detail="Servicio no encontrado")

@app.put("/actualizar-reglas-orquestacion")
def actualizar_reglas(reglas: Reglas):
    return {"mensaje": "Reglas actualizadas", "nuevas_reglas": reglas.reglas}

@app.post("/orquestar")
def orquestar(data: Orquestacion):
    if data.servicio_destino in servicios:
        return {
            "mensaje": f"Orquestación enviada al servicio {data.servicio_destino}",
            "datos": data.parametros_adicionales
        }
    raise HTTPException(status_code=404, detail="Servicio destino no encontrado")
