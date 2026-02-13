from registro_logs import registrar_evento
from datetime import datetime

def login(usuarios):
    print("\n INICIO DE SESIÓN\n")

    id_usuario = input("Ingrese su ID: ")

    if id_usuario not in usuarios:
        print("Usuario no encontrado.")
        registrar_evento("WARNING", f"Intento de login con ID inexistente: {id_usuario}")
        return

    tipo = usuarios[id_usuario]["Tipo"]

    print(f"Bienvenido {usuarios[id_usuario]['Nombre']} ({tipo})")

    registrar_evento("INFO", f"Inicio de sesión. Usuario: {id_usuario}, Tipo: {tipo}")

    return id_usuario

def consultar_herramientas(herramientas, prestamos):
    print("\n ESTADO DE HERRAMIENTAS\n")

    for id_h, datos in herramientas.items():
        print(f"\nID: {id_h}")
        print(f"Nombre: {datos['Nombre']}")
        print(f"Cantidad disponible: {datos['Cantidad']}")
        print(f"Estado: {datos['Estado']}")

        for p in prestamos.values():
            if p["Herramienta"] == id_h and p["Estado"] == "Activo":
                print(f"Prestada a Usuario ID: {p['Usuario']}")
                print(f"Fecha devolución estimada: {p['Fecha_devolucion']}")

        print("-" * 30)

def solicitar_herramienta(id_usuario, solicitudes, herramientas):
    print("\n SOLICITAR HERRAMIENTA\n")

    id_herramienta = input("Ingrese ID herramienta: ")

    if id_herramienta not in herramientas:
        print("Herramienta no existe.")
        return

    cantidad = int(input("Cantidad solicitada: "))

    id_solicitud = str(len(solicitudes) + 1)

    solicitudes[id_solicitud] = {
        "Usuario": id_usuario,
        "Herramienta": id_herramienta,
        "Cantidad": cantidad,
        "Estado": "Pendiente",
        "Fecha": datetime.now().strftime("%Y-%m-%d")
    }

    registrar_evento(
        "INFO",
        f"Solicitud creada. ID solicitud: {id_solicitud}, Usuario: {id_usuario}, Herramienta: {id_herramienta}"
    )

    print("Solicitud enviada al administrador.")


def aprobar_solicitudes(solicitudes, herramientas, prestamos):
    print("\n SOLICITUDES PENDIENTES\n")

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
                        "Fecha_inicio": datetime.now().strftime("%Y-%m-%d"),
                        "Fecha_devolucion": "Pendiente",
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