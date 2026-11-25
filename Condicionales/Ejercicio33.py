"""33. Programa un código que permita contar el número de vocales de la siguiente frase: No
hay mal que dure cien años. Que aparezcan el numero de a, e, i, o, u."""

frase = "No hay mal que dure cien años."
vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for letra in frase:
    if letra in vocales:
        vocales[letra] += 1
for vocal, cantidad in vocales.items():
    print(f"El número de {vocal} es {cantidad}.")

#Hecho con IA, no lo entiendo muy bien.