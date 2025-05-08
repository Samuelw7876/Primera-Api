from fastapi import Header, HTTPException

usuarios_db = {
    "admin": {"password": "1234", "rol": "Administrador"},
    "orquestador": {"password": "abcd", "rol": "Orquestador"},
    "user": {"password": "0000", "rol": "Usuario"}
}

def autenticar_usuario(token: str = Header(...)):
    if token not in usuarios_db:
        raise HTTPException(status_code=401, detail="Token inválido")
    return usuarios_db[token]

def verificar_rol(usuario: dict, roles_permitidos: list):
    if usuario["rol"] not in roles_permitidos:
        raise HTTPException(status_code=403, detail="No autorizado")
