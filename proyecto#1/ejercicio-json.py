"""
Ejercicio:
Hacer un programa que gestione la informacion de un camper. Un camper puede ver 1 o varios skill. Por cada skill hay una nota definitiva. El programa debe cargar, agregar, modificar, eliminar y guardar la informacion del camper de manera persistente.
"""

from gestion_datos import cargar_datos, guardar_datos
from gestion_campers import gestion_herramientas

def menu():
    datos = cargar_datos()
    while True:
        print("""
\nHERRAMIENTAS
1. Gestión de herramientas
2. Gestión de usuarios
3. Gestión de préstamos
4. Consultas y reportes
5. Registro de eventos (logs)
6. Permisos a manejar
7. Guardar o salir
--------------------------------
""")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestion_herramientas(datos)
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            id_camper = input("\n\n\nIngrese el ID del camper: ")
        elif opcion == "5":
            id_camper = input("\n\n\nIngrese el ID del camper: ")
            skill = input("Ingrese el skill: ")
        elif opcion == "6":
            id_camper = input("\n\n\nIngrese el ID del camper: ")
            skill = input("Ingrese el skill: ")  
        elif opcion == "7":
            guardar_datos(datos)
            print("Datos guardados. Saliendo ... \n\n")
            break
        else:
            print("Opción inválida. Intente de nuevo")
        input("Presione cualquier tecla para continuar ....")


menu()