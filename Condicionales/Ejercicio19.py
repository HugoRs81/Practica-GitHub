"""19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
iguales """
num1 = int(input("introduce un número: "))
num2 = int(input("introduce otro número: "))
if num1 > num2:
    print(f" {num1} es mayor que {num2}")
if num2 > num1:
    print(f"{num2} es mayor que {num1}")
if num1 == num2:
    print(f"{num1} es igual a {num2}")