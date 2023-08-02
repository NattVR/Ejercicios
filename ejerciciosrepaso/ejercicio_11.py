"""Crear un programa que genere una lista de números pares entre 1 y 100"""
import random
lista = []
contador = 0
while contador < 10:
    numero = random.randint(1, 100)
    if numero % 2 == 0:
        lista.append(numero)
        contador+=1
print(lista)

