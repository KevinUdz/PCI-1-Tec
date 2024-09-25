# Optimización inicial: creamos un diccionario que nos permita acceder rápidamente a los productos por su ID.
productos_por_id = {producto["ID"]: producto for categoria in productos.values() for producto in categoria}

# Función para ingresar un producto al carrito
def ingresar_producto():
    global monto_total
    id_producto = int(input("Ingrese el ID del producto: "))

    # Verificamos si el ID del producto existe
    if id_producto in productos_por_id:
        producto = productos_por_id[id_producto]  # Obtenemos el producto directamente del diccionario
        print(f"Producto encontrado: {producto['Item']} - ${producto['Price']}")
        

        confirmacion = input("¿Desea agregarlo al carrito? (Si/No): ").strip().lower()
        if confirmacion == 'si':

            # Agregamos el producto al carrito
            lista_carrito.append({
                "id": producto["ID"],
                "nombre": producto["Item"],
                "cantidad": 1,
                "precio": producto["Price"]
            })
            monto_total += producto["Price"]  # Sumamos el precio al monto total
            monto_total_con_impuestos = monto_total * (1 + impuestos)  # Calculamos el total con impuestos
            print(f"Producto agregado. Monto total con impuestos: ${monto_total_con_impuestos:.2f}")
    else:
        print("Producto no encontrado.")  

# Función para agregar otro producto, similar a ingresar_producto, pero manejamos cantidades
def agregar_otro_producto():
    global monto_total
    id_producto = int(input("Ingrese el ID del producto: "))  # Pedimos el ID del producto
    
    # Verificamos si el ID existe en el diccionario
    if id_producto in productos_por_id:
        # Recorremos el carrito para verificar si ya existe el producto
        for item in lista_carrito:
            if item["id"] == id_producto:
                item["cantidad"] += 1  # Aumentamos la cantidad si el producto ya está en el carrito
                monto_total += productos_por_id[id_producto]["Price"]  # Sumamos el precio del producto
                monto_total_con_impuestos = monto_total * (1 + impuestos)
                print(f"Producto agregado. Monto total con impuestos: ${monto_total_con_impuestos:.2f}")
                return
        
        # Si el producto no está en el carrito, lo agregamos
        print("Producto no está en el carrito. Añadiéndolo primero.")
        ingresar_producto()  # Reutilizamos la función de agregar producto por primera vez
    else:
        print("Producto no encontrado.")

# Función para quitar un producto del carrito
def quitar_producto():
    global monto_total
    id_producto = int(input("Ingrese el ID del producto a quitar: "))  # Pedimos el ID del producto
    
    # Recorremos el carrito en busca del producto
    for item in lista_carrito:
        if item["id"] == id_producto:
            monto_total -= item["precio"] * item["cantidad"]  # Restamos el total de ese producto del monto
            lista_carrito.remove(item)  # Lo eliminamos del carrito
            print(f"Producto eliminado. Monto total actualizado: ${monto_total * (1 + impuestos):.2f}")
            return
    
    print("Producto no encontrado en el carrito.")  # Si el producto no estaba en el carrito

# Función para mostrar el contenido del carrito
def ver_carrito():
    if not lista_carrito:
        print("El carrito está vacío.")  # Si no hay productos
    else:
        print("\n--- Carrito ---")
        # Recorremos e imprimimos cada producto en el carrito
        for item in lista_carrito:
            print(f"ID: {item['id']}, Nombre: {item['nombre']}, Cantidad: {item['cantidad']}, Precio: ${item['precio']}")
        print(f"Monto total: ${monto_total * (1 + impuestos):.2f}")  # Mostramos el monto total con impuestos

# Ciclo principal para interactuar con el usuario
def main():
    while True:
        opcion = mostrar_menu()  # Mostramos el menú y pedimos la opción
        
        # Según la opción seleccionada, llamamos a la función correspondiente
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
            print("Opción no válida. Intente de nuevo.")  # Manejo de opción incorrecta

if __name__ == "__main__":
    main()
