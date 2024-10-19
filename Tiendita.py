# Inicio con una matriz que me ayudara a guardar todos los productos de mi tiendita
PRODUCTOS = {
    "Comida": [
        [1, "Manzana", 25, 10.00],
        [2, "Platano", 17, 6.20],
        [3, "Naranja", 15, 7.99],
        [4, "Pan", 23, 50.00],
        [5, "Carne", 15, 130.00]
    ],
    "Bebidas": [
        [6, "Soda (600 ml)", 20, 20.00],
        [7, "Jugo (960 ml)", 25, 38.00],
        [8, "Agua (1 L)", 30, 10.00],
        [9, "Café (281 gr)", 12, 32.50],
        [10, "Leche", 25, 35.00],
        [11, "Fuze tea (453 gr)", 17, 15.00]
    ],
    "snacks": [
        [12, "Papas (160 gr)", 27, 55.60],
        [13, "Galletas", 20, 20.50],
        [14, "Nueces", 15, 40.50],
        [15, "Skittles", 23, 15.00]
    ]
}

# Agrego el carrito de compras virtual para que las cosas que el usuario eliga se vayan almacenando en ese lugar
lista_carrito = []
monto_total = 0.0
IMPUESTOS = 0.15

def mostrar_menu():
    # Muestro en pantalla las opciones que el usario tiene para escoger y lograr tener una mejor interaccion con el progama
    print("\n--- Menú Principal ---")
    print("1. Ingresar producto")
    print("2. Agregar otro producto")
    print("3. Quitar producto")
    print("4. Ver carrito")
    print("5. Finalizar compra")
    print("6. Salir")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Por favor, elija una opción válida entre 1 y 6.")
        except ValueError:
            print("Error: Ingrese un número válido.")

def ingresar_producto():
    # Defino lo que es la variable de "ingresar_producto"
    global monto_total
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    encontrado = False
    for categoria in PRODUCTOS.values():
        for producto in categoria:
            if producto[0] == id_producto:
                encontrado = True
                print(f"Producto encontrado: {producto[1]} - ${producto[3]:.2f}")
                confirmacion = input("¿Desea agregarlo al carrito? (Si/No): ").strip().lower()
                if confirmacion == 'si':
                    lista_carrito.append([producto[0], producto[1], 1, producto[3]])
                    monto_total += producto[3]
                    print(f"Producto agregado. Monto total con impuestos: ${monto_total * (1 + IMPUESTOS):.2f}")
                return
    if not encontrado:
        print("Producto no encontrado.")

def agregar_otro_producto():
    # Defino esta variable para que el usario pueda agregar mas cosas a su lista de compras
    global monto_total
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    for categoria in PRODUCTOS.values():
        for producto in categoria:
            if producto[0] == id_producto:
                for item in lista_carrito:
                    if item[0] == id_producto:
                        item[2] += 1
                        monto_total += producto[3]
                        print(f"Producto agregado. Monto total con impuestos: ${monto_total * (1 + IMPUESTOS):.2f}")
                        return
                print("Producto no está en el carrito. Añadiéndolo primero.")
                lista_carrito.append([producto[0], producto[1], 1, producto[3]])
                monto_total += producto[3]
                print(f"Producto agregado. Monto total con impuestos: ${monto_total * (1 + IMPUESTOS):.2f}")
                return
    print("Producto no encontrado.")

def quitar_producto():
    # Esta variable permite eliminar un producto que el usario haya elegido ya sea por error o por que ya no lo quiso
    global monto_total
    try:
        id_producto = int(input("Ingrese el ID del producto a quitar: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    encontrado = False
    for item in lista_carrito:
        if item[0] == id_producto:
            encontrado = True
            monto_total -= item[3]
            lista_carrito.remove(item)
            print(f"Producto eliminado. Monto total actualizado: ${monto_total * (1 + IMPUESTOS):.2f}")
            return
    if not encontrado:
        print("Producto no encontrado en el carrito.")

def ver_carrito():
    # La variable muestra la cuenta final del usario asi como los productos que eligio
    if not lista_carrito:
        print("El carrito está vacío.")
    else:
        print("\n--- Carrito ---")
        for item in lista_carrito:
            print(f"ID: {item[0]}, Nombre: {item[1]}, Cantidad: {item[2]}, Precio: ${item[3]:.2f}")
        print(f"Monto total con impuestos: ${monto_total * (1 + IMPUESTOS):.2f}")

def finalizar_compra():
    # Esta variable finaliza al pagar la cuenta y despues de esto borra todo lo que el usario habia puesto en su carrito
    global monto_total
    monto_total_con_impuestos = monto_total * (1 + IMPUESTOS)
    print(f"\nMonto total a pagar: ${monto_total_con_impuestos:.2f}")
    ver_carrito()
    confirmacion_pago = input("¿Desea confirmar el pago? (Si/No): ").strip().lower()
    if confirmacion_pago == 'si':
        lista_carrito.clear()
        monto_total = 0.0
        print("¡Gracias por su compra!, buen dia")
    else:
        print("Compra cancelada.")

def main():
    # Esta función es la principal ua que controla todo el flujo del programa
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

if __name__ == "__main__":
    main()
