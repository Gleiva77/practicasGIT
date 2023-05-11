#8-Crea un programa que pida al usuario el radio de un círculo y muestre su
#diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.




radio = float(input('Ingrese el radio del círculo: '))
area = pi * radio ** 2 
circunferencia = 2*pi*radio
diametro = 2*radio

print(f'El área del círculo es: {area}')
print ("La circunferencia es: ", circunferencia)
print ("El diametro es: ", diametro)