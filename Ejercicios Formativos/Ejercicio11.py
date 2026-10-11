"""11. Realiza un programa que introduciendo el valor del lado de un cuadrado nos devuelva 
por pantalla en el área y el perímetro."""
lado = float(input("Introduce el valor del lado del cuadrado: "))
area = lado ** 2
perimetro = lado * 4
print(f"El área es: {area}")
print(f"El perímetro es: {perimetro}")