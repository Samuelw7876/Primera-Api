SERVICIOS = []
contador_id = 1

def registrar_servicio(data):
    global contador_id
    servicio = {
        "id": contador_id,
        "nombre": data.nombre,
        "descripcion": data.descripcion,
        "endpoints": data.endpoints
    }
    SERVICIOS.append(servicio)
    contador_id += 1
    return servicio

def listar_servicios():
    return SERVICIOS

def obtener_servicio(id_servicio: int):
    for servicio in SERVICIOS:
        if servicio["id"] == id_servicio:
            return servicio
    return None
