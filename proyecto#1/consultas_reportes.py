from datetime import datetime

# -------------------------------
# 1️⃣ Herramientas con stock bajo
# -------------------------------

def herramientas_stock_bajo(herramientas, limite=3):
    print("\n🔎 HERRAMIENTAS CON STOCK BAJO\n")

    encontradas = False

    for id_h, datos in herramientas.items():
        if datos["Cantidad"] < limite and datos["Estado"] != "Inactiva":
            print(f"ID: {id_h}")
            print(f"Nombre: {datos['Nombre']}")
            print(f"Cantidad disponible: {datos['Cantidad']}")
            print("-" * 30)
            encontradas = True

    if not encontradas:
        print("No hay herramientas con stock bajo.")


# -----------------------------------
# 2️⃣ Préstamos activos y vencidos
# -----------------------------------

def prestamos_activos_vencidos(prestamos):
    print("\n📋 PRÉSTAMOS ACTIVOS Y VENCIDOS\n")

    hoy = datetime.now().date()
    encontrados = False

    for id_p, datos in prestamos.items():
        if datos["Estado"] == "Activo":
            fecha_dev = datetime.strptime(datos["Fecha_devolucion"], "%Y-%m-%d").date()

            estado_vencimiento = "VENCIDO" if fecha_dev < hoy else "Activo"

            print(f"\nPréstamo ID: {id_p}")
            print(f"Usuario: {datos['Usuario']}")
            print(f"Herramienta: {datos['Herramienta']}")
            print(f"Fecha devolución: {datos['Fecha_devolucion']}")
            print(f"Estado: {estado_vencimiento}")
            print("-" * 30)

            encontrados = True

    if not encontrados:
        print("No hay préstamos activos.")


# -----------------------------------
# 3️⃣ Historial de préstamos usuario
# -----------------------------------

def historial_usuario(prestamos, usuarios):
    print("\n📚 HISTORIAL DE PRÉSTAMOS POR USUARIO\n")

    id_usuario = input("Ingrese ID del usuario: ")

    if id_usuario not in usuarios:
        print("Usuario no encontrado.")
        return

    encontrados = False

    for id_p, datos in prestamos.items():
        if datos["Usuario"] == id_usuario:
            print(f"\nPréstamo ID: {id_p}")
            print(f"Herramienta: {datos['Herramienta']}")
            print(f"Cantidad: {datos['Cantidad']}")
            print(f"Fecha inicio: {datos['Fecha_inicio']}")
            print(f"Fecha devolución: {datos['Fecha_devolucion']}")
            print(f"Estado: {datos['Estado']}")
            print("-" * 30)
            encontrados = True

    if not encontrados:
        print("Este usuario no tiene préstamos registrados.")


# -----------------------------------
# 4️⃣ Herramientas más solicitadas
# -----------------------------------

def herramientas_mas_solicitadas(prestamos, herramientas):
    print("\n🏆 HERRAMIENTAS MÁS SOLICITADAS\n")

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
        print("-" * 30)


# -----------------------------------
# 5️⃣ Usuarios que más solicitan
# -----------------------------------

def usuarios_mas_activos(prestamos, usuarios):
    print("\n👥 USUARIOS QUE MÁS HERRAMIENTAS SOLICITAN\n")

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
        print("-" * 30)


# -----------------------------------
# MENÚ DE CONSULTAS
# -----------------------------------

def menu_consultas(herramientas, usuarios, prestamos):

    while True:
        print("""
📊 CONSULTAS Y REPORTES

1. Herramientas con stock bajo
2. Préstamos activos y vencidos
3. Historial de préstamos por usuario
4. Herramientas más solicitadas
5. Usuarios que más herramientas han solicitado
6. Volver al menú principal
--------------------------------
""")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            herramientas_stock_bajo(herramientas)
        elif opcion == "2":
            prestamos_activos_vencidos(prestamos)
        elif opcion == "3":
            historial_usuario(prestamos, usuarios)
        elif opcion == "4":
            herramientas_mas_solicitadas(prestamos, herramientas)
        elif opcion == "5":
            usuarios_mas_activos(prestamos, usuarios)
        elif opcion == "6":
            break
        else:
            print("Opción inválida")

        input("Presione cualquier tecla para continuar...")