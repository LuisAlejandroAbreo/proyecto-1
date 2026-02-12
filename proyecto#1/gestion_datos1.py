import json

def cargar_datos1(nom_archivo="usuarios.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
    
def guardar_datos1(datos, nom_archivo="usuarios.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception as ex:
        datos = {}