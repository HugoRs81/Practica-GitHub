"""22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido.
Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado."""
#En un rango del 0 al 10

nota = float(input("Introduce tu nota: "))

while not 0 <= nota <= 10:
    print("La nota debe estar entre 0 y 10.")
    nota = float(input("Introduce tu nota: "))

if nota >= 5:
    print("Has aprobado")
else:
    print("Has suspendido")

# Editado con IA porque no entendia que le faltaba al código.