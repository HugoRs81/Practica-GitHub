"""28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza
elif."""

letra = input("Introduce una letra: ")
if letra.isalpha():
    if letra.isupper():
        print("La letra está en mayúscula")
    else:
        print("La letra está en minúscula")
elif letra.isdigit():
    print("El valor introducido es un número")
else:
    print("El valor introducido es un símbolo")