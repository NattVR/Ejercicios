""" Crear un programa que calcule la suma de los números en una lista dada"""
def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma+= lista[i]
    return suma

lista=[4,6,8,9,12,23,45,56,78,90,123]
suma_total=suma_lista(lista)
print(suma_total)
