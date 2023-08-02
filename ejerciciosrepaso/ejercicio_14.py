""". Escribir una función que calcule la media aritmética de una lista de números."""
import random
def crear_lista(tamano_lista):
    lista = []
    for i in range(tamano_lista):
        numero = random.randint(0, 50)
        lista.append(numero)
    return lista

def calculo(lista):
    suma = 0
    for i in range(len(lista)):
        suma+=lista[i]
    media_aritmetica = suma/len(lista)
    return media_aritmetica

tamano_lista = int(input("Ingrese el tamño de la lista:"))
lista = crear_lista(tamano_lista)
print(lista)
media_aritmetica = calculo(lista)
print(media_aritmetica)
