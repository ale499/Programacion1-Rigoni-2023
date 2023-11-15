#1.      Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.#
def contar_digitos(n):
    # Convertir el número a cadena y contar la longitud de la cadena
    cantidad_digitos = len(str(n))
    return cantidad_digitos
# Solicitar al usuario que ingrese un número positivo
numero = int(input("Ingrese un número positivo: "))
# Llamar a la función contar_digitos y mostrar el resultado
resultado = contar_digitos(numero)
print("El número tiene", resultado, "dígitos.")

#2.      Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.#
def es_potencia(n, b):
    # Si n es 1, entonces b^0 es igual a 1 y n es una potencia de b
    if n == 1:
        return True
    # Inicializar una variable para almacenar el resultado de b^exp
    exp = 1
    # Mientras b elevado a exp sea menor o igual a n
    while exp <= n:
        # Si b^exp es igual a n, entonces n es una potencia de b
        if exp == n:
            return True
        # Incrementar exp multiplicando b por sí mismo
        exp *= b
    # Si no se cumple la condición en ningún punto, n no es una potencia de b
    return False

# Solicitar al usuario que ingrese dos enteros n y b
n = int(input("Ingrese un número entero n: "))
b = int(input("Ingrese un número entero b: "))

# Llamar a la función es_potencia y mostrar el resultado
resultado = es_potencia(n, b)
print("¿n es potencia de b?", resultado)

3.
def par(n):
    if n == 0:
        return True  # 0 es par
    else:
        return impar(n - 1)
def impar(n):
    if n == 0:
        return False  # 0 no es impar
    else:
        return par(n - 1)

# Ejemplos de uso
numero = int(input("Ingrese un número natural: "))
if par(numero):
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")

4.

def encontrar_mayor_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maximo_sublista = encontrar_mayor_elemento(lista[1:])
        return max(lista[0], maximo_sublista)
# Ejemplo de uso
lista_numeros = [4, 10, 2, 8, 7]
mayor_elemento = encontrar_mayor_elemento(lista_numeros)

print(f"El mayor elemento de la lista es: {mayor_elemento}")
