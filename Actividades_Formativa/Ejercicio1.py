"""Una empresa de mensajería necesita calcular la distancia entre dos puntos de un mapa 
para organizar sus entregas."""

CoordenadaX = float(input("introduce la coordenada x de el primer punto: "))
CoordenadaY = float(input("introduce la coordenada y de el primer punto: "))
CoordenadaX2 = float(input("introduce la coordenada x de el segundo punto: "))
CoordenadaY2 = float(input("introduce la coordenada y de el segundo punto: "))
distancia = ((CoordenadaX2 - CoordenadaX) ** 2 + (CoordenadaY2 - CoordenadaY) ** 2) ** 0.5
print(f"La distancia entre los dos puntos es: {distancia:.2f}")