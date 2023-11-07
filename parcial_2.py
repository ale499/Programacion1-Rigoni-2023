def is_mutant(dna):
    rows = len(dna)
    cols = len(dna[0])

    def check_sequence(row, col, dr, dc):
        sequence = ""
        for _ in range(4):
            if 0 <= row < rows and 0 <= col < cols:
                sequence += dna[row][col]
                row += dr
                col += dc
            else:
                return False
        return sequence == "AAAA" or sequence == "TTTT" or sequence == "CCCC" or sequence == "GGGG"

    for row in range(rows):
        for col in range(cols):
            if (
                check_sequence(row, col, 1, 0) or  # Vertical
                check_sequence(row, col, 0, 1) or  # Horizontal
                check_sequence(row, col, 1, 1) or  # Diagonal derecha
                check_sequence(row, col, 1, -1)   # Diagonal izquierda
            ):
                return True
    return False

# Solicitar al usuario la entrada de ADN
dna = []
for i in range(6):
    while True:
        sequence = input(f"Ingrese la secuencia de ADN de la fila {i + 1}: ").upper()
        if all(base in "ATCG" for base in sequence) and len(sequence) == 6:
            dna.append(sequence)
            break
        else:
            print("La secuencia de ADN debe contener solo las letras A, T, C y G, y tener una longitud de 6.")

# Verificar si el humano es mutante
if is_mutant(dna):
    print("El humano es mutante.")
else:
    print("El humano no es mutante.")
