# Desafío 1:
# Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
# sus ventas totales y el departamento comercial te solicita que ayudes a los
# vendedores a calcular sus comisiones creando un programa que les pregunte su
# nombre y cuánto han vendido en éste mes.
# Tu programa le va a responder con una frase que incluya su nombre y el monto
# que le corresponde por las comisiones

nombre = input("Cual es tu nombre: ")
ventas_mensuales = int(input("¿Cuanto vendiste este mes?"))

calculo_ventas = (ventas_mensuales/100) * 6

print(nombre,"Tu comisión mensual es de: ",calculo_ventas)