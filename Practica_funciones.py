import funciones

while True:
        numero = int(input("Ingrese un número (o 0 para salir): "))
        if numero == 0:
            break
        suma = funciones.suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es: {suma}")
