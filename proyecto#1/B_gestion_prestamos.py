from datetime import datetime
from C_gestion_datos_prestamos import guardar_datos2
from C_gestion_datos_herramientas import guardar_datos
   
def validar_Estado(fecha_dev):
    if datetime.strptime(fecha_dev, "%Y-%m-%d") < datetime.now():
        return "Vencido"
    else:
        return "Activo"

def  validar_usuario(usuarios):
    while True:
        id_usuario = input("Ingrese el ID del usuario: ").strip()
        
        if not id_usuario:
            print("Error: El ID no puede estar vacío.")
        elif not id_usuario.isdigit():
            print("Error: El ID solo debe contener números.")
        elif id_usuario not in usuarios:
                print("Usuario no existe.")    
        else:
            return id_usuario
        
def validar_herra(herramientas):       
    while True:
        id_herra = input("Digite ID de la herramienta: ").strip()

        if not id_herra:
            print("Error: El ID no puede estar vacío.")
        elif not id_herra.isdigit():
            print("Error: El ID solo debe contener números.") 
        elif id_herra not in herramientas:
            print("Esta herramienta no existe.")
        elif id_herra in herramientas and herramientas[id_herra]["Estado"] == "Inactiva":
            print("Error al cargar herramienta.")
        elif id_herra in herramientas and herramientas[id_herra]["Estado"] == "Reparacion":
            print("Herramienta en reparacion.")
        elif id_herra in herramientas and herramientas[id_herra]["Estado"] == "Fuera de servicio":
            print("Herramienta fuera de servicio.")
        else:
            return id_herra

def validar_cantidad(id_herramienta, herramientas):
    while True:
        cantidad = input("Ingrese la cantidad que desea: ").strip()
        if not cantidad:
            print("No puede estar vacío.")
        elif not cantidad.isdigit():
            print("Debe ser numérico.")
        elif int(cantidad) <=0:
            print("Debe ser mayor a 0")
        elif int(cantidad) > herramientas[id_herramienta]["Cantidad"]:
            print("Cantidad no disponible.")
        else:
            return int(cantidad)

def validar_id_prestamo(prestamos):
    while True:
        id_prestamo = input("Ingrese el ID del préstamo: ").strip()
        if not id_prestamo:
            print("No puede estar vacío.")
        elif not id_prestamo.isdigit():
            print("Debe ser numérico.")
        elif id_prestamo in prestamos:
            print("El ID ya existe")
        else:
            return id_prestamo
        
def validar_id_prestamo2(prestamos):
    while True:
        id_prestamo2 = input("Ingrese el ID del préstamo: ").strip()
        if not id_prestamo2:
            print("No puede estar vacío.")
        elif not id_prestamo2.isdigit():
            print("Debe ser numérico.")
        elif id_prestamo2 not in prestamos:
            print("Préstamo no encontrado.")
        else:
            return id_prestamo2

def validar_fecha(mensaje):
    while True:
        fecha = input(mensaje)
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            if datetime.strptime(fecha, "%Y-%m-%d") > datetime.now():
                print("Error: La fecha de inicio no puede ser posterior a la fecha actual.")
            else:
                return fecha
        except ValueError:
            print("Formato inválido. Use YYYY-MM-DD")

def validar_fecha2(mensaje, fecha_inicio):
    while True:
        fecha = input(mensaje)
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            if datetime.strptime(fecha, "%Y-%m-%d") <= datetime.strptime(fecha_inicio, "%Y-%m-%d"):
                print("Error: La fecha de devolución no puede ser anterior o igual a la fecha de inicio.")
            else:
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
            registrar_prestamo(herramientas, usuarios, prestamos)

        elif opcion == "2":
            devolver_herramienta(herramientas, prestamos)

        elif opcion == "3":
            listar_prestamos(prestamos)

        elif opcion == "4":
            guardar_datos2(prestamos)
            print("Datos guardados.")
            break

        else:
            print("Opción inválida")

def registrar_prestamo(herramientas, usuarios, prestamos):

    if not herramientas:
        print("No hay herramientas registradas.")
        return

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    id_prestamo = validar_id_prestamo(prestamos)
       
    id_usuario = validar_usuario(usuarios)

    id_herramienta = validar_herra(herramientas)

    cantidad = validar_cantidad(id_herramienta, herramientas)

    fecha_inicio = validar_fecha("Fecha inicio (YYYY-MM-DD): ")
    fecha_dev = validar_fecha2("Fecha estimada devolución (YYYY-MM-DD): ", fecha_inicio)
    estado = validar_Estado(fecha_dev)
    observaciones = input("Observaciones: ")

    herramientas[id_herramienta]["Cantidad"] -= int(cantidad)

    prestamos[id_prestamo] = {
        "Usuario": id_usuario,
        "Herramienta": id_herramienta,
        "Cantidad": int(cantidad),
        "Fecha_inicio": fecha_inicio,
        "Fecha_devolucion": fecha_dev,
        "Estado": estado,
        "Observaciones": observaciones
    }
    guardar_datos(herramientas)
    guardar_datos2(prestamos)

    print("Préstamo registrado correctamente.")

def devolver_herramienta(herramientas, prestamos):

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    id_prestamo = validar_id_prestamo2(prestamos)

    if prestamos[id_prestamo]["Estado"] == "Devuelto":
        print("Este préstamo ya fue cerrado.")
        return
    if prestamos[id_prestamo]["Estado"] == "Vencido":
        print("Este préstamo está vencido. Por favor, contacte al administrador.")
        return
    
    id_herramientas = prestamos[id_prestamo]["Herramienta"]
    cantidad = prestamos[id_prestamo]["Cantidad"]

    herramientas[id_herramientas]["Cantidad"] += cantidad

    prestamos[id_prestamo]["Estado"] = "Devuelto"
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