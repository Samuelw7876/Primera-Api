# Datos simulados en memoria
servicios = []
reglas = {}

def registrar_servicio(datos):
    servicios.append(datos)
    return {"mensaje": "Servicio registrado"}

def obtener_info_servicio(id):
    try:
        return servicios[int(id)]
    except:
        return {"error": "Servicio no encontrado"}

def actualizar_reglas(nuevas_reglas):
    reglas.update(nuevas_reglas)
    return {"mensaje": "Reglas actualizadas"}

def orquestar_servicio(datos):
    return {"mensaje": f"Orquestando servicio {datos.servicio_destino}"}
