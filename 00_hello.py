# Esto es un comentario: Hola mundo
# Nuestro "Hola mundo" en Python

"""
Este es un
comentario en 
varias líneas
"""

print("Hola mundo")


# Consultar el tipo de dato
print (type("Hola Python")) # Dato tipo str
print (type(5)) # Dato tipo int
print (type(1 + 2j)) # Dato tipo complex
print (type(1.5)) # Dato tipo float
print (type(False)) # Dato tipo bool



# Ejercicio 00 - Hello World
# 1. Imprime "¡Hola Mundo! por consola.
print("¡Hola Mundo!")

# 2. Escribe un comentario de una sola línea explicando qué hace el código del ejercicio 1.
# El código del ejercicio 1 imprime "¡Hola Mundo!" en la consola.

# 3. Imprime tu nombre y la edad en la misma línea utilizando la función print.
print("Mi nombre es Alexandru y tengo 26 años.")

# 4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, u  número entero y un número decimal.
print(type("Test")) # Dato tipo str
print(type(10)) # Dato de tipo int
print(type(20.5)) # Dato de tipo float

# 5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
"""
Los tipos de datos en Python son
categorías que definen la naturaleza
de los datos que se pueden almacenar
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print("Hola" + " " + "Mundo") # Resultado: Hola Mundo

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime amblas en la misma línea.
nombre = "Alexandru"
edad = 26
print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años.")

# 8. Escribe un programa que solicite al usuario su nombre y lo imrpima junto con un saludo.
nombre_usuario = input("¿Cuál es tu nombre?")
print("Hola" + " " + nombre_usuario + "! Bienvenido al curso de Python.")

# 9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.
numero1 =8 # Se define la variable numero 1 y se la asigna un valor, 8.
numero2 = 10 # Se define la variable numero 2 y se le asigna un valor, 10.
suma = numero1 + numero2 # Se define la variable suma y se le añade el resultado de la suma de las variables numero1 y numero2.
print("La suma de " + str(numero1) + " y " +str(numero2) + " es: " + str(suma)) # Se imprime el resultado de la suma de las variables.

# 10. Comenta el código del ejercicio 9, y explica qué hace cada l´çinea usando comentarios en una sola línea.
