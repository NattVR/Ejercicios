"""Crear una función que invierta el orden de los elementos en una lista dada."""
def invertir_lista(lista):
    lista.reverse()
    return lista

lista = [6,8,9,12,23,45,56,78,4,90,123]
lista_invertida = invertir_lista(lista)
print(lista_invertida)
