from C_gestion_datos_herramientas import cargar_datos
from C_gestion_datos_usuarios import cargar_datos1
from C_gestion_datos_prestamos import cargar_datos2
from C_solicitudes_prestamos import cargar_datos_prestamo
from B_gestion_herramientas import gestion_herramientas1
from B_gestion_prestamos import gestion_prestamos
from B_consultas_reportes import menu_consultas
from B_sistema_permisos import login, consultar_herramientas, solicitar_herramienta, aprobar_solicitudes
from B_gestion_usuarios import gestion_usuarios1, crear_usuario_provisional


def menu():
    datos = cargar_datos()
    datos1 = cargar_datos1()
    datos_prestamos = cargar_datos2()
    solicitudes = cargar_datos_prestamo()

    if not datos1:
        print("\nNo hay datos de usuarios. Por favor cree un usuario administrador provisional")
        crear_usuario_provisional(datos1)
    
    usuario_actual = login(datos1)
    if usuario_actual:
        tipo = datos1[usuario_actual]["Tipo"]
    if tipo == "Administrador":
        while True:
            print("""
===========================
     MENU ADMINISTRADOR
===========================                 
1. Aprobar solicitudes
2. Gestión de herramientas
3. Gestión de usuarios
4. Gestión de préstamos
5. Consultas y reportes
6. Salir del programa""")
            op_admin = input("Seleccione opción: ")

            if op_admin == "1":
                aprobar_solicitudes(solicitudes, datos, datos_prestamos)
            elif  op_admin == "2":
                gestion_herramientas1(datos)
            elif op_admin == "3":
                gestion_usuarios1(datos1)
            elif op_admin == "4":
                gestion_prestamos(datos, datos1, datos_prestamos)
            elif op_admin == "5":
                menu_consultas(datos, datos1, datos_prestamos)
            elif op_admin == "6":
                print("Salida del programa. Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo")
            input("Presione cualquier tecla para continuar ....")
    if tipo == "Residente":
        while True:
            print("""
===========================
      MENU RESIDENTE
===========================  
1. Consultar herramientas
2. Solicitar herramienta
3. Salir del programa\n""")
            op_user = input("Seleccione opción: ")

            if op_user == "1":
                consultar_herramientas(datos, datos_prestamos)
            elif op_user == "2":
                solicitar_herramienta(usuario_actual, solicitudes, datos)
            elif op_user == "3":
                print("Salida del programa. Hasta luego!")
                break     
            else:
                print("Opción inválida. Intente de nuevo")
            input("Presione cualquier tecla para continuar ....")
menu()