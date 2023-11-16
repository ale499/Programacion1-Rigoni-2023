class MatrizGlobal:
  def __init__(self, size):
      self.size = size
      self.matriz = [[0] * size for _ in range(size)]
      self.diagonal_elementos = []

  def crear_matriz(self):
      for i in range(self.size):
          for j in range(self.size):
              self.matriz[i][j] = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))

  def llenar_matriz_automaticamente(self):
      import random
      for i in range(self.size):
          for j in range(self.size):
              self.matriz[i][j] = random.randint(1, 99)

  def mostrar_matriz(self):
      print("Matriz:")
      for fila in self.matriz:
          print(fila)

  def extraer_elementos_diagonal(self):
      self.diagonal_elementos = [self.matriz[i][i] for i in range(self.size)]


  def mostrar_lista_diagonal(self):
      print("Lista de Elementos Diagonales:")
      print(self.diagonal_elementos)

  def calcular_promedio_diagonal(self):
      promedio = sum(self.diagonal_elementos) / self.size
      print("Promedio de Elementos Diagonales:", promedio)
      return round(promedio)

  def verificar_promedio_en_matriz(self, promedio):
      for i in range(self.size):
          for j in range(self.size):
              if self.matriz[i][j] == promedio:
                  print(f"Valor promedio encontrado en la posición ({i+1}, {j+1}).")

def main():
  while True:
      try:
          size = int(input("Ingrese el tamaño de la matriz cuadrada (número impar): "))
          if size % 2 == 1:
              break
          else:
              print("Por favor, ingrese un número impar para el tamaño.")
      except ValueError:
          print("Entrada no válida. Por favor, ingrese un número válido.")

  matriz = MatrizGlobal(size)

  while True:
      print("\nMenú:")
      print("a. Crear y asignar valores a la matriz")
      print("b. Cargar valores enteros en la matriz")
      print("c. Mostrar la matriz")
      print("d. Crear una lista con los elementos de la diagonal")
      print("e. Mostrar la lista diagonal")
      print("f. Calcular y mostrar el promedio de los elementos diagonales")
      print("g. Verificar si el valor promedio existe en la matriz original")
      print("h. Salir")

      opcion = input("Ingrese su elección (a-h): ").lower()

      if opcion == 'a':
          matriz.llenar_matriz_automaticamente()
      elif opcion == 'b':
          matriz.crear_matriz()
      elif opcion == 'c':
          matriz.mostrar_matriz()
      elif opcion == 'd':
          matriz.extraer_elementos_diagonal()
      elif opcion == 'e':
          matriz.mostrar_lista_diagonal()
      elif opcion == 'f':
          promedio = matriz.calcular_promedio_diagonal()
      elif opcion == 'g':
          matriz.verificar_promedio_en_matriz(promedio)
      elif opcion == 'h':
          print("¡Adiós!")
          break
      else:
          print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
  main()
