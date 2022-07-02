#  Numeros enteros (int) y operadores +, -, *, /, //, %, **

print("Numeros enteros")

# Suma
print(2 + 2)

# Resta
print(5 - 3)

# Multiplicacion
print(21 * 3)

# Division
print(12 / 6)
print(12 // 6)

# Modulo
print(12 // 6)

# Potencia
print(3 ** 2)
print(2 ** 5)


# Casteo o conversión
print(int("3"))
print(int(3.141516))

print("Numeros reales")
print(2 + 2)
print(5 - 3)
print(21 * 3)
print(12 / 6)
print(2 ** 5)
print(3.4 ** 2.2)

print(float("3.13555"))
print(float(4))

# Strings

print("cadena de caracteres")  # --> Comillas dobles " "
print('agua y aceite')  # --> Comillas simples ' '
print('McDonal\'s')  # --> Para que se pueda usar la comilla simple, debemos escaparla con \
print("McDonal's")  # --> Para que se pueda usar la comilla simple, otra opcion es cerrar con comillas dobles
print("\"McDonal's\"")  # --> Para que se puedan usar las comillas dobles, debemos escaparlas con \

# --> Este string se va a imprimir con un salto de linea ' \n '
print("c:\nueva\carpeta")
# Para escribir la ruta sin el salto de linea debemos agregar ' r ' antes del string
print(r"c:\nueva\carpeta")

print(""""Cadena de texto
con mas de una linea""")   # --> Con las tres comillas declaamos un string multilinea, agrega saltos de linea

print(""""Cadena de texto \
con mas de una linea""")   # --> Para no tener saltos de linea debemos agregar la barra

print(3 * 'string')  # --> Multiplica el string 3 veces
print(3 * 'la' + 'larala')

# --> Print puede recibir varios parametros, cuando se separa por coma se agrega un espacio entre los valores
print("vamos",  "vamos", "Argentina")

nombre = 'Ignacio'
print(f'Hola {nombre}')  # f-string remplaza a los backtitcks de JS

# Variables
ancho = 12
largo = 5

print(ancho * largo)

prefijo = "Mc"
apellido = "donald's"

print(prefijo + apellido)

palabra = "Argentina"
#                012345678

print(palabra[0])  # --> Imprime la primera letra de ' palabra '
print(palabra[5])  # --> Imprime la primera letra de ' palabra '

print(palabra[-1])  # --> Imprime la ultima letra de ' palabra '
print(palabra[-2])  # --> Imprime la penultima letra de ' palabra '

# --> imprime desde la letra ubicada en 0 hasta la 4, excluyendo el 5
print(palabra[0:5])
# --> imprime desde la letra ubicada en 5 hasta la 9, excluyendo el 10
print(palabra[5:10])

# --> = palabra[0:5]  Comienza desde el 0 aunque no este escrito
print(palabra[:5])
print(palabra[:5] + palabra[5:])
print(palabra[-4:])  # --> imprime desde la transantrepenultima hasta el final

# palabra[1: :2] Imprime desde la letra ubicada en 2da pos hasta la letra ubicada en la pos 10 salteando una / numeros impares
print(palabra[1:9:2])
print(palabra[1::2])  # --> array [star:stop:step]
# -->array[0:9:2]  Imprime desde la letra ubicada en la 1ra pos hasta la letra ubicada en la pos 10 salteando una / numeros pares
print(palabra[::2])

# for idx, elem in enumerate(palabra):
#     # ----> Imprime el indice y el elemento
#     print(idx, elem)


# for idx, elem in enumerate(palabra):
#     if idx % 2 == 1:                              # ----> Imprime los valores impares
#         print(idx, elem)                          #

# i = 0
# while i < len(palabra):                       #
#     if i % 2 == i:                                  # ----> Imprime los valores impares
#         print(i, palabra[i])                      #
#     i += 1  # i++ de js no existe

print("Funciones para trabajar con cadenas de texto")

print(len(palabra))  # ----->

palabraMinuscula = palabra.lower()
print(len(palabraMinuscula))

palabraMayuscula = palabra.upper()
print(len(palabraMayuscula))

palabraCapitalizada = "argentina es linda".capitalize()
print(palabraCapitalizada)

print(str(3.455))  # --> Crea un nuevo str del objeto que se ingresa en el prametro


#  print(type()) ---> Imprime por pantalla de que clase es el dato ingresado por parametro
print(type(17))
print(type(17.0))
print(type(palabra)) 

print("Tipos de datos logicos")

print(5 == 6)  # ¿ 5 es igual a 6?  ----> False
print(5 == 5) # ¿ 5 es igual a 5?  ----> True
print(5 != 7) # ¿ 5 es  distinto de 7?  ----> True
print(5 == "5") # ¿ 5 es igual a '5'?  ----> False

print(5 > 7) # ¿ 5 es  mayor a 7?  ----> False
print(5 < 7) # ¿ 5 es  menor a 7?  ----> True
print(5 >= 7) # ¿ 5 es  mayor o igual a 7?  ----> False
print(5 <= 7) # ¿ 5 es  menor o igual a 7?  ----> True

# AND y OR
print(5 > 4 and 3 > 2) # Conjuncion: Todos los valores deben ser verdadores para que el resultado sea verdadero
print(5 > 4 or 5 < 3) # Disyuncion: Mientra que uno de los valores sea verdadore, el resultado es verdadero
print(not 5 > 4) # Negacion:
