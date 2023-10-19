#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma