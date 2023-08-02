""" Crear una función que convierta grados Fahrenheit a grados Celsius"""
def calcular_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 0.5555555556
    return celsius

fahrenheit = float(input("Ingrese la temperatura en fahrenheit:"))
celsius = calcular_celsius(fahrenheit)
print("La temperatura en celsius es:", celsius)
