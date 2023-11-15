#1.Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja#

def ordenamiento_burbuja(lista):
    n = len(lista)
    # Iterar a través de todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar, por lo tanto, no es necesario verificarlos
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Tomar una lista de números como entrada del usuario
numeros = input("Ingrese una lista de números separados por espacios: ").split()
# Convertir los elementos de la lista en enteros
numeros = [int(numero) for numero in numeros]

# Llamar a la función de ordenamiento de burbuja
ordenamiento_burbuja(numeros)

# Imprimir la lista ordenada
print("Lista ordenada en orden ascendente:", numeros)
# 2 Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.#
def ordenamiento_seleccion(lista):
    n = len(lista)
    # Iterar a través de todos los elementos de la lista
    for i in range(n):
        # Encontrar el índice del elemento mínimo en el resto de la lista
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        # Intercambiar el elemento mínimo encontrado con el primer elemento no ordenado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
# Tomar una lista de palabras como entrada del usuario
palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()
# Llamar a la función de ordenamiento de selección
ordenamiento_seleccion(palabras)
# Imprimir la lista ordenada alfabéticamente en orden ascendente
print("Lista ordenada alfabéticamente en orden ascendente:", palabras)
#3.#
def merge_sort(lista):
    if len(lista) > 1:
        # Dividir la lista en mitades
        mitad = len(lista) // 2
        mitad_izquierda = lista[:mitad]
        mitad_derecha = lista[mitad:]
        # Llamadas recursivas para ordenar las dos mitades
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)
        # Inicializar índices para las sublistas y la lista principal
        i, j, k = 0, 0, 0
        # Fusionar las dos mitades ordenadas
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1
        # Verificar si quedan elementos en alguna de las mitades
        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1
        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1
# Ejemplo de uso
numeros = [12, 4, 5, 6, 7, 3, 1, 15]
print("Lista original:", numeros)
# Llamar a la función merge_sort para ordenar la lista
merge_sort(numeros)
# Imprimir la lista ordenada
print("Lista ordenada con Merge Sort:", numeros)

#4.#
def ordenamiento_insercion_por_longitud(lista):
    for i in range(1, len(lista)):
        palabra_actual = lista[i]
        longitud_actual = len(palabra_actual)
        j = i - 1
        while j >= 0 and len(lista[j]) > longitud_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = palabra_actual
# Tomar una lista de cadenas como entrada del usuario
cadenas = input("Ingrese una lista de cadenas separadas por espacios: ").split()
# Llamar a la función de ordenamiento de inserción por longitud
ordenamiento_insercion_por_longitud(cadenas)
# Imprimir la lista ordenada por longitud
print("Lista ordenada por longitud de cadenas:", cadenas)
