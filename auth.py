from fastapi import HTTPException
import secrets

usuarios = {
    "admin": {"contrasena": "1234", "rol": "Administrador"},
    "orquestador": {"contrasena": "abcd", "rol": "Orquestador"},
}

tokens = {}

def autenticar_usuario(nombre_usuario: str, contrasena: str):
    user = usuarios.get(nombre_usuario)
    if not user or user["contrasena"] != contrasena:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = secrets.token_hex(16)
    tokens[token] = user["rol"]
    return {"access_token": token, "rol": user["rol"]}

def verificar_token(token: str, roles_permitidos: list):
    rol = tokens.get(token)
    if not rol or rol not in roles_permitidos:
        raise HTTPException(status_code=403, detail="Acceso no autorizado")
    return rol
