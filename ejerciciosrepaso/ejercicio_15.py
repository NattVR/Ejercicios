"""Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no"""

cadena_usuario = input("Ingrese una cadena de texto:")
cadena_limpia = cadena_usuario.replace(" ", "")

if cadena_limpia == cadena_limpia[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
