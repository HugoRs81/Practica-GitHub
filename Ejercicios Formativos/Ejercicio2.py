"""Ejercicio2"""
codigo = input("introduce un codigo: ")
codigo = codigo.strip()
mayusculas = codigo.upper()
minusculas= codigo.lower()
longitud = len(codigo)
guion = codigo.count("-")
codigo = codigo.replace("-", "*")