#2-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es positivo, negativo o cero.

numero = int(input("ingrese un numero entero: "))

if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print ("el numeor es cero")