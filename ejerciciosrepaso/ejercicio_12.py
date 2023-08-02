"""Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for."""
import random
largo_lista = int(input("Ingrese la longitud de la lista:"))

for i in range(largo_lista):
    numero = random.randint(0, 10)
    print(numero)
