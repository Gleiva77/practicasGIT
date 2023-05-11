# 19-Escribe un programa que solicite al usuario un número decimal y luego
# imprima la parte entera y decimal por separado.

numero_decimal = input("ingresa un número decimal: ").split(",")

print("La parte entera es: ",numero_decimal[0],"y la parte decimal es: ",numero_decimal[1])
