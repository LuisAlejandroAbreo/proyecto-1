import json

def cargar_datos2(nom_archivo="prestamos.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
    
def guardar_datos2(datos, nom_archivo="prestamos.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception as ex:
        datos = {}
