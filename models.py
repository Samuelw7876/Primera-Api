from pydantic import BaseModel
from typing import List, Dict

class Usuario(BaseModel):
    nombre_usuario: str
    contrasena: str

class Acceso(BaseModel):
    recursos: List[str]
    rol_usuario: str

class Orquestacion(BaseModel):
    servicio_destino: str
    parametros_adicionales: Dict[str, str]

class NuevoServicio(BaseModel):
    nombre: str
    descripcion: str
    endpoints: List[str]

class ReglasOrquestacion(BaseModel):
    reglas: Dict[str, str]
