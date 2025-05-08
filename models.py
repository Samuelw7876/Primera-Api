from pydantic import BaseModel
from typing import List, Optional

class Servicio(BaseModel):
    id: int
    nombre: str
    descripcion: str
    endpoints: List[str]

class Usuario(BaseModel):
    nombre_usuario: str
    contrasena: str
    rol: str  # "Administrador", "Orquestador", etc.

class Orquestacion(BaseModel):
    servicio_destino: str
    parametros_adicionales: Optional[dict] = {}

class ReglaOrquestacion(BaseModel):
    reglas: dict

class Acceso(BaseModel):
    recursos: List[str]
    rol_usuario: str
