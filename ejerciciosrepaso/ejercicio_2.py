"""Escribir una función que calcule el área de un círculo dado su radio."""
def circulo(radio):
    calcular_area = 3.1416*radio**2
    return calcular_area
radio=float(input("Ingrese el radio del círculo:"))
area=circulo(radio)
print("El radio del circulo es",area)
