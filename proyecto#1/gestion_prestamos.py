from datetime import datetime
from gestion_datos_prestamos import guardar_datos2
from gestion_datos import guardar_datos

def validar_id_prestamo(prestamos):
    while True:
        id_prestamo = input("Ingrese el ID del préstamo: ").strip()
        if not id_prestamo:
            print("No puede estar vacío.")
        elif not id_prestamo.isdigit():
            print("Debe ser numérico.")
        elif id_prestamo in prestamos:
            print("Ese ID ya existe.")
        else:
            return id_prestamo


def validar_fecha(mensaje):
    while True:
        fecha = input(mensaje)
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Formato inválido. Use YYYY-MM-DD")

def gestion_prestamos(herramientas, usuarios, prestamos):


    while True:
        print("""
1. Registrar préstamo
2. Devolver herramienta
3. Listar préstamos
4. Guardar y volver
""")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_prestamo(prestamos, herramientas, usuarios)

        elif opcion == "2":
            devolver_herramienta(prestamos, herramientas)

        elif opcion == "3":
            listar_prestamos(prestamos)

        elif opcion == "4":
            guardar_datos2(prestamos)
            print("Datos guardados.")
            break

        else:
            print("Opción inválida")

def registrar_prestamo(prestamos, herramientas, usuarios):


    if not herramientas:
        print("No hay herramientas registradas.")
        return

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    id_prestamo = validar_id_prestamo(prestamos)

    id_usuario = input("Ingrese ID del usuario: ")
    if id_usuario not in usuarios:
        print("Usuario no existe.")
        return

    id_herramienta = input("Ingrese ID de la herramienta: ")
    if id_herramienta not in herramientas:
        print("Herramienta no existe.")
        return
    if id_herramienta in herramientas and herramientas[id_herramienta]["Estado"] == "Inactiva":
        print("Herramienta está inactiva.")
        return

    cantidad = int(input("Cantidad a prestar: "))

    if herramientas[id_herramienta]["Cantidad"] < cantidad:
        print("No hay suficiente stock disponible.")
        return

    fecha_inicio = validar_fecha("Fecha inicio (YYYY-MM-DD): ")
    fecha_dev = validar_fecha("Fecha estimada devolución (YYYY-MM-DD): ")

    observaciones = input("Observaciones: ")

    herramientas[id_herramienta]["Cantidad"] -= cantidad

    prestamos[id_prestamo] = {
        "Usuario": id_usuario,
        "Herramienta": id_herramienta,
        "Cantidad": cantidad,
        "Fecha_inicio": fecha_inicio,
        "Fecha_devolucion": fecha_dev,
        "Estado": "Activo",
        "Observaciones": observaciones
    }
    guardar_datos(herramientas)
    guardar_datos2(prestamos)

    print("Préstamo registrado correctamente.")

def devolver_herramienta(prestamos, herramientas):

    id_prestamo = input("Ingrese ID del préstamo: ")

    if id_prestamo not in prestamos:
        print("Préstamo no encontrado.")
        return

    if prestamos[id_prestamo]["Estado"] != "Activo":
        print("Este préstamo ya fue cerrado.")
        return

    id_herramienta = prestamos[id_prestamo]["Herramienta"]
    cantidad = prestamos[id_prestamo]["Cantidad"]

    herramientas[id_herramienta]["Cantidad"] += cantidad

    prestamos[id_prestamo]["Estado"] = "Devuelto"
    herramientas[id_herramienta]["Cantidad"] += cantidad
    guardar_datos(herramientas)
    guardar_datos2(prestamos)

    print("Herramienta devuelta correctamente.")

def listar_prestamos(prestamos):

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    for id_prestamo, datos in prestamos.items():
        print(f"\nPréstamo ID: {id_prestamo}")
        for k, v in datos.items():
            print(f"{k}: {v}")
        print("-" * 30)