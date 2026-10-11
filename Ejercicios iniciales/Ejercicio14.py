"""14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el 
resultado a un decimal."""
diametro = float(input("Introduce el valor del diámetro del círculo: "))
radio = diametro / 2
area = 3.14159 * (radio ** 2)
perimetro = 2 * 3.14159 * radio
print(f"El perímetro es: {round(perimetro, 1)}")
print(f"El área es: {round(area, 1)}")