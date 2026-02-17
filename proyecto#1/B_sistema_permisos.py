from datetime import datetime
from C_registro_logs import registrar_evento
from C_solicitudes_prestamos import guardar_datos_prestamo
from C_gestion_datos_herramientas import guardar_datos

def fecha_Devolucion_estimada():
    while True:
        fecha_dev = input("Fecha estimada devolución (YYYY-MM-DD): ")
        try:
            datetime.strptime(fecha_dev, "%Y-%m-%d")
            if datetime.strptime(fecha_dev, "%Y-%m-%d") < datetime.now():
                print("Error: La fecha de devolución no puede ser anterior a la fecha actual.")
                registrar_evento(
                    "WARNING",
                    f"Fecha de devolucion {fecha_dev} inválida respecto a la fecha actual"
                )
            else:
                return fecha_dev
        except ValueError:
            print("Error: Formato de fecha inválido. Use YYYY-MM-DD.")
            registrar_evento(
                    "WARNING",
                    f"Fecha de devolucion {fecha_dev} no digitada correctamente"
                )

def validar_cantidad(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        else:
            print("Error: Debe ingresar un número entero positivo.")
            registrar_evento(
                    "WARNING",
                    f"Cantidad {valor} no digitada correctamente"
                )

def validar_id_herramienta(mensaje, herramientas):
    while True:
        id_h = input(mensaje).strip()
        if not id_h:
            print("Error: El ID no puede estar vacío.")
        elif not id_h.isdigit():
            print("Error: El ID solo debe contener números.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_h} no digitado correctamente"
                )
        elif id_h not in herramientas:
            print("Error: Ese ID de herramienta no existe.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_h} no registrado en el sistema"
                )
        else:
            return id_h

def login(usuarios):
    print("================================\n\tINICIO DE SESIÓN\n================================") 

    while True:
        id_usuario = input("Ingrese su ID: ")
        if id_usuario not in usuarios:
            print("Usuario no encontrado.")
            print("Intente nuevamente.")
            registrar_evento("WARNING", f"Intento de login con ID inexistente: {id_usuario}")
        else:
            break

    tipo = usuarios[id_usuario]["Tipo"]

    print(f"Bienvenido {usuarios[id_usuario]['Nombre']} ({tipo})")

    registrar_evento("INFO", f"Inicio de sesión. Usuario: {id_usuario}, Tipo: {tipo}")

    return id_usuario

def consultar_herramientas(herramientas, prestamos):
    print("=============================\nESTADO DE LAS HERRAMIENTAS\n=============================")


    for id_h, datos in herramientas.items():
        if datos["Estado"] == "Inactiva":
            continue
        print(f"\nID: {id_h}")
        print(f"Nombre: {datos['Nombre']}")
        print(f"Categoria: {datos['Categoria']}")
        print(f"Cantidad disponible: {datos['Cantidad']}")
        print(f"Estado: {datos['Estado']}")
        print(f"Valor: ${datos['Valor']:,.2f}")
        for p in prestamos.values():
            if p["Herramienta"] == id_h and p["Estado"] == "Activo":
                print(f"Prestada a Usuario ID: {p['Usuario']}")
                print(f"Cantidad prestada: {p['Cantidad']}")
        print("-" * 50)

def solicitar_herramienta(id_usuario, solicitudes, herramientas):
    print("========================\nSOLICITAR HERRAMIENTA\n========================")

    id_herramienta = validar_id_herramienta("Ingrese el ID de la herramienta que desea solicitar: ", herramientas)
    
    if herramientas[id_herramienta]["Estado"] == "Inactiva":
        print("Herramienta no disponible para préstamo.")
        return
    if herramientas[id_herramienta]["Estado"] == "Reparacion":
            print("Herramienta en reparación.")
            return
    if herramientas[id_herramienta]["Estado"] == "Fuera de servicio":
            print("Herramienta fuera de servicio.")
            return
    if herramientas[id_herramienta]["Cantidad"] <= 0:
            print("Herramienta sin stock disponible.")
            return
    while True:
        cantidad = validar_cantidad("Cantidad solicitada: ")
        if cantidad > herramientas[id_herramienta]["Cantidad"]:
            print("Cantidad solicitada excede el stock disponible.")
        else:
            break

    id_solicitud = str(len(solicitudes) + 1)

    solicitudes[id_solicitud] = {
        "Usuario": id_usuario,
        "Herramienta": id_herramienta,
        "Cantidad": cantidad,
        "Estado": "Pendiente",
        "Fecha de inicio": datetime.now().strftime("%Y-%m-%d")
    }

    registrar_evento(
        "INFO",
        f"Solicitud creada. ID solicitud: {id_solicitud}, Usuario: {id_usuario}, Herramienta: {id_herramienta}"
    )

    print("Solicitud enviada al administrador.")
    guardar_datos_prestamo(solicitudes)


def aprobar_solicitudes(solicitudes, herramientas, prestamos):
    print("========================\nSOLICITUDES PENDIENTES\n========================")

    for id_s, datos in solicitudes.items():
        if datos["Estado"] == "Pendiente":
            print(f"\nSolicitud ID: {id_s}")
            print(f"Usuario: {datos['Usuario']}")
            print(f"Herramienta: {datos['Herramienta']}")
            print(f"Cantidad: {datos['Cantidad']}")

            decision = input("Aprobar (A) / Rechazar (R): ").lower()

            if decision == "a":
                id_h = datos["Herramienta"]
                cantidad = datos["Cantidad"]

                if herramientas[id_h]["Cantidad"] >= cantidad:

                    herramientas[id_h]["Cantidad"] -= cantidad

                    id_prestamo = str(len(prestamos) + 1)

                    prestamos[id_prestamo] = {
    "Usuario": datos["Usuario"],
    "Herramienta": id_h,
    "Cantidad": cantidad,
    "Fecha de inicio": datetime.now().strftime("%Y-%m-%d"),
    "Fecha de devolución": fecha_Devolucion_estimada(),
    "Estado": "Activo",
    "Observaciones": "Aprobado por administrador"
}

                    datos["Estado"] = "Aprobada"

                    registrar_evento(
                        "INFO",
                        f"Solicitud aprobada. ID solicitud: {id_s}, Generó préstamo: {id_prestamo}"
                    )

                    print("Solicitud aprobada y préstamo generado.")

                else:
                    print("Stock insuficiente.")
                    registrar_evento(
                        "ERROR",
                        f"Solicitud rechazada por stock insuficiente. ID solicitud: {id_s}"
                    )

            elif decision == "r":
                datos["Estado"] = "Rechazada"
                registrar_evento(
                    "WARNING",
                    f"Solicitud rechazada por administrador. ID solicitud: {id_s}"
                )
                print("Solicitud rechazada.")
    guardar_datos_prestamo(solicitudes)
    guardar_datos(herramientas)