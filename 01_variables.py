# Variables - Ejercicios

# 1. Declara y asigna valores a las siguientes variables:
# name: una cadena que contenga tu nombre.
# age: un número entero que represente tu edad.
# height: un número decimal que represente tu altura en metros.
# Imprime cada variable en una línea separada.
name = "Alexandru"
age = 26
height = 1.70
print(name)
print(age)
print(height)


# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
age = str(age)
print("Tengo " + age + " años.")


# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segúin corresponda e imprímela.
is_student = True
print(is_student)


# 4. Usala función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
name = "Alexandru"
name_length = len(name)
print("La longitud de mi nombre es de: " + str(name_length) + " caracteres.")


# 5. declara tres variables en una sola línea que reresenten tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, surname, city = "Alexandru", "Moldovan", "Almería"
print("Nombre" + ": " + name, "Apellido" + ": " + surname, "Ciudad" + ": " + city)


# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
color = input("¿Cuál es tu color favorito?")
print("Tu color favorito es el " + color + ".")


# 7. Declara una variable fruit e inicializala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Pera"
print("La fruta elegida es: " + fruit)
fruit = "Manzana"
print("La fruta elegida es: " + fruit)


# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 11.99
price = int(price)
print("El precio del producto es de: " + str(price) + " € ")


# 9. Declara una variable llamada adress_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
adress = "Calle de La Paz, 13"
adress_len = len(adress)
print("La longitud de la dirección es de: " + str(adress_len) + " caracteres.")


# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone = 666999666
print(type(phone))
phone = 999666999
print(type(phone))




