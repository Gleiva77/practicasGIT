#11-Escribir un programa que pida al usuario dos números y muestre por pantalla
#la suma de ellos solo si ambos son pares.

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingresa un segundo número: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    suma = numero1 + numero2
    print("La suma de los números es:", suma)
else:
    print("No se pudo sumar por que uno de los números ingresados es impar.")