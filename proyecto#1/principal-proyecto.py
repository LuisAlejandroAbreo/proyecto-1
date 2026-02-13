from gestion_datos_herramientas import cargar_datos
from gestion_datos_usuarios import cargar_datos1
from gestion_datos_prestamos import cargar_datos2
from gestion_usuarios import gestion_usuarios1
from gestion_herramientas import gestion_herramientas1
from gestion_prestamos import gestion_prestamos
from consultas_reportes import menu_consultas
from sistema_permisos import login, consultar_herramientas, solicitar_herramienta, aprobar_solicitudes

def menu():
    datos = cargar_datos()
    datos1 = cargar_datos1()
    datos_prestamos = cargar_datos2()
    solicitudes = {}
    while True:
        print("""
\nHERRAMIENTAS
1. Gestión de herramientas
2. Gestión de usuarios
3. Gestión de préstamos
4. Consultas y reportes
5. Iniciar sesión
6. Salir del programa
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
            usuario_actual = login(datos1)
            if usuario_actual:
                tipo = datos1[usuario_actual]["Tipo"]
            if tipo == "Administrador":
                while True:
                    print("""
 1. Aprobar solicitudes
2. Volver""")
                    op_admin = input("Seleccione opción: ")

                    if op_admin == "1":
                        aprobar_solicitudes(solicitudes, datos, datos_prestamos)
                    elif op_admin == "2":
                        break

            else: 
                while True:
                    print("""
1. Consultar herramientas
2. Solicitar herramienta
3. Volver""")
                    op_user = input("Seleccione opción: ")

                    if op_user == "1":
                                consultar_herramientas(datos, datos_prestamos)
                    elif op_user == "2":
                                solicitar_herramienta(usuario_actual, solicitudes, datos)
                    elif op_user == "3":
                        break 
        elif opcion == "6":
            print("Salida del programa. Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo")
        input("Presione cualquier tecla para continuar ....")


menu()