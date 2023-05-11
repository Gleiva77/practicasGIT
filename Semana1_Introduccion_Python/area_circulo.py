#6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
#La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
#Supongamos que pi = 3.1416

from math import pi

radio = float(input('Ingrese el radio del círculo: '))
area = pi * radio ** 2 

print(f'El área del círculo es: {area}')
