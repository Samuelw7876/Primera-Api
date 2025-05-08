from pydantic import BaseModel
from typing import List, Optional

class UsuarioLogin(BaseModel):
    nombre_usuario: str
    contrasena: str

class Servicio(BaseModel):
    id: int
    nombre: str
    descripcion: str
    endpoints: List[str]

class ServicioInput(BaseModel):
    nombre: str
    descripcion: str
    endpoints: List[str]

class OrquestacionInput(BaseModel):
    servicio_destino: str
    parametros_adicionales: Optional[str] = None

class ReglaOrquestacion(BaseModel):
    reglas: str

class AutorizacionInput(BaseModel):
    recursos: List[str]
    rol_usuario: str
