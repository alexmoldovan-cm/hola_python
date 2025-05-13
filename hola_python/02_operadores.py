# Operadores - Explicaciones.

# Operadores aritméticos #

print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (10 % 3)
print (10 // 3)
print (2 ** 3)
print (2 ** 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto

print ("Hola " + "Python " + "¿Qué tal?")
print ("Hola " + str(5))


# Operaciones mixtas

print ("Hola " * 5)
print ("Hola " * (2 ** 3))

my_float = 2.5 * 2 # Creamos una variable para un número float y lo multiplicamos por 2.
print ("Hola " * int(my_float)) # Convertimos el número float a un número entero y lo multiplicamos por "Hola".


# Operadores comparativos #

# Operaciones con enteros

print (3 > 4)
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4)

# Operaciones con cadenas de texto

print ("Hola" > "Python")
print ("Hola" < "Python")
print ("aaaa" >= "abaa") #Ordenación alfabética por ASCII.
print (len("aaaa") >= len("abaa")) #Cuenta caracteres.
print ("Hola" <= "Python")
print ("Hola" == "Python")
print ("Hola" != "Python")


# Operadores lógicos #

#Explicación álgebra de Boole
# True or True = True      # False or False = False
# True or False = True    # False or True = True

print (3 > 4 and "Hola" > "Python") # False
print (3 > 4 or "Hola" > "Python") # False
print (3 < 4 and "Hola" < "Python") # True
print (3 < 4 or "Hola" > "Python") # True
print (3 < 4 or ("Hola" > "Python" and 4 == 4)) # True
print (not (3 > 4)) # True
