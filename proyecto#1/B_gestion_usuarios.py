from C_gestion_datos_usuarios import guardar_datos1
from C_registro_logs import registrar_evento

def validar_id(datos1):
    while True:
        id_vecino = input("Ingrese el ID del usuario: ").strip()
        
        if not id_vecino:
            print("Error: El ID no puede estar vacío.")
        elif not id_vecino.isdigit():
            print("Error: El ID solo debe contener números.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_vecino} no digitado correctamente"
                )
        elif id_vecino not in datos1:
            print("Error: Ese ID no existe.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_vecino} no registrado en el sistema"
                )
        else:
            return id_vecino

def validar_usuario(datos1):
    while True:
        id_vecino = input("Ingrese el ID del usuario: ").strip()
        
        if not id_vecino:
            print("Error: El ID no puede estar vacío.")
            
        elif not id_vecino.isdigit():
            print("Error: El ID solo debe contener números.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_vecino} no digitado correctamente"
                )
        elif id_vecino in datos1:
            print("Error: Ese ID ya existe.")
            registrar_evento(
                    "WARNING",
                    f"ID {id_vecino} ya registrado en el sistema"
                )
        else:
            return id_vecino

def validar_nombres(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.replace(" ", "").isalpha():
            return texto.title()
        else:
            print("Error: Solo se permiten letras y espacios.")
            registrar_evento(
                    "WARNING",
                    f"Texto {texto} no digitado correctamente"
                )

def validar_tel(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and len(valor) == 10:
            return int(valor)
        else:
            print("Error: Debe ingresar un número válido con 10 digitos.")
            registrar_evento(
                    "WARNING",
                    f"ID {valor} no digitado correctamente"
                )

def validar_dire(mensaje):
    while True:
        direccion = input(mensaje).strip().title()
        
        if "#" in direccion and "-" in direccion and len(direccion) > 10:
            return direccion
        else:
            print("Dirección inválida. Debe contener # y -")
            registrar_evento(
                    "WARNING",
                    f"Direccion {direccion} no digitado correctamente"
                )

def validar_tipo():
    estados_validos = ["residente", "administrador"]

    while True:
        estado = input("Ingrese el estado (Residente/Administrador): ").lower()
        if estado in estados_validos:
            return estado.capitalize()
        else:
            print("Estado inválido. Opciones válidas:")
            print(", ".join(estados_validos))
            registrar_evento(
                    "WARNING",
                    f"Estado {estado} no digitado correctamente"
                )
            
def validar_tipo_provisoria():
    estados_validos = ["administrador"]

    while True:
        estado = input("Ingrese el estado (Administrador): ").lower()
        if estado in estados_validos:
            return estado.capitalize()
        else:
            print("Estado inválido. Opciones válidas:")
            print(", ".join(estados_validos))
            registrar_evento(
                    "WARNING",
                    f"Estado {estado} no digitado correctamente"
                )

def gestion_usuarios1(datos1):

    while True:
        print("""
=============================================
            GESTION DE USUARIOS
=============================================
1. Agregar usuario
2. Listar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
6. Gurdar datos y salir al menu principal
------------------------------------------
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":    
            crear_usuario(datos1)
        elif opcion == "2":
            listar_usuarios(datos1)
        elif opcion == "3":
            buscar_usuario(datos1)
        elif opcion == "4":
            actualizar_usuario(datos1)
        elif opcion == "5":
            eliminar_usuario(datos1)
        elif opcion == "6":
            guardar_datos1(datos1)
            print("Datos guardados. Saliendo ... \n\n")
            break
        else:
            print("Opcion inválida. Digíte un número del 1 al 6")
        input("Presione cualquier tecla para continuar")

def crear_usuario(datos1):
    print("==========================\nDIGITACIÓN DE USUARIOS\n==========================")
    id_vecino = validar_usuario(datos1)
    nombre_vecino = validar_nombres("Ingrese el nombre del usuario: ")
    apellido_vecino = validar_nombres("Ingrese el apellido del usuario: ")
    telefono_vecino = validar_tel("Ingrese el telefono del usuario: ")
    direccion_vecino = validar_dire("Ingrese la direccion del usuario: ")
    tipo_vecino = validar_tipo()

    datos1[id_vecino] = {
        "Nombre": nombre_vecino,
        "Apellido": apellido_vecino,
        "Telefono": int(telefono_vecino),
        "Direccion": direccion_vecino,    
        "Tipo" : tipo_vecino
    }

    print("\nUsuario agregado correctamente")
    registrar_evento(
                    "INFO",
                    f"ID {id_vecino} de usuario agregado correctamente"
                )

def listar_usuarios(datos1):
    if not datos1:
        print("No hay usuarios registrados.")
        return

    print("=======================\nLISTADO DE USUARIOS\n=======================")    
    for id_usuario, keys  in datos1.items():
        print(f"\nUsuario con ID: {id_usuario}")
        for key, valor in keys.items():
            print(f"-{key} -> {valor}")
        print(f"{'-'*30}\n")
    registrar_evento(
                    "INFO",
                    f"Listado de usuario consultado"
                )

def buscar_usuario(datos1):
    if not datos1:
        print("El inventario está vacío. No hay usuarios registrados.")
        return
    
    print("======================\nBÚSQUEDA DE USUARIO\n======================")
    id_usuario = validar_id(datos1)

    producto = datos1[id_usuario]
    print(f"\nUsuario con ID: {id_usuario}")
    for key, valor in producto.items():
        print(f"-{key} -> {valor}")
    print(f"{'-'*50}\n")
    registrar_evento(
                    "INFO",
                    f"Busqueda de usuario consultado"
                )

def actualizar_usuario(datos1):
    if not datos1:
        print("El inventario está vacío. No hay usuarios para actualizar.")
        return
    
    print("==========================\nACTUALIZACIÓN DE USUARIO\n==========================")
    id_usuario = validar_id(datos1)

    print(f"Nombre ({datos1[id_usuario]['Nombre']}): ")
    nombre = validar_nombres("Ingrese el nuevo nombre: ")
    print(f"Apellido ({datos1[id_usuario]['Apellido']}): ")
    apellido = validar_nombres("Ingrese el nuevo apellido: ")
    print(f"Telefono ({datos1[id_usuario]['Telefono']}): ")
    telefono = validar_tel("Ingrese el nuevo telefono: ")
    print(f"Direccion ({datos1[id_usuario]['Direccion']}): ")
    direccion = validar_dire("Ingrese la nueva direccion: ")
    print(f"Tipo ({datos1[id_usuario]['Tipo']}): ")
    tipo = validar_tipo()

    if nombre:
        datos1[id_usuario]["Nombre"] = nombre
    if apellido:
        datos1[id_usuario]["Apellido"] = apellido
    if telefono:
        datos1[id_usuario]["Telefono"] = int(telefono)
    if direccion:
        datos1[id_usuario]["Direccion"] = direccion
    if tipo:
        datos1[id_usuario]["Tipo"] = tipo
    
    print("Usuario actualizado.")
    registrar_evento(
                    "INFO",
                    f"ID {id_usuario} de usuario actualizado"
                )

def eliminar_usuario(datos1):
    if not datos1:
        print("El inventario está vacío. No hay usuarios para eliminar.")
        return
    
    print("==========================\nELIMINACIÓN DE USUARIO\n==========================")
    id_usuario = validar_id(datos1)
    
    persona = datos1[id_usuario]
    print("\nUsuario a eliminar:")
    print(f"ID: {id_usuario}")
    print(f"Nombre: {persona['Nombre']}")
    print(f"Apellido: {persona['Apellido']}")
    print(f"Telefono: {persona['Telefono']}")
    print(f"Direccion: {persona['Direccion']}")
    print(f"Tipo: {persona['Tipo']}")
    
    while True:
        confirmacion = input("\n¿Está seguro que desea eliminar a este usuario? \nPresione S para confirmar o N  para cancelar: ").lower()
        if confirmacion == 's':
            del datos1[id_usuario]
            print(f"\nEl usuario con ID {id_usuario} ha sido eliminado")
            registrar_evento(
                    "INFO",
                    f"ID {id_usuario} de usuario eliminado"
                )

            break
        elif confirmacion == 'n': 
            print("\nOperación cancelada. El usuario no fue eliminado.")
            registrar_evento(
                    "INFO",
                    f"ID {id_usuario} de usuario no eliminado, por decision del administrador"
                )

            break
        else:
            print("\nNo digito correctamente las opciones")
            registrar_evento(
                    "INFO",
                    f"Opcion {confirmacion} de decision no digitada correctamente"
                )
    
def crear_usuario_provisional(datos1):
    print("====================================\nDIGITACIÓN DE USUARIO PROVISIONAL\n====================================")
    id_vecino = validar_usuario(datos1)
    nombre_vecino = validar_nombres("Ingrese el nombre del usuario: ")
    apellido_vecino = validar_nombres("Ingrese el apellido del usuario: ")
    telefono_vecino = validar_tel("Ingrese el telefono del usuario: ")
    direccion_vecino = validar_dire("Ingrese la direccion del usuario: ")
    tipo_vecino_provisoria = validar_tipo_provisoria()

    datos1[id_vecino] = {
        "Nombre": nombre_vecino,
        "Apellido": apellido_vecino,
        "Telefono": int(telefono_vecino),
        "Direccion": direccion_vecino,    
        "Tipo" : tipo_vecino_provisoria
    }

    print("\nUsuario agregado correctamente")
    registrar_evento(
                    "INFO",
                    f"ID {id_vecino} de usuario agregado correctamente"
                )