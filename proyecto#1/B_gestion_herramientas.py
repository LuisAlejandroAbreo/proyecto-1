from C_gestion_datos_herramientas import guardar_datos

def validar_id(datos):
    while True:
        id_herramienta = input("Ingrese el ID de la herramienta: ").strip()
        
        if not id_herramienta:
            print("Error: El ID no puede estar vacío.")
        elif not id_herramienta.isdigit():
            print("Error: El ID solo debe contener números.")
        elif id_herramienta not in datos:
            print("Herramienta no encontrada.")
        else:
            return id_herramienta
        
def validar_id2(datos):
    while True:
        id_herramienta = input("Ingrese el ID de la herramienta: ").strip()
        
        if not id_herramienta:
            print("Error: El ID no puede estar vacío.")
        elif not id_herramienta.isdigit():
            print("Error: El ID solo debe contener números.")
        elif id_herramienta in datos:
            print("Error: Ese ID ya existe.")
        else:
            return id_herramienta

def validar_entero_positivo(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and int(valor) >= 0:
            return int(valor)
        else:
            print("Error: Debe ingresar un número entero positivo.")

def validar_decimal_positivo(mensaje):
    while True:
        valor = input(mensaje)
        try:
            valor = float(valor)
            if valor >= 0:
                return valor
            else:
                print("Error: El valor debe ser positivo.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.replace(" ", "").isalpha():
            return texto.title()
        else:
            print("Error: Solo se permiten letras y espacios.")

def validar_estado():
    estados_validos = ["activa", "reparacion", "fuera de servicio"]

    while True:
        estado = input("Ingrese el estado (Activa/Reparacion/Fuera de servicio): ").lower()
        if estado in estados_validos:
            return estado.capitalize()
        else:
            print("Estado inválido. Opciones válidas:")
            print(", ".join(estados_validos))

def gestion_herramientas1(datos):

    print("\nGESTION DE HERRAMIENTAS")
    while True:
        print("""
1. Agregar herramienta
2. Listar herramientas
3. Buscar herramienta
4. Actualizar herramienta
5. Eliminar herramienta
6. Inactivar herramienta
7. Gurdar datos y salir al menu principal
--------------------------------
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":    
            agregar_herramientas(datos)
        elif opcion == "2":
            listar_herramientas(datos)
        elif opcion == "3":
            buscar_herramienta(datos)
        elif opcion == "4":
            actualizar_herramienta(datos)
        elif opcion == "5":
            eliminar_herramienta(datos)
        elif opcion == "6":
            inactivar_herramienta(datos)
        elif opcion == "7":
            guardar_datos(datos)
            print("Datos guardados. Saliendo ... \n\n")
            break
        else:
            print("Opcion inválida. Digíte un número del 1 al 7")
        input("Presione cualquier tecla para continuar")

def agregar_herramientas(datos) :

    print("\n\n1. Digitizacion de Herramienta\n\n")
    id_herramienta = validar_id2(datos)    
    nombre_herramienta = validar_texto("Ingrese el nombre de la herramienta: ")
    categoria_herramienta = validar_texto("Ingrese categoria de la herramienta: ")
    cant_disp_herramienta = validar_entero_positivo("Ingrese la cantidad disponible: ")
    estado_herramienta = validar_estado()
    valor_est_herramienta = validar_decimal_positivo("Ingrese el valor estimado en $: ")

    datos[id_herramienta] = {
        "Nombre": nombre_herramienta,
        "Categoria": categoria_herramienta,
        "Cantidad": int(cant_disp_herramienta),
        "Estado": estado_herramienta,    
        "Valor" : float(valor_est_herramienta)
                }
    
    print("\nHerramienta agregada correctamente")

def listar_herramientas(datos):

    if not datos:
        print("No hay herramientas registradas.")
        return
    
    print("\n\n2. Listado de Herramientas\n\n")    
    for id_herramientas, keys  in datos.items():
        print(f"\nHerramienta con ID: {id_herramientas}")
        for key, valor in keys.items():
            print(f"-{key} -> {valor}")
        print(f"{'-'*30}\n")

def buscar_herramienta(datos):

    if not datos:
        print("El inventario está vacío. No hay herramientas para buscar.")
        return
    
    print("\n\n3. Busqueda de Herramienta\n\n")
    id_herra = validar_id(datos)

    producto = datos[id_herra]
    print(f"\nHerramienta con ID: {id_herra}")
    for key, valor in producto.items():
        print(f"-{key} -> {valor}")
    print(f"{'-'*30}\n")

def actualizar_herramienta(datos):

    if not datos:
        print("El inventario está vacío. No hay herramientas para actualizar.")
        return
    
    print("\n\n4. Actualizacion de Herramienta\n\n")
    id_herra = validar_id(datos)

    print(f"Nombre ({datos[id_herra]['Nombre']}): ")
    nombre = validar_texto("Ingrese el nuevo nombre: ")
    print(f"Categoria ({datos[id_herra]['Categoria']}): ")
    categoria = validar_texto("Ingrese la nueva categoria: ")
    print(f"Cantidad ({datos[id_herra]['Cantidad']}): ")
    cantidad = validar_entero_positivo("Ingrese la nueva cantidad: ")
    print(f"Estado ({datos[id_herra]['Estado']}): ")
    estado = validar_estado()
    print(f"Valor $ ({datos[id_herra]['Valor']}): ")
    valor = validar_decimal_positivo("Ingrese el nuevo valor: ")

    if nombre:
        datos[id_herra]["Nombre"] = nombre
    if categoria:
        datos[id_herra]["Categoria"] = categoria
    if cantidad:
        datos[id_herra]["Cantidad"] = int(cantidad)
    if estado:
        datos[id_herra]["Estado"] = estado
    if valor:
        datos[id_herra]["Valor"] = float(valor)
    
    print("Herramienta actualizada.")

def eliminar_herramienta(datos):

    if not datos:
        print("El inventario está vacío. No hay herramientas para eliminar.")
        return
    
    print("\n\n5. Eliminacion de Herramienta\n\n")
    id_herra = validar_id(datos)
    
    producto = datos[id_herra]
    print("\nHerramienta a eliminar:")
    print(f"ID: {id_herra}")
    print(f"Nombre: {producto['Nombre']}")
    print(f"Categoria: {producto['Categoria']}")
    print(f"Cantidad: {producto['Cantidad']}")
    print(f"Estado: {producto['Estado']}")
    print(f"Valor: {producto['Valor']}")
    
    while True:
        confirmacion = input("\n¿Está seguro que desea eliminar esta herramienta? \nPresione S para confirmar o N  para cancelar: ").lower()
        if confirmacion == 's':
            del datos[id_herra]
            print(f"\nLa herramienta con ID {id_herra} ha sido eliminada")
            break
        elif confirmacion == 'n': 
            print("\nOperación cancelada. La herramienta no fue eliminada.")  
            break
        else:
            print("\nNo digito correctamente las opciones")

def inactivar_herramienta(datos):
   
    if not datos:
        print("El inventario está vacío. No hay herramientas para inactivar.")
        return
    
    print("\n\n6. Inactivacion de Herramienta\n\n")
    id_herra = validar_id(datos)
    if datos[id_herra]["Estado"] == "Inactiva":
        print("La herramienta ya está inactiva.")
        return
    else:
        datos[id_herra]["Estado"] = "Inactiva"
        print("Herramienta inactivada correctamente.")