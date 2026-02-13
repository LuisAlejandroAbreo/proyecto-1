from gestion_datos import cargar_datos
from gestion_datos1 import cargar_datos1
from gestion_datos_prestamos import cargar_datos2
from gestion_usuarios import gestion_usuarios1
from gestion_herramientas import gestion_herramientas1
from gestion_prestamos import gestion_prestamos
from consultas_reportes import menu_consultas

def menu():
    datos = cargar_datos()
    datos1 = cargar_datos1()
    datos_prestamos = cargar_datos2()
    while True:
        print("""
\nHERRAMIENTAS
1. Gestión de herramientas
2. Gestión de usuarios
3. Gestión de préstamos
4. Consultas y reportes
5. Registro de eventos (logs)
6. Permisos a manejar
7. Salir del programa
--------------------------------
""")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestion_herramientas1(datos)
        elif opcion == "2":
            gestion_usuarios1(datos1)
        elif opcion == "3":
            gestion_prestamos(datos, datos1, datos_prestamos)
        elif opcion == "4":
            menu_consultas(datos, datos1, datos_prestamos)
        elif opcion == "5":
            pass
        elif opcion == "6":
            id_camper = input("\n\n\nIngrese el ID del camper: ")
            skill = input("Ingrese el skill: ")  
        elif opcion == "7":
            print("Salida del programa. Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo")
        input("Presione cualquier tecla para continuar ....")


menu()