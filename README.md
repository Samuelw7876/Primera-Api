# 🚚 API de Logística Global

Una API RESTful construida con FastAPI para simular la orquestación de servicios en una empresa de logística.

## 🔗 Acceso a la API

👉 Visita la API en: [https://mi-api-logistica.up.railway.app](https://mi-api-logistica.up.railway.app)

👉 Documentación interactiva: [https://mi-api-logistica.up.railway.app/docs](https://mi-api-logistica.up.railway.app/docs)

---

## 📌 Funcionalidades

- 🔐 Autenticación por token (simulada)
- ✅ CRUD de servicios
- ⚙️ Simulación de orquestación de servicios
- 👥 Control de acceso por roles: `Administrador` y `Orquestador`

---

## 🛠️ Cómo usar la API

### 1. Autenticarse

Usa `/autenticar-usuario` con uno de estos usuarios:

| Usuario      | Contraseña | Rol          |
|--------------|------------|--------------|
| `admin`      | `1234`     | Administrador |
| `orquestador`| `abcd`     | Orquestador   |

Obtendrás un `access_token`.

---

### 2. Copiar el token

- En cada petición, agrega el token en el campo `token` del header.

---

### 3. Probar las rutas

Desde `/docs`, puedes:
- Registrar, consultar, actualizar o eliminar servicios
- Simular la orquestación de servicios

---

## 🧪 Tecnologías

- Python 3.10+
- FastAPI
- Railway (Deploy)

---

## ⚠️ Nota

Esta API es **una simulación académica** para propósitos de demostración. No incluye base de datos ni seguridad real.

---

## 📂 Estructura del proyecto

