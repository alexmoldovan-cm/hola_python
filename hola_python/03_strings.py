# Strings #

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)


my_new_line_string = "Este es un String\ncon un salto de línea"
print(my_new_line_string)

my_tab_string = "Este es un String\tcon un tabulador"
print(my_tab_string)

my_scape_string = "Este es un String\\con una barra invertida" # Sirve para escapar caracteres.
print(my_scape_string)


# Formateo #

name, surname, age = "Alex", "Moldovan", 26
print("Mi nombre es {} {}, y tengo {} años".format(name, surname, age))
print("Mi nombre es %s %s, y mi edad es %d" % (name, surname, age))
print(f"Mi nombre es {name} {surname}, y tengo {age} años") # Formato f-string (Python 3.6+)


# Desempaqueado de caracteres #

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División #

language_slice = language[1:3] # Sirve para dividir cadenas de texto
print(language_slice) # Imprime "yt"

language_slice = language[1:] # Imprime "ython"
print(language_slice) # Imprime "ython"

language_slice = language[-2]
print(language_slice) # Imprime "o"

language_slice = language[0:6:2]
print(language_slice) # Imprime "pto"


# Reverso #

reversed_language = language[::-1] # Reversa la cadena de texto
print(reversed_language) # Imprime "nohtyp"

# Funciones del lenguaje #

print(language.capitalize()) # Capitaliza la primera letra de la cadena
print(language.upper()) # Convierte la cadena a mayúsculas
print(language.lower()) # Convierte la cadena a minúsculas
print(language.count("o")) # Cuenta la cantidad de veces que aparece un caracter en la cadena
print(language.find("o")) # Encuentra la posición de un caracter en la cadena
print(language.index("o")) # Encuentra la posición de un caracter en la cadena
print(language.replace("o", "a")) # Reemplaza un caracter por otro en la cadena
print(language.split("o")) # Divide la cadena en una lista de cadenas
print(language.split("o", 1)) # Divide la cadena en una lista de cadenas, pero solo una vez
print(language.lower().isupper()) # Verifica si la cadena está en mayúsculas
print(language.startswith("Py")) # Es falso porque la cadena no empieza con "Py" sino con "py"
print("Py" == "py") # No es lo mismo