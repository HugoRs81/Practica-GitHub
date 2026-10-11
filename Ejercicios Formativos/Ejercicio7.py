"""7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
forzar que el resultado de la división tenga 2 decimales?"""
num1= float(print("introduce el primer numero: "))
num2= float(print("introduce el segundo numero: "))
num1= float(input("introduce el primer numero: "))
num2= float(input("introduce el segundo numero: "))
print(f"la suma es: {num1 + num2}")
print(f"la resta es: {num1 - num2}")
print(f"la multiplicacióm es: {num1 * num2}")
print(f"la división es: {round(num1 / num2, 2)}")
print(f"la división entera es: {num1 // num2}")
print(f"el módulo es: {num1 % num2}")
print(f"la poténcia es: {num1 ** num2}") 