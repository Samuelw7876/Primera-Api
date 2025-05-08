USUARIOS = {
    "admin": {"password": "admin123", "rol": "Administrador"},
    "orquestador": {"password": "orq123", "rol": "Orquestador"},
    "usuario": {"password": "user123", "rol": "Usuario"}
}

TOKENS = {}

def autenticar_usuario(nombre_usuario: str, contrasena: str) -> str:
    usuario = USUARIOS.get(nombre_usuario)
    if usuario and usuario["password"] == contrasena:
        token = f"token_{nombre_usuario}"
        TOKENS[token] = usuario["rol"]
        return token
    return ""

def obtener_rol_por_token(token: str) -> str:
    return TOKENS.get(token, "")
