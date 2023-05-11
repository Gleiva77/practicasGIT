# 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
# e imprima su índice de masa corporal (IMC).
# La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

altura = int(input("Ingrese su altura: "))
peso = int(input("Ingreso su peso: "))

imc = (peso / (altura ** 2)) * 10000

print ("su Indice de masa corporal es de: ", imc)