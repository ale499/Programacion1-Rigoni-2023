name = input("Por favor, introduce tu nombre: ")
print(f"¡Hola, {name}!")

while True:
    # Menú de opciones
    print("\nMenú de opciones:")
    print("1. Juego de números")
    print("2. Juego de palabras")
    print("0. Salir")

    option = input("Por favor, elige una opción: ")

    if option == "1":
        # Juego de números
        numbers = []
        while True:
            number = int(input("Introduce un número entero (o 0 para salir): "))
            if number == 0:
                break
            numbers.append(number)

        # Encontrar el mayor número par
        even_numbers = [num for num in numbers if num % 2 == 0]
        if even_numbers:
            largest_even_numbers = max(even_numbers)
            print(f"El mayor número par es: {largest_even_numbers}")
        else:
            print("No ingresaste números pares.")

        # Promedio de los números impares
        odd_numbers = [num for num in numbers if num % 2 != 0]
        if odd_numbers:
            average_odd_numbers = sum(odd_numbers) / len(odd_numbers)
            print(f"El promedio de los números impares es: {average_odd_numbers:.2f}")
        else:
            print("No ingresaste números impares.")

    elif option == "2":
        # Juego de palabras
        phrase = input("Introduce una frase: ")

        vowels = "aeiou"
        vowels_count = {vowels: phrase.lower().count(vowels) for vowels in vowels}

        # Mostrar el resultado
        print("Cantidad de vocales en la frase:")
        for vowels, count in vowels_count.items():
            print(f"{vowels}: {count}")

    elif option == "0":
        # Finalizacion de programa
        print("¡Hasta luego, gracias por jugar!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción válida.")
