"""15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales."""
radio = float(input("Introduce el valor del radio del cilindro: "))
altura = float(input("Introduce el valor de la altura del cilindro: "))
area = 2 * 3.14159 * radio * (radio + altura)
volumen = 3.14159 * (radio ** 2) * altura
#Seguidamente, mostramos se muestran los resultados con 2 decimales
print(f"El área es: {round(area, 2)}")
print(f"El volumen es: {round(volumen, 2)}")