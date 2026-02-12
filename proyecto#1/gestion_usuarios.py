"""
id, nombres, apellidos, teléfono, dirección y tipo de usuario (ej. residente, administrador).
Operaciones: crear, listar, buscar, actualizar y eliminar usuarios.
"""
def validar_id():
    while True:
        id_vecino = input("Ingrese el ID del vecino: ").strip()
        
        if not id_vecino:
            print("Error: El ID no puede estar vacío.")
        
        elif not id_vecino.isdigit():
            print("Error: El ID solo debe contener números.")
        
        else:
            return id_vecino

def validar_nombres(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.replace(" ", "").isalpha():
            return texto.title()
        else:
            print("Error: Solo se permiten letras y espacios.")


def validar_tel(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and len(valor) == 10:
            return int(valor)
        else:
            print("Error: Debe ingresar un número válido con 10 digitos.")

def validar_dire(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.replace(" ", "").isalpha():
            return texto.title()
        else:
            print("Error: Solo se permiten letras y espacios.")

def validar_tipo():
    estados_validos = ["residente", "administrador"]

    while True:
        estado = input("Ingrese el estado (Residente/Administrador): ").lower()
        if estado in estados_validos:
            return estado.capitalize()
        else:
            print("Estado inválido. Opciones válidas:")
            print(", ".join(estados_validos))

from gestion_datos1 import guardar_datos1


def gestion_usuarios1(datos1):

    print("\nGESTION DE HERRAMIENTAS")
    while True:
        print("""
1. Agregar usuario
2. Listar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
6. Gurdar datos y salir al menu principal
--------------------------------
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
    print("\n\n1. Digitizacion de Usuario\n\n")
    id_vecino = validar_id()
    if id_vecino in datos1:
            print("Error: Ese ID ya existe.")
            return
    nombre_vecino = validar_nombres("Ingrese el nombre del vecino: ")
    apellido_vecino = validar_nombres("Ingrese el apellido del vecino: ")
    telefono_vecino = validar_tel("Ingrese el telefono del vecino: ")
    direccion_vecino = validar_dire("Ingrese la direccion del vecino: ")
    tipo_vecino = validar_tipo()

    datos1[id_vecino] = {
        "Nombre": nombre_vecino,
        "Apellido": apellido_vecino,
        "Telefono": int(telefono_vecino),
        "Direccion": direccion_vecino,    
        "Tipo" : tipo_vecino
    }

    print("\nVecino agregado correctamente")

def listar_usuarios(datos1):
    if not datos1:
        print("No hay vecinos registrados.")
        return

    print("\n\n2. Listado de vecinos\n\n")    
    for id_vecino, keys  in datos1.items():
        print(f"\nVecino con ID: {id_vecino}")
        for key, valor in keys.items():
            print(f"-{key} -> {valor}")
        print(f"{'-'*30}\n")

def buscar_usuario(datos1):
    if not datos1:
        print("El inventario está vacío. No hay vecinos para buscar.")
        return
    
    print("\n\n3. Busqueda de Vecinos\n\n")
    id_veci = validar_id()
    if id_veci not in datos1:
            print("Vecino no encontrado.")
            return

    producto = datos1[id_veci]
    print(f"\nVecino con ID: {id_veci}")
    for key, valor in producto.items():
        print(f"-{key} -> {valor}")
    print(f"{'-'*30}\n")

def actualizar_usuario(datos1):
    if not datos1:
        print("El inventario está vacío. No hay vecinos para actualizar.")
        return
    
    print("\n\n4. Actualizacion de Vecino\n\n")
    id_veci = validar_id()
    if id_veci not in datos1:
            print("Vecino no encontrado.")
            return

    print(f"Nombre ({datos1[id_veci]['Nombre']}): ")
    nombre = validar_nombres("Ingrese el nuevo nombre: ")
    print(f"Apellido ({datos1[id_veci]['Apellido']}): ")
    apellido = validar_nombres("Ingrese el nuevo apellido: ")
    print(f"Telefono ({datos1[id_veci]['Telefono']}): ")
    telefono = validar_tel("Ingrese el nuevo telefono: ")
    print(f"Direccion ({datos1[id_veci]['Direccion']}): ")
    direccion = validar_dire("Ingrese la nueva direccion: ")
    print(f"Tipo ({datos1[id_veci]['Tipo']}): ")
    tipo = validar_tipo()

    if nombre:
        datos1[id_veci]["Nombre"] = nombre
    if apellido:
        datos1[id_veci]["Apellido"] = apellido
    if telefono:
        datos1[id_veci]["Telefono"] = int(telefono)
    if direccion:
        datos1[id_veci]["Direccion"] = direccion
    if tipo:
        datos1[id_veci]["Tipo"] = tipo
    
    print("Vecino actualizado.")

def eliminar_usuario(datos1):
    if not datos1:
        print("El inventario está vacío. No hay vecinos para eliminar.")
        return
    
    print("\n\n5. Eliminacion de Vecino\n\n")
    id_veci = validar_id()
    
    if id_veci  not in datos1:
        print(f"No existe un vecino con el ID {id_veci }")
        return
    
    persona = datos1[id_veci]
    print("\nUsuario a eliminar:")
    print(f"ID: {id_veci}")
    print(f"Nombre: {persona['Nombre']}")
    print(f"Apellido: {persona['Apellido']}")
    print(f"Telefono: {persona['Telefono']}")
    print(f"Direccion: {persona['Direccion']}")
    print(f"Tipo: {persona['Tipo']}")
    
    while True:
        confirmacion = input("\n¿Está seguro que desea eliminar a este usuario? \nPresione S para confirmar o N  para cancelar: ").lower()
        if confirmacion == 's':
            del datos1[id_veci]
            print(f"\nEl vecino con ID {id_veci} ha sido eliminado")
            break
        elif confirmacion == 'n': 
            print("\nOperación cancelada. El usuario no fue eliminado.")  
            break
        else:
            print("\nNo digito correctamente las opciones")
