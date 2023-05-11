#12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
#dd/mm/aaaa y luego imprima su edad en años.
#Utiliza la función .split()

fechaNacimiento= input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

fechas=fechaNacimiento.split("/")
edad=2023-(int(fechas[2]))
print(edad)



