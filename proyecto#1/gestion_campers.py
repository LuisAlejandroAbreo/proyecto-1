def gestion_herramientas(datos):


    print("\nGESTION DE HERRAMIENTAS")
    while True:
        print("""
1. Agregar herramienta
2. Listar herramientas
3. Buscar herramienta
4. Actualizar herramienta
5. Eliminar herramienta
6. Inactivar herramienta
7. Salir al menu principal
--------------------------------
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":    
            id_herramienta = input("\nIngrese el id de la herramienta: ")
            nombre_herramienta = input("\nIngrese el nombre de la herramienta: ")
            categoria_herramienta = input("\nIngrese categoria de la herramienta: ")
            cant_disp_herramienta = input("\nIngrese la cantidad disponible de la herramienta: ")
            estado_herramienta = input("\nIngrese el estado de la herramienta: ")
            valor_est_herramienta = input("\nIngrese el valor estimado de la herramienta: ")
            agregar_herramientas(datos, id_herramienta, nombre_herramienta, categoria_herramienta, cant_disp_herramienta, estado_herramienta, valor_est_herramienta)
        elif opcion == "2":
            listar_herramientas(datos)
        elif opcion == "3":
            buscar_herramienta()
        elif opcion == "4":
            actualizar_herramienta(datos)
        elif opcion == "5":
            eliminar_herramienta(datos)
        elif opcion == "6":
            pass
        elif opcion == "7":
            break
        else:
            print("Opcion inválida. Digíte un número del 1 al 7")
        input("Presione cualquier tecla para continuar")

def agregar_herramientas(datos, id_herramienta, nombre_herramienta, categoria_herramienta, cant_disp_herramienta, estado_herramienta, valor_est_herramienta) :

    if id_herramienta in datos:
        print("La Herramienta ya existe.")
        return

    datos[id_herramienta] = {
        "Nombre": nombre_herramienta,
        "Categoria": categoria_herramienta,
        "Cantidad": cant_disp_herramienta,
        "Estado": estado_herramienta,    
        "Valor" : valor_est_herramienta
                }
    
    print("\nHerramienta agregada correctamente")

def listar_herramientas(datos):
    print("\n\n2. Listado de Herramientas\n\n")

    if not datos:
        print("No hay herramientas registradas.")
        return
    
    for id_herramientas, keys  in datos.items():
        print(f"\nHerramienta con ID: {id_herramientas}")
        for key, valor in keys.items():
            print(f"-{key} -> {valor}")
        print(f"{'-'*30}\n")

def buscar_herramienta():
    pass

def actualizar_herramienta(datos):
    print("\n\n4. Actualizacion de Herramienta\n\n")

    if not datos:
        print("El inventario está vacío. No hay herramientas para actualizar.")
        return

    id_herra = input("ID de la herramienta a modificar: ")
    if id_herra not in datos:
        print("Herramienta no encontrada.")
        return

    print("Deje vacío para mantener el valor actual de la herramienta.")
    nombre = input(f"Nombre ({datos[id_herra]['Nombre']}): ")
    categoria = input(f"Categoria ({datos[id_herra]['Categoria']}): ")
    cantidad = input(f"Cantidad ({datos[id_herra]['Cantidad']}): ")
    estado = input(f"Estado ({datos[id_herra]['Estado']}): ")
    valor = input(f"Valor $ ({datos[id_herra]['Valor']}): ")

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
    print("\n\n5. Eliminacion de Herramienta\n\n")

    if not datos:
        print("El inventario está vacío. No hay herramientas para eliminar.")
        return
    
    id_herra = input("Código de la herramienta a eliminar: ")
    
    if id_herra not in datos:
        print(f"No existe una herramienta con el ID {id_herra}")
        return
    
    producto = datos[id_herra]
    print("\nHerramienta a eliminar:")
    print(f"ID: {id_herra}")
    print(f"Nombre: {producto['Nombre']}")
    print(f"Categoria: {producto['Categoria']}")
    print(f"Cantidad: {producto['Cantidad']}")
    print(f"Estado: {producto['Estado']}")
    print(f"Valor: {producto['Valor']}")
    
    confirmacion = input("\n¿Está seguro que desea eliminar esta herramienta? \nPresione S para continuar o cualquier otra letra para cancelar: ").lower()

    if confirmacion == 's':
        del datos[id_herra]
        print(f"\nLa herramienta con con ID {id_herra} ha sido eliminada")    
    else:
        print("\nOperación cancelada. La herramienta no fue eliminada.")