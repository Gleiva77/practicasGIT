#5-Crea un programa que pida al usuario dos números enteros y muestre en
#pantalla su cociente y su resto.

numero1=float(input("ingresa el primer número: "))
numero2=float(input("ingresa el segundo número: "))
cociente=numero1//numero2
resto=numero1%numero2

print("el cociente es: ",cociente)
print("el resto es= ",resto)