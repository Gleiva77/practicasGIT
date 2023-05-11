#15-Escribe un programa que solicite al usuario una temperatura en grados
#Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
#La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

grados_celsius = int(input("Ingrese una temperatura: "))

fahrenheit = (grados_celsius * 1.8) + 32

print ("La temperatura es: ",fahrenheit, " fahrenheit")

