# Datos iniciales en formato de matriz
productos = {
    "food": [
        [1, "Apple", 25, 10.00],
        [2, "Banana", 17, 6.20],
        [3, "Orange", 15, 7.99],
        [4, "Bread", 23, 50.00],
        [5, "Milk", 25, 35.00],
        [6, "Beef", 15, 130.00]
    ],
    "drinks": [
        [7, "Soda (600 ml)", 20, 20.00],
        [8, "Juice (960 ml)", 25, 38.00],
        [9, "Water (1 L)", 30, 10.00],
        [10, "Coffee (281 gr)", 12, 32.50],
        [11, "Fuze tea (453 gr)", 17, 15.00]
    ],
    "snacks": [
        [12, "Chips (160 gr)", 27, 55.60],
        [13, "Cookies", 20, 20.50],
        [14, "Nuts", 15, 40.50],
        [15, "Skittles", 23, 15.00]
    ]
}

# Carrito de compras en formato de matriz
lista_carrito = []
monto_total = 0.0
impuestos = 0.15

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Ingresar producto")
    print("2. Agregar otro producto")
    print("3. Quitar producto")
    print("4. Ver carrito")
    print("5. Finalizar compra")
    print("6. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def ingresar_producto():
    global monto_total
    id_producto = int(input("Ingrese el ID del producto: "))
    encontrado = False

    for categoria in productos.values():
        for producto in categoria:
            if producto[0] == id_producto:
                encontrado = True
                print(f"Producto encontrado: {producto[1]} - ${producto[3]}")
                confirmacion = input("¿Desea agregarlo al carrito? (Si/No): ").strip().lower()
                if confirmacion == 'si':
                    lista_carrito.append([producto[0], producto[1], 1, producto[3]])
                    monto_total += producto[3]
                    monto_total_con_impuestos = monto_total * (1 + impuestos)
                    print(f"Producto agregado. Monto total con impuestos: ${monto_total_con_impuestos:.2f}")
                break
        if encontrado:
            break
    if not encontrado:
        print("Producto no encontrado.")

def agregar_otro_producto():
    global monto_total
    id_producto = int(input("Ingrese el ID del producto: "))
    encontrado = False

    for categoria in productos.values():
        for producto in categoria:
            if producto[0] == id_producto:
                encontrado = True
                for item in lista_carrito:
                    if item[0] == id_producto:
                        item[2] += 1
                        monto_total += producto[3]
                        monto_total_con_impuestos = monto_total * (1 + impuestos)
                        print(f"Producto agregado. Monto total con impuestos: ${monto_total_con_impuestos:.2f}")
                        return
                print("Producto no está en el carrito. Añadiéndolo primero.")
                lista_carrito.append([producto[0], producto[1], 1, producto[3]])
                monto_total += producto[3]
                monto_total_con_impuestos = monto_total * (1 + impuestos)
                print(f"Producto agregado. Monto total con impuestos: ${monto_total_con_impuestos:.2f}")
                return
        if encontrado:
            break
    if not encontrado:
        print("Producto no encontrado.")

def quitar_producto():
    global monto_total
    id_producto = int(input("Ingrese el ID del producto a quitar: "))
    encontrado = False

    for item in lista_carrito:
        if item[0] == id_producto:
            encontrado = True
            monto_total -= item[3]
            lista_carrito.remove(item)
            print(f"Producto eliminado. Monto total actualizado: ${monto_total * (1 + impuestos):.2f}")
            return
    if not encontrado:
        print("Producto no encontrado en el carrito.")

def ver_carrito():
    if not lista_carrito:
        print("El carrito está vacío.")
    else:
        print("\n--- Carrito ---")
        for item in lista_carrito:
            print(f"ID: {item[0]}, Nombre: {item[1]}, Cantidad: {item[2]}, Precio: ${item[3]}")
        print(f"Monto total: ${monto_total * (1 + impuestos):.2f}")

def finalizar_compra():
    global monto_total
    monto_total_con_impuestos = monto_total * (1 + impuestos)
    print(f"\nMonto total a pagar: ${monto_total_con_impuestos:.2f}")
    ver_carrito()
    confirmacion_pago = input("¿Desea confirmar el pago? (Si/No): ").strip().lower()
    if confirmacion_pago == 'si':
        lista_carrito.clear()
        monto_total = 0.0
        print("¡Gracias por su compra!")
    else:
        print("Compra cancelada.")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            ingresar_producto()
        elif opcion == 2:
            agregar_otro_producto()
        elif opcion == 3:
            quitar_producto()
        elif opcion == 4:
            ver_carrito()
        elif opcion == 5:
            finalizar_compra()
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
