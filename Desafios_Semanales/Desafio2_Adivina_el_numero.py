"""Desafío 3: Adivina el número
Requisitos técnicos:
- Operadores lógicos.
- Operadores de comparación.
- Control de flujo - Condicionales.
- Control de Flujo - Repetitivas.
Vamos a crear un juego completamente funcional.
Para ello el programa debe:
 Pedir al usuario que ingrese su nombre.
 Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
 Generar aleatoriamente un número entero entre 1 y 100.
tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
 Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
El "número" ingresado por el usuario puede:
 No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
tip 2: con el método isdigit() puedes saber si es posible convertir a entero
 Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
 Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
 Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento
lo adivinó.
 Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si
debes descontarle un intento.
 En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que
ingrese otro número.
 Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el
número que tenía que adivinar.
"""

#Importar la libreria random y generar el numero al azar de 1 al 100.
import random
numero_al_azar = random.randint(1, 100)

#Pedido de nombre del participante y explica las reglas del juego.
nombre_participante = input("Ingrese el nombre_participante del Jugador: ")
print(f"Hola {nombre_participante}. El juego consiste en adivinar un número entre 1 y 100.")
print("** Pero ojo, solo tienes 8 intentos para adivinarlo.")

#Cantidad de intentos totales.
intentos_disponibles = 8

#lleva el control de la cantidad de intentos, si no acierta el participante descuenta un intento.
for intento in range(1, intentos_disponibles + 1):
    print(f"Intento N°{intento}. Te quedan {intentos_disponibles - intento + 1} intentos.")

    #Verifica si el numero ingresado es entero, si no es entero avisa al participante y vuelve a solicitar otro numero.
    while True:
        numero_ingresado = input("Por favor, ingrese un número entero: ")
        if numero_ingresado.isdigit():
            numero = int(numero_ingresado)
            break
        else:
            print("El número ingresado no es entero. Por favor, ingrese un número correcto.")

# compara la respuesta con lo ingresado por el participante, si es ganador avisa y termina el codigo. sino da pistas del numero a adivinar.
    if numero == numero_al_azar:
        print(f"GANASTE!!!, {nombre_participante} Adivinaste el número en la chance N°{intento}.")
        break
    elif numero > numero_al_azar:
        print("Te doy una pista, el número es menor.")
    elif numero < numero_al_azar:
        print("Te doy otra pista, el número es mayor.")

#En el caso de que el participante no acierte en las 8 oportunidades, se avisa cual era el numero sorteado y da juego finalizado.
    if intento == intentos_disponibles:
        print(f"UY perdiste, {nombre_participante}, ya no tienes mas intentos. El número era {numero_al_azar}.")