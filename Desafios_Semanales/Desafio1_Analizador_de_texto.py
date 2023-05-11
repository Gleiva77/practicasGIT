texto = input("Ingresa un texto: ")
letras = input("Ingresa 3 letras separadas por espacios: ").split()

# Convertimos el texto y las letras a minúsculas
texto = texto.lower()
letras = [letra.lower() for letra in letras]

# Contamos las letras en el texto
contador = {}
for letra in letras:
    contador[letra] = texto.count(letra)

# Contamos las palabras en el texto
palabras = texto.split()
cantidad_palabras = len(palabras)

# Obtenemos la primera y última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]

# Mostramos el texto invertido
texto_invertido = texto[::-1]

# Verificamos si "python" aparece en el texto
if "python" in texto:
    aparece_python = "sí"
else:
    aparece_python = "no"

# Imprimimos los resultados
print("1- Cantidad de veces que aparece cada una de las letras:")
for letra, cantidad in contador.items():
    print("    La letra", letra, "aparece", cantidad, "veces.")
print("2- Cantidad de palabras en el texto:", cantidad_palabras)
print("3- Primera letra del texto:", primera_letra)
print("   Última letra del texto:", ultima_letra)
print("4- Texto invertido:", texto_invertido)
print("5- ¿Aparece la palabra 'python'?:", aparece_python)