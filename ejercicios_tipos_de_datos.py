# Introduccion-a-la-Programacion-y-diagrama-de-flujo
Tareas 

# ejercicios con entero

# 1
edad = 25

# 2
resultado_suma = 15 + 30
print("El resultado de la suma es:", resultado_suma)

# 3
numero = int(input("Ingresa un número entero: "))
doble = numero * 2
print("El doble del número ingresado es:", doble)

# 4
diferencia = 100 - 45
print("La diferencia es:", diferencia)

# Ejercicios con Reales (Números Decimales)

# 5
precio = 19.99

# 6
promedio = (8.5 + 9.2 + 7.8) / 3
print("El promedio es:", promedio)

# 7
area = 3.14 * 2.5
print("El área calculada es:", area)

# 8
peso = float(input("Ingresa tu peso en kilogramos: "))
print("Tu peso es:", peso, "kg")


# Ejercicios con Valores Lógicos (Booleanos)
# 9
esMayor = edad > 18
print("¿Es mayor de edad?:", esMayor)

# 10
numero = int(input("Ingresa un número: "))
if numero >= 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")

# 11
llueve = True
if llueve:
    print("Debes llevar un paraguas.")
else:
    print("No necesitas paraguas.")

# 12
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("¿Son iguales los números?:", num1 == num2)


# Ejercicios con Caracteres
# 13
inicial = 'A'

# 14
letra = input("Ingresa una letra: ")
print("La letra ingresada es:", letra)

# 15
simbolo = '#'

# 16
caracter = input("Ingresa un carácter: ")
if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Es una vocal.")
else:
    print("No es una vocal.")

# Ejercicios con Cadenas (Texto)

# 17
nombre = "Tu Nombre Completo"

# 18
saludo = "Hola" + " Mundo"
print(saludo)

# 19
nombre_usuario = input("Ingresa tu nombre: ")
print(f"¡Bienvenido/a, {nombre_usuario}!")

# 20
cadena = input("Ingresa una cadena de texto: ")
print("La cadena tiene", len(cadena), "letras.")

# Ejercicios con Vectores (Arreglos)

# 21
vector = [1, 2, 3, 4, 5]
suma_vector = sum(vector)
print("La suma de los elementos del vector es:", suma_vector)

# 22
vector = [2, 4, 6, 8]
escalar = 3
vector_escalado = [x * escalar for x in vector]
print("Vector multiplicado por el escalar:", vector_escalado)


# Ejercicios con Matrices (Arreglos)
# 23
matriz_2x2 = [[1, 2], [3, 4]]
promedio_matriz = sum(sum(fila) for fila in matriz_2x2) / 4
print("El promedio de los elementos de la matriz es:", promedio_matriz)

# 24
matriz_2x3 = [[1, 2, 3], [4, 5, 6]]
transpuesta = list(zip(*matriz_2x3))
print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)
