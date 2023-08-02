""" Escribir una función que calcule el factorial de un número dado."""
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

numero = int(input("Ingrese un numero:"))
resultado = factorial(numero)
print(f"El factorial de es {resultado}")
