"""16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
(raíz y división)."""
import math
número = float(input("Introduce un número: "))
raiz_quadrada = math.sqrt (número)
division = raiz_quadrada // 2
print(f"La raíz cuadrada de {número} es: {raiz_quadrada}")
print(f"El resultado entero es: {division}")