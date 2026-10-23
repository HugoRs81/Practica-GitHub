"""10. Introduce por teclado dos números y muestre por pantalla la siguiente información: 
cociente, resto y si el dividendo es par o impar."""
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
cociente = num1 / num2
resto = num1 % num2
if num1 % 2 == 0: par_nopar = "par"
else: par_nopar = "impar"

"""Luego de las operaciones se muestran los resultados"""
print(f"El cociente es: {cociente}")
print(f"El resto es: {resto}")
print(f"El dividendo es: {par_nopar}")