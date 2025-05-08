from models import Servicio

servicios = []
contador = 1

def registrar_servicio(servicio: Servicio):
    global contador
    servicio.id = contador
    contador += 1
    servicios.append(servicio)
    return servicio

def obtener_servicio(id: int):
    for s in servicios:
        if s.id == id:
            return s
    return None

def eliminar_servicio(id: int):
    global servicios
    servicios = [s for s in servicios if s.id != id]

def actualizar_servicio(id: int, nuevo_servicio: Servicio):
    for i, s in enumerate(servicios):
        if s.id == id:
            servicios[i] = nuevo_servicio
            return nuevo_servicio
    return None

def patch_servicio(id: int, nueva_descripcion: str):
    for s in servicios:
        if s.id == id:
            s.descripcion = nueva_descripcion
            return s
    return None
