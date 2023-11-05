import funciones
#Punto 1
numero_dni1 = 1234567
numero_dni2 = 12345678
numero_dni3 = 12345

print(funciones.es_dni_valido(numero_dni1))
print(funciones.es_dni_valido(numero_dni2))  
print(funciones.es_dni_valido(numero_dni3))  
 
#Punto 2
cadena1 = "  Hola, mundo   "
cadena2 = "   Python es genial"
cadena3 = "  "
cadena4 = "UnaPalabra"
print("punto 2")
print(funciones.longitud_ultima_palabra(cadena1))  # Debe imprimir 5
print(funciones.longitud_ultima_palabra(cadena2))  # Debe imprimir 6
print(funciones.longitud_ultima_palabra(cadena3))  # Debe imprimir 0
print(funciones.longitud_ultima_palabra(cadena4))  # Debe imprimir 10

#Punto 3
socios = []
print("Punto 3")
while True:
    nombre_completo = input("Nombre completo del socio (deje en blanco para salir): ")
    
    if not nombre_completo:
        break
    
    dni = input("Número de DNI del socio: ")
    while not funciones.es_dni_valido(dni):
        print("Número de DNI no válido. Debe tener 7 u 8 dígitos.")
        dni = input("Número de DNI del socio: ")
    
    identificador = funciones.obtener_identificador(nombre_completo, dni)
    
    socios.append((nombre_completo, identificador))

# Mostrar los identificadores de los socios
print("Identificadores únicos de los socios:")
for nombre, identificador in socios:
    print(f"Nombre: {nombre}")
    print(f"ID -> {identificador}")

#Punto 4
print("punto 4")
# Solicitar al usuario dos números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Verificar si alguno de los números es múltiplo del otro utilizando la función
if funciones.es_multiplo(numero1, numero2) or funciones.es_multiplo(numero2, numero1):
    print(f"¡Al menos uno de los números es múltiplo del otro!")
else:
    print("Ninguno de los números es múltiplo del otro.")
    
#Punto 5
print("punto 5")
num_dias = int(input("Ingrese el número de días para los que desea calcular la temperatura media: "))

for dia in range(1, num_dias + 1):
    # Solicitar las temperaturas máxima y mínima para el día actual
    temp_max = float(input(f"Temperatura máxima para el día {dia}: "))
    temp_min = float(input(f"Temperatura mínima para el día {dia}: "))
    
    # Calcular la temperatura media utilizando la función
    temp_media = funciones.temperatura_media(temp_max, temp_min)
    
    # Mostrar la temperatura media para el día actual
    print(f"Temperatura media para el día {dia}: {temp_media}°C")
    
#Punto 6
print("punto 6")
texto_original = input("Ingrese un texto: ")

# Llamar a la función para agregar espacios
texto_con_espacios = funciones.agregar_espacios(texto_original)

# Mostrar el resultado
print("Texto con espacios adicionales:")
print(texto_con_espacios)

#Punto 7
print("punto 7")
numeros = []

while True:
    try:
        numero = float(input("Ingrese un número (o presione Enter para finalizar): "))
        numeros.append(numero)
    except ValueError:
        break  # Si no se ingresa un número, se finaliza la entrada

maximo, minimo = funciones.encontrar_maximo_y_minimo(numeros)

if maximo is not None and minimo is not None:
    print(f"El valor máximo es: {maximo}")
    print(f"El valor mínimo es: {minimo}")
else:
    print("No se ingresaron números para calcular el máximo y mínimo.")

#Punto 8
print("punto 8")
radio = float(input("Ingrese el radio de la circunferencia: "))

area, perimetro = funciones.calcular_area_y_perimetro(radio)

if area is not None and perimetro is not None:
    print(f"El área de la circunferencia es: {area:.2f}")
    print(f"El perímetro de la circunferencia es: {perimetro:.2f}")
else:
    print("El radio debe ser un número positivo para calcular el área y el perímetro.")