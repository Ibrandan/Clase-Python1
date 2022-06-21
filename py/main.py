# #  Numeros enteros (int) y operadores +, -, *, /, //, %, **

# print("Numeros enteros")

# # Suma
# print(2 + 2)

# # Resta
# print(5 - 3)

# # Multiplicacion
# print(21 * 3)

# # Division
# print(12 / 6)
# print(12 // 6)

# # Modulo
# print(12 // 6)

# # Potencia
# print(3 ** 2)
# print(2 ** 5)


# # Casteo o conversión
# print(int("3"))
# print(int(3.141516))

# print("Numeros reales")
# print(2 + 2)
# print(5 - 3)
# print(21 * 3)
# print(12 / 6)
# print(2 ** 5)

# print(float(4))

# # Strings

# print("vamos",  "vamos", "Argentina")
# nombre = 'Ignacio'
# print(f'Hola {nombre}')  # f-string

# # Variables
# ancho = 12
# largo = 5

# print(ancho * largo)

# prefijo = "Mc"
# apellido = "donalda's"

# print(prefijo + apellido)

palabra = "Argentina"
#                012345678

print(palabra[0])
print(palabra[5])

print(palabra[-1])
print(palabra[-2])

print(palabra[0:5])
print(palabra[5:9])
print(palabra[5:10])

print(palabra[:5])  # --> palabra[0:5
print(palabra[:5] + palabra[5:])
print(palabra[-4:])

print(palabra[1:9:2])  # palabra[1: :2]
print(palabra[1::2])  # --> array [star:stop:step]

# for idx, elem in enumerate(palabra):
#     if idx % 2 == 1:
#         print(idx, elem)

# i = 0
# while i < len(palabra):
#     if i % 2 == i:
#         print(i, palabra[i])
#     i += 1  # i++ no existei

print("Funciones para trabajar con cadenas de texto")

print(len(palabra))
palabraMinuscula = palabra.lower()
print(len(palabraMinuscula))

palabraMayuscula = palabra.upper()
print(len(palabraMayuscula))

palabraCapitalizada = "Argentina es linda".capitalize()
print(palabraCapitalizada)

print(str(3.455))

print(type(17))
print(type(17.0))
print(type(palabra))

print("Tipos de datos logicos")

print(5 == 6)
print(5 == 5)
print(5 != 7)
print(5 == "5")

print(5 > 7)
print(5 < 7)
print(5 >= 7)
print(5 <= 7)

# AND y OR
print(5 > 4 and 3 > 2)
print(5 > 4 or 5 < 3)
print(5 > 4)
print(not 5 > 4)
