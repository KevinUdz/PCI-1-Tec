# Datos iniciales
productos = {
    "food": [
        {"ID": 1, "Item": "Apple", "Quantity": 25, "Price": 10.00},
        {"ID": 2, "Item": "Banana", "Quantity": 17, "Price": 6.20},
        {"ID": 3, "Item": "Orange", "Quantity": 15, "Price": 7.99},
        {"ID": 4, "Item": "Bread", "Quantity": 23, "Price": 50.00},
        {"ID": 5, "Item": "Milk", "Quantity": 25, "Price": 35.00},
        {"ID": 6, "Item": "Beef", "Quantity": 15, "Price": 130.00}
    ],
    "drinks": [
        {"ID": 7, "Item": "Soda (600 ml)", "Quantity": 20, "Price": 20.00},
        {"ID": 8, "Item": "Juice (960 ml)", "Quantity": 25, "Price": 38.00},
        {"ID": 9, "Item": "Water (1 L)", "Quantity": 30, "Price": 10.00},
        {"ID": 10, "Item": "Coffee (281 gr)", "Quantity": 12, "Price": 32.50},
        {"ID": 11, "Item": "Fuze tea (453 gr)", "Quantity": 17, "Price": 15.00}
    ],
    "snacks": [
        {"ID": 12, "Item": "Chips (160 gr)", "Quantity": 27, "Price": 55.60},
        {"ID": 13, "Item": "Cookies", "Quantity": 20, "Price": 20.50},
        {"ID": 14, "Item": "Nuts", "Quantity": 15, "Price": 40.50},
        {"ID": 15, "Item": "Skittles", "Quantity": 23, "Price": 15.00}
    ]
}

# Inicialización
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
            if producto["ID"] == id_producto:
                encontrado = True
                print(f"Producto encontrado: {producto['Item']} - ${producto['Price']}")
                confirmacion = input("¿Desea agregarlo al carrito? (Si/No): ").strip().lower()
                if confirmacion == 'si':
                    lista_carrito.append({
                        "id": producto["ID"],
                        "nombre": producto["Item"],
                        "cantidad": 1,
                        "precio": producto["Price"]
                    })
                    monto_total += producto["Price"]
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
            if producto["ID"] == id_producto:
                encontrado = True
                for item in lista_carrito:
                    if item["id"] == id_producto:
                        item["cantidad"] += 1
                        monto_total += producto["Price"]
                        monto_total_con_impuestos = monto_total * (1 + impuestos)
                        print(f"Producto agregado. Monto total con impuestos: ${monto_total_con_impuestos:.2f}")
                        return
                print("Producto no está en el carrito. Añadiéndolo primero.")
                lista_carrito.append({
                    "id": producto["ID"],
                    "nombre": producto["Item"],
                    "cantidad": 1,
                    "precio": producto["Price"]
                })
                monto_total += producto["Price"]
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
        if item["id"] == id_producto:
            encontrado = True
            monto_total -= item["precio"]
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
            print(f"ID: {item['id']}, Nombre: {item['nombre']}, Cantidad: {item['cantidad']}, Precio: ${item['precio']}")
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
