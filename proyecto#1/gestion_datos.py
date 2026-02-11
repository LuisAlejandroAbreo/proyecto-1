"""
Este modulo se encarga de gestionar los datos json en el disco
"""

import json

def cargar_datos(nom_archivo="herramientas.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
    
def guardar_datos(datos, nom_archivo="herramientas.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception as ex:
        datos = {}
