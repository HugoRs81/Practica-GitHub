"""27. Mejora el programa anterior para controlar que el valor introducido es una letra y en
caso de introducir un número, aparezca un aviso por pantalla"""

letra = input("Introduce una letra: ")
if letra.isalpha():
    if letra.isupper():
        print("La letra está en mayúscula")
    else:
        print("La letra está en minúscula")
elif letra.isdigit():
    print("El valor introducido es un número")
else:
    print("La letra es mayúscula¿?")