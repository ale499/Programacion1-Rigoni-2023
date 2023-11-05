import math
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def es_dni_valido(numero_dni):
    numero_dni_str = str(numero_dni)
    if 7 <= len(numero_dni_str) <= 8:
        if numero_dni_str.isdigit():
            return True
    return False

def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()

    if palabras:
        ultima_palabra = palabras[-1]
        return len(ultima_palabra)
    else:
        return 0

def obtener_identificador(nombre_completo, dni):
    palabras = nombre_completo.split()
    
    primer_nombre = palabras[0]
    
    apellido = palabras[-1]
    
    dni_str = str(dni)[:3]
    
    identificador = primer_nombre + str(len(apellido)) + dni_str
    
    return identificador

def obtener_identificador(nombre_completo, dni):
    palabras = nombre_completo.split()
    
    primer_nombre = palabras[0]
    
    apellido = palabras[-1]
    
    dni_str = str(dni)[:3]
    
    identificador = primer_nombre + str(len(apellido)) + dni_str
    
    return identificador

def es_multiplo(numero1, numero2):
    if numero2 == 0:
        return False
    return numero1 % numero2 == 0

def temperatura_media(temp_max, temp_min):
    return (temp_max + temp_min) / 2

def agregar_espacios(texto):
    texto_con_espacios = " ".join(texto)
    return texto_con_espacios

def encontrar_maximo_y_minimo(lista):
    if not lista:
        return None, None 
    
    maximo = minimo = lista[0]  
    
    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    
    return maximo, minimo

def calcular_area_y_perimetro(radio):
    if radio < 0:
        return None, None 
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro