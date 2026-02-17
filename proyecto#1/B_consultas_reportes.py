from datetime import datetime
from C_registro_logs import registrar_evento

def validar_id(usuarios):
    while True:
        id_usuario = input("Ingrese el ID del usuario: ").strip()
        
        if not id_usuario:
            print("Error: El ID no puede estar vacío.")
        elif not id_usuario.isdigit():
            print("Error: El ID solo debe contener números.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_usuario} no digitado en el formato adecuado"
                )
        elif id_usuario not in usuarios:
            print("Usuario no encontrado.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_usuario} no registrado en el sistema"
                )
        else:
            return id_usuario

def herramientas_stock_bajo(herramientas):
    print("============================\nHERRAMIENTAS CON STOCK BAJO\n============================")

    encontrados = False

    for id_h, datos in herramientas.items():
        if datos["Cantidad"] <= 3 and datos["Estado"] != "Inactiva":
            print(f"ID: {id_h}")
            print(f"Nombre: {datos['Nombre']}")
            print(f"Cantidad disponible: {datos['Cantidad']}")
            print("-" * 50)
            encontrados = True
    registrar_evento(
                    "INFO",
                    f"Herramientas con bajo stock consultado"
                )
    if not encontrados:
        print("No hay herramientas con stock bajo.")

def prestamos_activos_vencidos(prestamos):
    print("=============================\nPRÉSTAMOS ACTIVOS Y VENCIDOS\n=============================")
    
    encontrados = False

    for id_p, datos in prestamos.items():

        if datos["Estado"] == "Devuelto":
            continue

        print(f"Préstamo ID: {id_p}")
        print(f"Usuario: {datos['Usuario']}")
        print(f"Herramienta: {datos['Herramienta']}")
        print(f"Cantidad: {datos['Cantidad']}")
        print(f"Estado: {datos['Estado']}")
        print("-" * 50)

        encontrados = True

    registrar_evento(
        "INFO",
        "Prestamos activos y vencidos consultados"
    )

    if not encontrados:
        print("No hay préstamos activos ni vencidos.")
def historial_usuario(usuarios, prestamos):
    print("===================================\nHISTORIAL DE PRÉSTAMOS POR USUARIO\n===================================")

    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    if not prestamos:
        print("No hay préstamos registrados.")
        return

    id_usuario = validar_id(usuarios)

    encontrados = False

    for id_p, datos in prestamos.items():
        if datos["Usuario"] == id_usuario:
            print(f"\nPréstamo ID: {id_p}")
            print(f"Herramienta: {datos['Herramienta']}")
            print(f"Cantidad: {datos['Cantidad']}")
            print(f"Estado: {datos['Estado']}")
            print("-" * 50)
            encontrados = True
    registrar_evento(
                    "INFO",
                    f"Historial de prestamos por usuario consultados"
                )

    if not encontrados:
        print("Este usuario no tiene préstamos registrados.")

def herramientas_mas_solicitadas(herramientas, prestamos):
    print("==============================\nHERRAMIENTAS MÁS SOLICITADAS\n==============================")

    contador = {}

    for datos in prestamos.values():
        id_h = datos["Herramienta"]
        cantidad = datos["Cantidad"]

        if id_h in contador:
            contador[id_h] += cantidad
        else:
            contador[id_h] = cantidad

    if not contador:
        print("No hay datos de préstamos.")
        return

    ranking = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    for id_h, total in ranking:
        nombre = herramientas[id_h]["Nombre"] if id_h in herramientas else "Desconocida"
        print(f"Herramienta: {nombre} (ID: {id_h})")
        print(f"Total solicitada: {total}")
        print("-" * 50)
        registrar_evento(
                    "INFO",
                    f"Historial de herramientas mas solicitadas consultado"
                )

def usuarios_mas_activos(usuarios, prestamos):
    print("==========================================\nUSUARIOS QUE MÁS HERRAMIENTAS SOLICITAN\n==========================================")

    contador = {}

    for datos in prestamos.values():
        id_u = datos["Usuario"]
        cantidad = datos["Cantidad"]

        if id_u in contador:
            contador[id_u] += cantidad
        else:
            contador[id_u] = cantidad

    if not contador:
        print("No hay datos de préstamos.")
        return

    ranking = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    for id_u, total in ranking:
        nombre = usuarios[id_u]["Nombre"] if id_u in usuarios else "Desconocido"
        print(f"Usuario: {nombre} (ID: {id_u})")
        print(f"Total herramientas solicitadas: {total}")
        print("-" * 50)
        registrar_evento(
                    "INFO",
                    f"Historial de usuarios con mas herramientas solicitadas consultado"
                )

def menu_consultas(herramientas, usuarios, prestamos):

    while True:
        print("""
===============================================
            CONSULTAS Y REPORTES
===============================================
1. Herramientas con stock bajo
2. Préstamos activos y vencidos
3. Historial de préstamos por usuario
4. Herramientas más solicitadas
5. Usuarios que más herramientas han solicitado
6. Volver al menú principal
------------------------------------------------
""")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            herramientas_stock_bajo(herramientas)
        elif opcion == "2":
            prestamos_activos_vencidos(prestamos)
        elif opcion == "3":
            historial_usuario(usuarios, prestamos)
        elif opcion == "4":
            herramientas_mas_solicitadas(herramientas, prestamos)
        elif opcion == "5":
            usuarios_mas_activos(usuarios, prestamos)
        elif opcion == "6":
            break
        else:
            print("Opción inválida")

        input("Presione cualquier tecla para continuar...")