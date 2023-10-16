"""Escribir un programa que pida al usuario una palabra y 
la muestre por pantalla 10 veces"""
palabra = input("ingrese la palabra: ")
for i in range(10):
    print(palabra)

"""Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla todos los años que 
ha cumplido (desde 1 hasta su edad).
"""
# ingreso de datos
edad = int(input("Ingresa tu edad: "))

# Mostrar los años que ha cumplido
print("Has cumplido los siguientes años:")
for i in range(1, edad + 1):
    print(i)#

"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas.
"""
# Pedir al usuario un número 
numero = int(input("Por favor, ingresa un número entero positivo: "))

# Validar que el número ingresado sea positivo
if numero <= 0:
    print("El número ingresado no es positivo.")
else:
    # Inicializar una cadena vacía para almacenar los números impares
    impares = ""

    # Recorrer todos los números 
    for i in range(1, numero + 1, 2):
        if i == 1:
            impares = str(i)
        else:
            impares += ", " + str(i)

    # Mostrar los números impares separados por comas
    print("Números impares desde 1 hasta", numero, ":", impares)

"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
# Pedir al usuario un número entero positivo
numero = int(input("Por favor, ingresa un número entero positivo: "))

# Validar que el número ingresado sea positivo
if numero <= 0:
    print("El número ingresado no es positivo.")
else:
    cuenta_atras = ""
    for i in range(numero, -1, -1):
        if cuenta_atras:
            cuenta_atras += ", "
        cuenta_atras += str(i)
    
    print("Cuenta atrás desde", numero, "hasta 0:", cuenta_atras)
    
"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

# Pedir al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertir = float(input("Cantidad a invertir: "))
tasa_interes_anual = float(input("Tasa de interés anual (en porcentaje): "))
num_anios = int(input("Número de años: "))

# Convertir la tasa de interés de porcentaje a decimal
tasa_interes_anual /= 100

# Calcular y mostrar el capital obtenido para cada año
for anio in range(1, num_anios + 1):
    capital_obtenido = cantidad_invertir * (1 + tasa_interes_anual) ** anio
    print(f"Año {anio}: Capital obtenido = {capital_obtenido:.2f}")

"""Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido."""

# Pedir al usuario un número 
numero = int(input("Por favor, ingresa un número entero: "))

# Muestra un triángulo rectángulo
for i in range(1, numero + 1):
    for j in range(i):
        print("*", end="")
    print() 
    
"""Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10."""

for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  

"""Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo."""
# Pedir al usuario un número
numero = int(input("Por favor, ingresa un número entero: "))

# Mostrar el triángulo 
for i in range(1, numero + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()

"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""
# Contraseña
contrasena = "nombre"

# Pedir al usuario la contraseña
intento = input("Por favor, ingresa la contraseña: ")

# Verificar si el intento de contraseña es correcto
while intento != contrasena:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    intento = input("Por favor, ingresa la contraseña: ")

print("¡Contraseña correcta! Bienvenido.")

""" Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es un número primo o no.
"""
# Pedir al usuario un número entero
numero = int(input("Por favor, ingresa un número entero: "))

# Verificar si el número es primo
if numero > 1:
    es_primo = True
    for i in range(2, numero):
        if (numero % i) == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
else:
    print(f"{numero} no es un número primo.")
    
"""Escribir un programa que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
# Pedir al usuario una palabra
palabra = input("Por favor, ingresa una palabra: ")

# Mostrar las letras de la palabra empezando por la última
for letra in palabra[::-1]:
    print(letra)

""" Escribir un programa en el que se pregunte al usuario por una frase 
y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

# Pedir al usuario una frase
frase = input("Por favor, ingresa una frase: ")

# Pedir al usuario una letra
letra = input("Por favor, ingresa una letra: ")

# Contar el número de veces que aparece la letra en la frase
conteo = frase.count(letra)

# Mostrar el resultado
print(f'La letra "{letra}" aparece {conteo} veces en la frase.')

""" Escribir un programa que muestre el eco de todo lo que el 
usuario introduzca hasta que el usuario escriba “salir” que terminará."""

entrada = input("Escribe algo (o 'salir' para terminar): ")

while entrada.lower() != "salir":
    print(entrada)
    entrada = input("Escribe algo (o 'salir' para terminar): ")
    
"""Escriba un programa que pida dos números enteros y escriba qué números son pares 
y cuáles impares desde el primero hasta el segundo."""

# Pedir al usuario dos números enteros
numero1 = int(input("Por favor, ingresa el primer número entero: "))
numero2 = int(input("Por favor, ingresa el segundo número entero: "))

# Determinar el rango de números
inicio = min(numero1, numero2)
fin = max(numero1, numero2)

# Mostrar números pares e impares en el rango
print("Números pares en el rango:")
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)

print("Números impares en el rango:")
for numero in range(inicio, fin + 1):
    if numero % 2 != 0:
        print(numero)

""" Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores"""

# Pedir al usuario un número entero mayor que cero
numero = int(input("Por favor, ingresa un número entero mayor que cero: "))

# Validar que el número sea mayor que cero
if numero <= 0:
    print("El número debe ser mayor que cero.")
else:
    print(f"Los divisores de {numero} son:")

    # Encontrar y mostrar los divisores
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

#16- Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

numbers= int(input("ingrese cuantos numeros va a introducir: "))

negative = 0

for i in range (numbers):
     number = int(input("ingrese cualquier numero porfavor: "))
     if number < 0:
        negative += 1

print("la cantidad de numeros negativos es de:",negative)

#17- Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase = input("ingrese una frase:")

vocal = []

for letter in phrase:
         if letter.lower() in "aeiou" and letter.lower() not in vocal:
           vocal.append(letter.lower())

#print("vocale en frase sin repetirse son ".join(letter_vocal))

print("vocales en la frase sin repetirse :", ", ".join(vocal))
"""
"""
#18-Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y,
# a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

fibo = [0,1]

for i in range (2,10):
    next_number = fibo[i-1] + fibo[i - 2]
    fibo.append(next_number)

print("los 10 numero son:")
print(fibo)   

#19 - Escriba un programa que simule una alcancía. 
# El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. 
# A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 
# El programa deberá comprobar que las cantidades ingresadas sean positivas.

save = float(input("Ingrese la cantidad que quiere ahorrar: "))
total_saved = 0
while total_saved < save:
    cantidad = float(input("Ingrese la cantidad que desea ahorrar (debe ser positiva): "))
    if cantidad <= 0:
        print("La cantidad ingresada debe ser positiva. Inténtelo de nuevo.")
        continue
    total_saved += cantidad
print("¡Felicidades! Has alcanzado tu objetivo de ahorro. Total ahorrado: ", total_saved)

#20-Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# Finalmente, mostrar la sumatoria de todos los números ingresados.

total = 0
while True:
    i = int(input("ingrese un numero diferente de 0:"))
    if i == 0:
        break
    total += i
print("la sumatoria de los numero es ",total)

#21 - Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
max = 0
while True:
    number = int(input("Ingrese un número entero positivo :"))
    
    if number > max and number >0:
        max = number  
    if number == 0:
        break  
    
print("El número máximo ingresado es:", max)

#22-Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. 
# Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

pairs = 0

# Leer números enteros positivos del teclado hasta que se ingrese -1
while True:
    number = int(input("Ingrese un número entero positivo o ingrese -1 para salir: "))
    if number == -1:
        break   
    digits = sum(int(digits) for digits in str(abs(number)))
    print("La suma de los dígitos de", number, "es", digits)
    if number % 2 == 0:
        pairs += 1
print("Cantidad de números pares ingresados:", pairs)

#23-Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0.

total_buying = 0
while True:
    amount = float(input("Ingrese el monto de la compra o 0 para salir: "))
    if amount == 0:
        break 
    if amount < 0:
        print("Por favor, ingrese un monto positivo.")
        continue
    total_buying += amount
print("El total es: $" + str(total_buying))

#24-Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar,informar el total a pagar teniendo que cuenta que, 
# si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
total_buying2 = 0
while True:
    amount2 = float(input("Ingrese el monto de la compra o 0 para salir: "))
    if amount2 < 0:
        print("Por favor, ingrese un monto positivo.")
        continue
    if amount2 == 0:
        break 
    total_buying2 += amount2

if total_buying2 > 1000:
    discount = total_buying2 * 0.10
    total_buying2 -= discount
print("El total a pagar es: $" + str(total_buying2))

#25-Dado un número entero positivo, mostrar su factorial. 
# El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. 
# El factorial de 0 es 1.
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print("El factorial de", numero, "es", factorial)





