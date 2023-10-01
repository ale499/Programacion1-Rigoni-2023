# los lunes se dicta nivel inicial, los martes el nivel intermedio, 
# los miércoles el nivel avanzado, los jueves son para práctica hablada 
# y los viernes se dicta inglés para viajeros.


fecha = input("Por favor, ingrese la fecha en formato 'día, DD/MM': ").lower()  # Convertir a minúsculas 

# Separar la entrada en día y fecha
dia_semana, fecha = fecha.split(', ')[0], fecha.split(', ')[1]

# Validar el día de la semana
if dia_semana == "lunes":
    nivel = "inicial"
elif dia_semana == "martes":
    nivel = "intermedio"
elif dia_semana == "miércoles":
    nivel = "avanzado"
elif dia_semana == "jueves":
    nivel = "práctica hablada"
elif dia_semana == "viernes":
    nivel = "inglés para viajeros"
else:
    print("Error: Día de la semana no válido.")
    exit()

# Procesar según el nivel
if nivel in ["inicial", "intermedio", "avanzado"]:
    tiene_examenes = input("¿Hubo exámenes? (Sí/No): ").lower()
    if tiene_examenes == "si" :
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
        porcentaje_aprobados = (aprobados / (aprobados + no_aprobados)) * 100
        print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")
elif nivel == "práctica hablada":
    asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
    if asistencia > 50:
        print("Asistió la mayoría.")
    else:
        print("No asistió la mayoría.")
elif nivel == "inglés para viajeros":
    if fecha == "01/01" or fecha == "01/07":
        print("Comienzo de nuevo ciclo")
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))
        ingreso_total = cantidad_alumnos * arancel_por_alumno
        print(f"Ingreso total en $: {ingreso_total}")
else:
    print("No se requiere procesamiento para este nivel en este día.")
