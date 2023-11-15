
1.     # Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.#

# Inicializar una lista vacía para almacenar los números
numeros = []

# Solicitar al usuario que ingrese números hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número (o ingrese 0 para finalizar): "))
    
    # Verificar si el número ingresado es 0 para finalizar el bucle
    if numero == 0:
        break
    else:
        # Agregar el número a la lista si no es 0
        numeros.append(numero)

# Imprimir la lista de números ingresados
print("Los números ingresados son:", numeros)




2. #Imprimir la sumatoria de todos los números de la lista.#
# Inicializar una lista vacía para almacenar los números
numeros = []
# Solicitar al usuario que ingrese números hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número (o ingrese 0 para finalizar): "))
    # Verificar si el número ingresado es 0 para finalizar el bucle
    if numero == 0:
        break
    else:
        # Agregar el número a la lista si no es 0
        numeros.append(numero)
# Imprimir la lista de números ingresados
print("Los números ingresados son:", numeros)
# Calcular la sumatoria de los números en la lista y imprimir el resultado
suma = sum(numeros)
print("La sumatoria de los números ingresados es:", suma)
3.
# Inicializar una lista vacía para almacenar los números
numeros = []
# Solicitar al usuario que ingrese números hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número (o ingrese 0 para finalizar): "))
    # Verificar si el número ingresado es 0 para finalizar el bucle
    if numero == 0:
        break
    else:
        # Agregar el número a la lista si no es 0
        numeros.append(numero)
# Imprimir la lista de números ingresados
print("Los números ingresados son:", numeros)
# Calcular la sumatoria de los números en la lista
suma_total = sum(numeros)
# Imprimir la sumatoria
print("La sumatoria de los números en la lista es:", suma_total)

4.
def obtener_diagonal_principal(matriz):
    # Obtener la longitud de la matriz (número de filas o columnas)
    n = len(matriz)
    # La diagonal principal es una lista de elementos de la forma matriz[i][i]
    diagonal_principal = [matriz[i][i] for i in range(n)]
    return diagonal_principal
def obtener_diagonal_inversa(matriz):
    # Obtener la longitud de la matriz (número de filas o columnas)
    n = len(matriz)
    # La diagonal inversa es una lista de elementos de la forma matriz[i][n-1-i]
    diagonal_inversa = [matriz[i][n-1-i] for i in range(n)]
    return diagonal_inversa
# Ejemplo de una matriz cuadrada
matriz_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Obtener la diagonal principal
diagonal_principal = obtener_diagonal_principal(matriz_cuadrada)
print("Diagonal Principal:", diagonal_principal)
# Obtener la diagonal inversa
diagonal_inversa = obtener_diagonal_inversa(matriz_cuadrada)
print("Diagonal Inversa:", diagonal_inversa)
