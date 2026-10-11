"""9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos 
y las horas"""
segundos = int(input("Introduce el número de segundos: "))
minutos = segundos / 60
horas = minutos / 60
print(f"El número de minutos es: {round(minutos, 2)} y en horas es: {round(horas, 2)}")