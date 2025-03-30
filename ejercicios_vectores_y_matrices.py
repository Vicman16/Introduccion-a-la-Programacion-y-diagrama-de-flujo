#  Ejercicio 1
# Realizar un programa que defina un vector llamado "vector_numeros" de 10 enteros, a continuación lo inicialice con valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.

import random

# Definir el vector llamado "vector_numeros"
vector_numeros = [random.randint(1, 10) for _ in range(10)]

# Mostrar cada elemento del vector junto con su cuadrado y su cubo
print("Elemento | Cuadrado | Cubo")
print("---------------------------")
for numero in vector_numeros:
    cuadrado = numero ** 2
    cubo = numero ** 3
    print(f"{numero:8} | {cuadrado:8} | {cubo:8}")



# ejercicios 2
# Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado. Copia los elementos del vector en otro vector pero en orden inverso, y muéstralo por la pantalla.

# Crear un vector de 5 elementos de cadenas de caracteres
vector_original = []

# Inicializar el vector con datos leídos por teclado
for i in range(5):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    vector_original.append(elemento)

# Copiar los elementos en otro vector en orden inverso
vector_inverso = vector_original[::-1]

# Mostrar el vector inverso en pantalla
print("Vector original:", vector_original)
print("Vector inverso:", vector_inverso)


# ejercio 3 
# Diseñar el algoritmo correspondiente a un programa, que
# Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

# Crear la tabla bidimensional 5x5 llamada "matriz"
# Crear la tabla bidimensional 5x5 llamada "matriz"
matriz = []

# Cargar la tabla con valores numéricos enteros ingresados por el usuario
print("Por favor, ingrese los valores de la matriz:")
for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Sumar los elementos de cada fila
print("\nSuma de los elementos de cada fila:")
for i in range(5):
    suma_fila = sum(matriz[i])
    print(f"Suma de la fila {i + 1}: {suma_fila}")

# Sumar los elementos de cada columna
print("\nSuma de los elementos de cada columna:")
for j in range(5):
    suma_columna = sum(matriz[i][j] for i in range(5))
    print(f"Suma de la columna {j + 1}: {suma_columna}")
