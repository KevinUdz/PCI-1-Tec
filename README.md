### Food
| Item | Quantity | Price |
| --- | --- | --- |
| Apple | 10 | $3.00 |
| Banana | 20 | $32.50 |
| Orange | 15 | $1.50 |
| Bread | 30 | $2.00 |
| Milk | 25 | $3.00 |





### Drinks
| Item | Quantity | Price |
| --- | --- | --- |
| Soda| 10 | $3.00 |
| Juice| 20 | $32.50 |
| Water| 15 | $1.50 |
| Coffee| 30 | $2.00 |
| Tea| 25 | $3.00 |





### Snacks
| Item | Quantity | Price |
| --- | --- | --- |
| Chips| 10 | $3.00 |
| Cookies| 20 | $32.50 |
| Nuts| 15 | $1.50 |
| Candy| 30 | $2.00 |


**Entrada**
Id-producto
Precio-producto
Impuestos
Monto-total
         
  **Proceso**
 1. Usuario ingresa id-producto se despliega el nombre y precio-producto
 2. Si el usuario presiona si, el producto se añade a "lista_carrito" Si no regresa a ingresar un id-de un producto
 2.1 Y el precio-producto se suma al monto-total y el monto-total + impuestos
 3. Si el usuario quiere agregar un producto mas escribe agregar y podrá ingresar otro producto (id_producto)
 3.1. Si el usuario quiere quitar un producto escribe "quitar" y el id-producto que desea quitar
 3.2. Si no despliega "lista_carrito" 
 4. Si el usuario ingresa pagar habra realizado su compra

               
       **Salida**
       1. Lista carrito monto_total


1.  **Inicio del Programa**:
    
    -   El usuario pide al programa mostrar lista de productos.
    - El usuario ingresa el nombre o un identificador de un producto, dicho producto o ID ira almacenandose en una lista 
2.  **Menú Principal**:
    
    -   El usuario ve las siguientes opciones:
        1.  Agregar producto al carrito
        2.  Ver carrito
        3.  Finalizar compra
        4.  Salir
3.  **Agregar Producto al Carrito**:
    
    -   Si el usuario elige agregar un producto, el programa le pide que ingrese el nombre o identificador del producto.
    -   El programa también solicita el precio del producto.
    -   El producto y su precio se agregan a una lista que representa el carrito de compras.
    -   El programa vuelve al menú principal.
4.  **Ver Carrito**:
    
    -   Si el usuario elige ver el carrito, el programa muestra todos los productos que se han agregado al carrito junto con sus precios.
    -   El programa también muestra el total acumulado de los precios de los productos en el carrito.
    -   El programa vuelve al menú principal.
5.  **Finalizar Compra**:
    
    -   Si el usuario elige finalizar la compra, el programa muestra el total a pagar.
    -   El programa muestra un mensaje de agradecimiento por la compra.
    -   El carrito de compras se vacía para estar listo para una nueva compra.
    -   El programa vuelve al menú principal.
6.  **Salir**:
    
    -   Si el usuario elige salir, el programa termina su ejecución.
