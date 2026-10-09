'''Aplica un 10% de descuento a un producto y después añade un 21% de IVA'''
precio_sin_descuento = float(input("introduce el precio del producto sin descuento: "))
precio_con_descuento = (round (precio_sin_descuento * 0.9 ,2))
precio_con_iva = (round (precio_con_descuento + precio_con_descuento* 0.21 ,2))
print (f" el precio con descuento es: {precio_con_descuento}, con iva es: {precio_con_iva} ")