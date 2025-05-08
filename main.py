from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from models import *
from auth import autenticar_usuario, obtener_rol_por_token
from services import registrar_servicio, listar_servicios, obtener_servicio

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head><title>API Logística</title></head>
    <body>
      <h1>Bienvenido a la API de Logística Global</h1>

      <h2>Login</h2>
      <input id="user" placeholder="Usuario" />
      <input id="pass" type="password" placeholder="Contraseña" />
      <button onclick="login()">Iniciar Sesión</button>
      <p id="tokenMsg"></p>

      <h2>Registrar Servicio</h2>
      <input id="nombre" placeholder="Nombre Servicio" />
      <input id="desc" placeholder="Descripción" />
      <input id="endpoints" placeholder="Endpoints separados por coma" />
      <button onclick="registrarServicio()">Registrar</button>

      <h2>Ver Servicios</h2>
      <button onclick="listar()">Listar Servicios</button>
      <ul id="servicios"></ul>

      <script>
        let token = "";

        async function login() {
          const user = document.getElementById("user").value;
          const pass = document.getElementById("pass").value;
          const res = await fetch("/autenticar-usuario", {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ nombre_usuario: user, contrasena: pass })
          });
          const data = await res.text();
          token = data;
          document.getElementById("tokenMsg").innerText = "Token recibido: " + token;
        }

        async function registrarServicio() {
          const nombre = document.getElementById("nombre").value;
          const descripcion = document.getElementById("desc").value;
          const endpoints = document.getElementById("endpoints").value.split(",");
          const res = await fetch("/registrar-servicio", {
            method: "POST",
            headers: {
              'Content-Type': 'application/json',
              'Authorization': token
            },
            body: JSON.stringify({ nombre, descripcion, endpoints })
          });
          alert(await res.text());
        }

        async function listar() {
          const res = await fetch("/servicios", { headers: {'Authorization': token}});
          const data = await res.json();
          document.getElementById("servicios").innerHTML = data.map(s => "<li>" + s.nombre + "</li>").join("");
        }
      </script>
    </body>
    </html>
    """

@app.post("/autenticar-usuario")
def login(user: UsuarioLogin):
    token = autenticar_usuario(user.nombre_usuario, user.contrasena)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return token

@app.post("/registrar-servicio")
def registrar(data: ServicioInput, authorization: str = Header(None)):
    rol = obtener_rol_por_token(authorization)
    if rol != "Administrador":
        raise HTTPException(status_code=403, detail="No autorizado")
    return registrar_servicio(data)

@app.get("/servicios")
def listar(authorization: str = Header(None)):
    rol = obtener_rol_por_token(authorization)
    if not rol:
        raise HTTPException(status_code=401, detail="No autenticado")
    return listar_servicios()
