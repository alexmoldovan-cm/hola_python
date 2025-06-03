# Ejercicios con tuplas

# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
my_tupla = (10, 20, 30, 40, 50)
print(my_tupla)


# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
my_second_tupla = (100, 200, 300, 400, 500)
print(my_second_tupla[1])


# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3,) a 10 y observa el resultado.
my_third_tupla = (1, 2, 3)
try:
    my_third_tupla[0] = 10
except TypeError as e:
    print(f"Error: {e}. Las tuplas son inmutables y no se pueden modificar.")


# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3) e imprímelo.
my_fourth_tupla = (1, 2, 3, 3, 4, 5, 3)
count_3 = my_fourth_tupla.count(3)
print(f"El número 3 aparece {count_3} veces en la tupla.")


# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
my_fifth_tupla = ("Java", "Python", "JavaScript", "Python")
index_python = my_fifth_tupla.index("Python")
print(f"La cadena 'Python' se encuentra en el índice {index_python} de la tupla.")


# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
my_sixth_tupla1 = (1, 2, 3)
my_sixth_tupla2 = (4, 5, 6)
concatenated_tupla = my_sixth_tupla1 + my_sixth_tupla2
print(f"La tupla concatenada es: {concatenated_tupla}")


# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
my_tupla = (10, 20, 30, 40, 50)
subtupla = my_tupla[2:4]
print(f"La subtupla desde la posición 2 hasta la 4 es: {subtupla}")


# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en tupla.
my_eighth_tupla = ("rojo", "verde", "azul")
my_eighth_list = list(my_eighth_tupla)
my_eighth_list[1] = "amarillo"
my_eighth_tupla = tuple(my_eighth_list)
print(f"La tupla después de convertirla a lista y modificar es: {my_eighth_tupla}")


# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1, 2, 3, 4, 5)
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print(f"Error: {e}. La tupla my_tuple ha sido eliminada y ya no existe.")


# 10. Crea una tupla con un solo elemento (100) e imprímela. Asegúrate de incluir la sintaxis correcta para crear una tupla de un solo elemento.
my_single_element_tupla = (100,)  # Nota la coma al final para indicar que es una tupla de un solo elemento
print(f"La tupla con un solo elemento es: {my_single_element_tupla}")