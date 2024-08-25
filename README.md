Mi proyecto se basa en una "tiendita" en línea donde los usuarios pueden explorar diferentes categorías como comida, bebidas y snacks. A través de esta plataforma, los consumidores pueden seleccionar lo que necesitan y recibir un precio exacto de todo lo que han escogido. Este proyecto es útil porque ahorra tiempo al usuario al eliminar la necesidad de desplazarse físicamente a una tienda, permitiéndole realizar sus compras desde cualquier lugar y en cualquier momento.

Lo que hace que esta "tiendita" sea especialmente interesante es su diseño orientado a la comodidad y eficiencia del usuario. Al ofrecer una experiencia de compra organizada por categorías claras, facilita la exploración y comparación de productos. La plataforma no solo brinda comodidad, sino también una experiencia de compra segura y transparente, al garantizar que el precio total se muestre con precisión antes de completar la compra.

Además, al ser un servicio en línea disponible las 24 horas del día, se adapta perfectamente a los estilos de vida modernos, donde el tiempo es un recurso valioso. La flexibilidad para hacer compras en cualquier momento, combinada con la simplicidad de la interfaz, asegura que los usuarios puedan realizar sus compras de manera rápida y sin complicaciones.




### Food
| ID | Item | Quantity | Price |
| --- | --- | --- | --- |
| 1 | Apple | 25 | $10.00 |
| 2 | Banana | 17 | $6.20 |
| 3 | Orange | 15 | $7.99 |
| 4 | Bread | 23 | $50.00 |
| 5 | Milk | 25 | $35.00 |
| 6 | beef | 15 | $130.00 |





### Drinks
| ID | Item | Quantity | Price |
| --- | --- | --- | --- |
| 7 | Soda (600 ml)| 20 | $20.00 |
| 8 | Juice (960 ml)| 25 | $38.00 |
| 9 | Water (1 L)| 30 | $10.00 |
| 10 | Coffee (281 gr)| 12 | $32.50 |
| 11| Fuze tea (453 gr)| 17 | $15.00 |





### Snacks
| ID | Item | Quantity | Price |
|--- | --- | --- | --- |
| 12 | Chips (160 gr)| 27 | $55.60 |
| 13 | Cookies| 20 | $20.50 |
| 14| Nuts| 15 | $40.50 |
| 15 | Skittles| 23 | $15.00 |



## Entrada

1. Lista_carrito como lista vacia de diccionarios (Cada diccionario con campos id (int), nombre (string), cantidad (int), precio (float))
2. Monto_total como 0.0 (float)
3. Impuestos como 0.15 (float) (15% )
         

## Proceso

**Mostrar menú principal**
4. Mientars el usuario no elija salir:
4.1 Mostrar opciónes:
1. Ingresar producto 
2. Agregar otro producto
3. Quitar producto
4. Ver carrito 
5. Finalizar compra 
6. Salir
4.2 Leer opcion del usuario (int)

**Si la opcion es "ingresar producto":**
5. Leer id-producto (int)
5.1 Mostrar nombre (string) y precio (float) del producto
5.2 Leer confirmación (string) (Si/No)
**Si confirmacion es "si":**
5.4 Agregar producto a Lista_carrito
5.5 Sumar precio (float) al Monto_total
5.6 Actualizar Monto_total con impuestos
**Si no:**
5.7 Regresar al menu principal

**Si la opción es "agregar otro producto":**
6. Leer nuevo id-producto (int)
6.1 Verificar si el produto existe
**Si existe:**
6.2 Añadir producto a Lista_carrito
6.3 Sumar precio (float) a Monto_total
6.4 Actualizar Monto_total con impuestos
**Si no existe:**
6.5 Mostrar mensaje de producto no encontrado (string)

**Si la opción es "quitar_producto":**
7. Leer id_producto (int) que desea quitar
7.1 Buscar producto en Lista_carrito
**Si el producto se encuentra:**
7.2 Eliminar producto de Lista_carrito
7.3 Restar precio (float) del producto en Monto_total
**Si no se encuentra:**
7.4 Mostrar mensaje de producto no encontrado (string)

**Si la opción es ver_carrito:**
8. Mostrar todos los productos en Lista_carrito (lista de diccionarios)
8.1 Mostrar Monto_total (float)

**Si la opción es finalizar_compra":**
9. Calcular Monto_toal con impuestos
9.1 Mostrar Monto_total (float) a pagar 
9.2 Mostrar Lista_carrito (lista de diccionario)
9.3 Leer confirmación de pago (string) (Si/No)
**Si el usuario realizo el pago:**
9.4 Vaciar Lista_carrito (lista vacia de diccionarios)
9.5 Mostrar mensaje de agradecimiento (string)
**Si el usuario no realiza el pago:**
9.6 Volver al menu principal

**Si la opción es "salir":**
10. Terminar programa


## Salida
11. Detalles del carrito (lista de productos con sus precios y cantidades)
11.1 Monto total después de impuestos (float)
11.2 Mensaje de agradecimiento después del pago (string)
