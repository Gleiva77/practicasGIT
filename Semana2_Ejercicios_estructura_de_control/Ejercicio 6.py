#6-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print("El número " + str(numero) + " es multiplo de 2")
elif numero % 3 == 0:
    print("El número " + str(numero) + " es multiplo de 3")