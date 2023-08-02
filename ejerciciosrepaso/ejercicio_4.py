"""Escribir un programa que determine si un número dado es par o impar"""
numero = int(input("Ingrese un numero"))
residuo = numero % 2
if residuo == 0:
    print("El número es par")
else:
    print("El número es impar")
