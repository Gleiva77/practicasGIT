#8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
#por pantalla si contiene la letra "a".

cadena = input("Ingresa una cadena de caracteres: ")

cadena.lower()

if "a" in cadena:
    print("La cadena contiene la letra 'a'")
else:
    print("La cadena no contiene la letra 'a'")