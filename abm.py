# Base de datos de inventario como un diccionario
inventario = {}

def agregar_producto():
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad en stock: "))
    inventario[producto] = cantidad
    print(f"{producto} ha sido agregado al inventario con una cantidad de {cantidad}.")

def actualizar_stock():
    producto = input("Nombre del producto a actualizar: ")
    if producto in inventario:
        nueva_cantidad = int(input("Nueva cantidad en stock: "))
        inventario[producto] = nueva_cantidad
        print(f"Cantidad de {producto} ha sido actualizada a {nueva_cantidad}.")
    else:
        print(f"{producto} no se encuentra en el inventario.")

def eliminar_producto():
    producto = input("Nombre del producto a eliminar: ")
    if producto in inventario:
        del inventario[producto]
        print(f"{producto} ha sido eliminado del inventario.")
    else:
        print(f"{producto} no se encuentra en el inventario.")

def mostrar_inventario():
    print("Inventario:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

while True:
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Actualizar stock")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4/5): ")
    
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        actualizar_stock()
    elif opcion == '3':
        eliminar_producto()
    elif opcion == '4':
        mostrar_inventario()
    elif opcion == '5':
        print("Gracias por usar el sistema de gestión de inventario.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5).")
