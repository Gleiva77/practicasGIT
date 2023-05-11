#9-Escribir un programa que pida al usuario tres números y muestre por pantalla
#el mayor de ellos.

n1 = input("Ingrese un numero: ")
n2 = input("Ingrese otro numero: ")
n3 = input("Ingrese un ultimo numero: ")

if (n1 > n2 and n1 > n3):
    print(f"El numero {n1} es el mas alto")
elif (n2 > n3 and n2 > n1):
    print(f"El numero {n2} es el mas alto")
else:
    print(f"El numero {n3} es el mas alto")