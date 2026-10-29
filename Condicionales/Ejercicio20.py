"""20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
números entre 0 y 10"""
listanumeros = (1,2,3,4,5,6,7,8,9,10)
num1 = float(input("introduce un número: "))
num2 = float(input("introduce otro número: "))
if num1 or num2 != listanumeros:
    print("no esta en la lista de números")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} es igual a {num2}")