#ejercicio 1
# Pedir al usuario el corrimiento
corrimiento = int(input("Ingrese la cantidad de lugares que se correrán las letras: "))

# Leer los 5 mensajes del jefe y encriptarlos usando el mismo corrimiento
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i+1} del jefe: ")
    mensaje_encriptado = ""
    for letra in mensaje:
        if letra.isalpha():  # Verificar si es una letra
            indice = (alfabeto.index(letra.upper()) + corrimiento) % 27  # Aplicar el corrimiento
            # Mayuscula a minuscula
            if letra.isupper():
                mensaje_encriptado += alfabeto[indice].lower()
            else :
                 mensaje_encriptado += alfabeto[indice]
        else:
            # Mantener caracteres que no son letras sin cambios
            mensaje_encriptado += letra
    print(f"Mensaje {i+1} encriptado: {mensaje_encriptado}")

#ejercicio 2

""" Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""
"""
par = 0
impar = 0

while i != 0 :
    
    """