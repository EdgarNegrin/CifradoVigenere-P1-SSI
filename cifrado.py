'''
Practica 1: Cifrado de Vigenere
Fecha: 27/02/2021

Autor: Edgar Negrin Gonzalez
Email: alu0101210964@ull.edu.es

El programa pide por teclado un mensaje y una clave e implementa el cifrado y descifrado de Vigenere.

Ejecucion: py cifrado.py
'''
import sys

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Modulo 26 (Sin Ñ y con W)
# Guardamos el mensaje, eliminamos los espacios y lo transformamos a mayuscula
mensaje = str(input("Introduzca el mensaje a cifrar: "))
mensaje = mensaje.replace(' ', '').upper()
# Comprobacion del mensaje	
for i in range(len(mensaje)):
	if alfabeto.find(mensaje[i]) == -1:
		print ('Se han introducido caracteres no validos.')
		sys.exit(1)	

# Guardamos la clave, eliminamos los espacios y lo tranformamos a mayuscula
clave_original = str(input("Introduzca la palabra clave: "))
clave_original = clave_original.replace(' ', '').upper()
# Comprobacion de la clave
for i in range(len(clave_original)):
	if alfabeto.find(clave_original[i]) == -1:
		print ('Se han introducido caracteres no validos.')
		sys.exit(1)	
clave = ''
mensaje_cifrado = ''
mensaje_descifrado = ''

# Si el tamaño del mensaje es mayor que la clave
if len(mensaje) > len(clave_original):
	# Añadimos la clave hasta que el tamaño sea menor o igual al mensaje
	for i in range(int(len(mensaje) / len(clave_original))):		
		clave += clave_original									
	clave += clave_original[:len(mensaje) % len(clave_original)] 

# Si el tamaño del mensaje es menor que la clave
elif len(mensaje) < len(clave_original):
	clave = clave_original[:len(mensaje)]

# Si el mensaje es del mismo tamaño que la clave
elif len(mensaje) == len(clave_original):
	clave = clave_original

# En cualquier otro caso
else:
	print ('Se ha producido un error.')
	sys.exit(1)

print ('\nMensaje original: ' + mensaje)
print ('Palabra clave: ' + clave_original)
print ()

# Funcion que calcula el mensaje cifrado
def cifradoVigenere(mensaje, clave, alfabeto):
    mensaje_cifrado_temp = ''
    for i in range(len(mensaje)): 
	    pos_mensaje = alfabeto.find(mensaje[i]) # Posicion del caracter del mensaje	 
	    pos_clave = alfabeto.find(clave[i])	# Posicion del caracter de la clave
	    suma = pos_mensaje + pos_clave
	    suma_modulo = suma % len(alfabeto)
	    mensaje_cifrado_temp += alfabeto[suma_modulo]
    return mensaje_cifrado_temp

# Funcion que calcula el mensaje descifrado
def descifradoVigenere(mensaje_cifrado, alfabeto, clave):
    mensaje_descifrado_temp = ''
    for i in range(len(mensaje_cifrado)):
	    pos_mensaje_cifrado = alfabeto.find(mensaje_cifrado[i]) # Posicion del caracter del mensaje cifrado
	    pos_clave = alfabeto.find(clave[i])	# Posicion del caracter de la clave
	    resta = pos_mensaje_cifrado - pos_clave
	    resta_modulo = resta % len(alfabeto)
	    mensaje_descifrado_temp += alfabeto[resta_modulo]
    return mensaje_descifrado_temp


mensaje_cifrado = cifradoVigenere(mensaje, clave, alfabeto)
mensaje_descifrado = descifradoVigenere(mensaje_cifrado, alfabeto, clave)
print ('Mensaje cifrado: ' + mensaje_cifrado + '\n')
print ('Mensaje descifrado: ' + mensaje_descifrado + '\n')

sys.exit(0)