# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usandoo la función len().
text = "Aprendiendo Python"
print(len(text))


# 2. Concatena dos cadenas: "Hola" y "Phyton" y muestra el resultado en una sola línea.
saludo= "Hola"
lenguaje= "Phyton"
print(saludo + " " + lenguaje)


# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
saludo= "Hola\nPhyton"
print(saludo)


# 4. Usa el formato de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre = "Alex"
apellido = "Moldovan"
edad = 26
print(f"Mi nombres es {nombre} {apellido}, y tengo {edad} años")


# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprímelas uno por uno.
palabra= "Python"
a, b, c, d, e, f = palabra
print(palabra)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# 6. Extrae un slice de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.
lenguaje= "Programación"
slice = lenguaje[3:8]
print(slice)


 # 7. Invierte la cadena "Python" y muéstrala en pantalla.
palabra_nueva= "Python"
palabra_invertida= palabra_nueva[::-1]
print(palabra_invertida)


# 8. convierte la cadena "Aprendiendo Python" en maýsculas usando el método adecuado e imprímela.
cadena= "Aprendiendo Python"
cadena_mayusculas= cadena.upper()
print(cadena_mayusculas)


# 9. Cuenta cuántas veces aparece la letra "a" en la palabra "Programación" y muéstralo en pantalla.
otra_palabra= "Programación"
contador= otra_palabra.count("a")
print(contador)


# 10. Verifica si la cadenaa "12345" es numérica usando el método adecuado e imprímelo.
cadena_numerica= "12345"
es_numerica= cadena_numerica.isnumeric()
print(es_numerica)

