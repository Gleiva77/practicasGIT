#7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
#es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input("Ingrese un caracter: ")

if (caracter >= "0" and caracter <= "9"):
    print ("Es un numero entero")
elif (caracter >= "a" and caracter <= "z"):
    print ("Es una letra minuscula")
elif (caracter >= "A" and caracter <= "Z"):
    print ("Es una letra Mayuscula")
else:
    print("Es un caracter especial")