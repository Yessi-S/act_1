# Inicializo el diccionario de inventario
inventory = {}
# Inicializo variable de control
var_control = True
while var_control:
    # Mostrar el menú de opciones
    print("Menú de Inventario")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    option = input("Seleccione una opción: ")

    if option == "1":
        # Agregar un nuevo producto al inventario
        name = input("Ingrese el nombre del producto: ")
        # Normalizo el nombre en minúsculas
        name=name.lower()
        quantity = int(input("Ingrese la cantidad del producto: "))
        if name in inventory:
            # Si el producto ya existe, sumar la cantidad al inventario
            inventory[name] += quantity
            print(f"Cantidad de '{name}' actualizada a {inventory[name]}.")
        else:
            # Si el producto no existe, agregarlo al inventario
            inventory[name] = quantity
            print(f"Producto '{name}' agregado con cantidad {quantity}.")

    elif option == "2":
        # Eliminar un producto existente del inventario
        name = input("Ingrese el nombre del producto a eliminar: ")
        if name in inventory:
            quantity = int(input("Ingrese la cantidad a eliminar: "))
            if quantity >= inventory[name]:
                # Si la cantidad a eliminar es mayor o igual a la cantidad existente, eliminar el producto
                del inventory[name]
                print(f"Producto '{name}' eliminado del inventario.")
            else:
                # Si la cantidad a eliminar es menor, reducir la cantidad en el inventario
                inventory[name] -= quantity
                print(f"Cantidad de '{name}' actualizada a {inventory[name]}.")
        else:
            # Si el producto no existe, mostrar un mensaje de advertencia
            print("El producto no existe en el inventario.")

    elif option == "3":
        # Mostrar el inventario actual
        if not inventory:
            # Si el inventario está vacío, mostrar un mensaje
            print("El inventario está vacío.")
        else:
            # Mostrar el nombre y la cantidad de cada producto en el inventario
            print("Inventario actual:")
            for name, quantity in inventory.items():
                print(f"{name}: {quantity}")

    elif option == "4":
        # Salir del programa
        print("Saliendo del programa.")
        var_control = False

    else:
        # Si la opción no es válida, mostrar un mensaje de advertencia
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
    print()