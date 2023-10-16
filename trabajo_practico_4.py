""" punto 1"""
x = 0

while x < 30:
    x += 1
    if x in (4, 6, 10):
        print("Se saltó el valor " + str(x) + " de x")
        continue
    print("El valor del bucle es: " + str(x))
    if x == 15:
        print("Se rompió la ejecución del bucle cuando x valía: 15")
        break

"""punto 2"""
# Inicializar una lista para almacenar las líneas
lineas = []

# Leer líneas de entrada
while True:
    linea = input("Ingresa una línea de texto (o presiona Enter para finalizar): ")
    if not linea:
        break
    lineas.append(linea.upper())

# Imprimir las líneas en mayúsculas
for linea in lineas:
    print(linea)
    
"""punto 3"""
#saldo de la cuenta
saldo = 0

# Leer la bitácora de operaciones
while True:
    entrada = input("Introduce una operación (D para depósito, R para retiro, línea vacía para finalizar): ")
    
    if entrada == "":
        break
    
    # Separar el tipo de operación y el monto
    tipo, monto = entrada.split()
    monto = int(monto)
    
    if tipo == "D":
        saldo += monto
    elif tipo == "R":
        saldo -= monto

# Mostrar el saldo final
print(saldo)

"""punto 4"""

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

cantidad_primos = 0

while True:
    numero = int(input("Ingresa un número mayor que 1 (o 0 para finalizar): "))
    
    if numero == 0:
        break

    if es_primo(numero):
        cantidad_primos += 1

print(f"La cantidad total de números primos ingresados es: {cantidad_primos}")

"""punto 5"""

# Pedir al usuario que ingrese dos años
inicio = int(input("Ingresa el primer año: "))
fin = int(input("Ingresa el segundo año: "))

# Iterar a través del rango de años
for año in range(inicio, fin + 1):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        if año % 10 == 0:
            print(año)


"""punto 6"""

for numero in range(1, 21):
    if numero % 2 != 0:
        continue  # Omitir números impares
    print(numero)

"""punto 7"""

# Lista de números
numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Número que deseamos encontrar
numero_objetivo = 12

# buscar el número objetivo
encontrado = False
for numero in numeros:
    if numero == numero_objetivo:
        encontrado = True
        break

# Comprobar si se encontró el número
if encontrado:
    print(f"¡Se encontró el número {numero_objetivo} en la lista!")
else:
    print(f"El número {numero_objetivo} no se encontró en la lista.")

"""punto 8"""

while True:
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "0":
        print("Saliendo del programa.")
        break
    elif opcion == "1":
        print("Has seleccionado la Opción 1.")
    elif opcion == "2":
        print("Has seleccionado la Opción 2.")
    elif opcion == "3":
        print("Has seleccionado la Opción 3.")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")




