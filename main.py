from fastapi import FastAPI, Header, Depends
from models import Usuario, Acceso, Orquestacion, NuevoServicio, ReglasOrquestacion
from auth import autenticar_usuario, verificar_rol
import services

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente en Railway"}

@app.post("/autenticar-usuario")
def autenticar(usuario: Usuario):
    if usuario.nombre_usuario in services.usuarios_db and services.usuarios_db[usuario.nombre_usuario]["password"] == usuario.contrasena:
        return {"token": usuario.nombre_usuario}
    return {"error": "Credenciales inválidas"}

@app.post("/autorizar-acceso")
def autorizar(acceso: Acceso, usuario=Depends(autenticar_usuario)):
    verificar_rol(usuario, [acceso.rol_usuario])
    return {"mensaje": "Acceso autorizado"}

@app.post("/registrar-servicio")
def registrar_servicio(servicio: NuevoServicio, usuario=Depends(autenticar_usuario)):
    verificar_rol(usuario, ["Administrador"])
    return services.registrar_servicio(servicio)

@app.get("/informacion-servicio/{id}")
def informacion_servicio(id: int, usuario=Depends(autenticar_usuario)):
    return services.obtener_info_servicio(id)

@app.put("/actualizar-reglas-orquestacion")
def actualizar_reglas(reglas: ReglasOrquestacion, usuario=Depends(autenticar_usuario)):
    verificar_rol(usuario, ["Orquestador"])
    return services.actualizar_reglas(reglas.reglas)

@app.post("/orquestar")
def orquestar(datos: Orquestacion, usuario=Depends(autenticar_usuario)):
    verificar_rol(usuario, ["Orquestador", "Administrador"])
    return services.orquestar_servicio(datos)
