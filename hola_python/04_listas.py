# Una lista o array es una estructura de datos que permite almacenar múltiples valores
# en una sola variable. Pueden cambiar su tamaño y contenido dinámicamente.

# Ejerecicios Listas.

# 1. Crea una lista con los números del 1 al 5 e imprímela.

numeros = [1, 2, 3, 4, 5]
print(numeros)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50]

numeros = [10, 20, 30, 40, 50]
print(numeros[2])


# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.

numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros.append(6)
print(numeros)


# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].

numeros = [10, 20, 30, 40, 50]
print(numeros)
numeros.insert(2, 15)
print(numeros)


# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50]

numeros = [10, 20, 30, 30, 40, 50]
print(numeros)
numeros.remove(30)
print(numeros)


# 6. Usa la función pop() para eliminar el último elemento de la lista [10, 20, 30, 40, 50], almacénalo en una variable. Imprime la variable y la lista.
numeros = [10, 20, 30, 40, 50]
print(numeros)
numeros.pop()
print(numeros)
my_variable = numeros
print(my_variable)

# 7. Invierte una lista [100, 200, 300, 400, 500] e imprímela.
numeros = [100, 200, 300, 400, 500]
print(numeros)
numeros.reverse()
print(numeros)


# 8. Ordena a lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
numeros = [3, 1, 4, 2, 5]
print(numeros)
numeros.sort()
print(numeros)


# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista e imprímela.
numeros1 = [1, 2, 3]
print(numeros1)
numeros2 = [4, 5, 6]
print(numeros2)
numeros3 = numeros1 + numeros2
print(numeros3)


# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3)
numeros = [10, 20, 30, 40, 50]
print(numeros)
sublista = numeros[1:3]
print(sublista)