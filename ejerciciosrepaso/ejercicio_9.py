"""Crear un programa que genere una matriz de números y la imprima en pantalla."""
import random
filas = int(input("Ingrese el número de filas:"))
columnas = int(input("Ingrese el número de columnas:"))
matriz = []

for i in range(filas):
    fila = []
    for k in range(columnas):
        numero = random.randint(0, 99)
        fila.append(numero)
    matriz.append(fila)
print(matriz)
