import sys
print ("Calculadora IMC")
print ("Vamos a calcular el Indice de Masa Corporal según tú peso y estatura")
print ("Para esto primero te pediremos algunos datos")
print ("Se requiere todos los datos o se cierra el programa")
nombre = str(input("¿Cuál es tú nombre o nombres?: "))
if nombre == "":
	sys.exit(-1)
apellido1 = str(input("¿Cuál es tú apellido paterno?: "))
if apellido1 == "":
	sys.exit(-1)
apellido2 = str(input("¿Cuál es tú apellido materno?: "))
if apellido2 == "":
	sys.exit(-1)
estatura = (input("¿Cuál es tú estatura en metros? Ejemplo 1.75: "))
try:
    estatura = float(estatura)
except:
    print("peso invalido, tendras que empezar nuevamente")
if estatura == "":
 	sys.exit(-1)
peso = (input("Cual es tú peso en kilos?: "))
try:
    estatura = float(estatura)
except:
    print("peso invalido, tendras que empezar nuevamente")
peso = int(peso)
if peso == "":
	sys.exit(-1)
print (f"Hola, {nombre} {apellido1} {apellido2}")
print ("por tú estatura de", estatura, ("mtos"))
print ("y tú peso ", peso, ("Kg"))
print (f"Tú IMC es: {peso/estatura**2 : .2f}")
print ("Muchas gracias por tu participación")
input ("Presione cualquier letra para cerrar el programa, gracias")