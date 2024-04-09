# concatenación
cadena1 = "mi edad es "
cadena2 = 28
resultado = cadena1 + str(cadena2)
print(resultado.upper())

# nombre = input("Ingresa tu nombre : ")
# apellido = input("ingressa tu apellido : ")
# # print(("Hola mi nombre es " + nombre + " " + apellido))

# #  f-strings
# edad = int(input("Edad : "))
# saludo = f"hola mi nombre es {nombre} {apellido} y tengo {edad} años"
# print(saludo)

# concatenar con números
numeros = [1, 2, 3, 4, 5]
resultado = ""
for num in numeros:
    resultado += str(num) + " "
print(resultado)

# concatenación con join
palabras = ["Hola", "mundo", "python"]
frase = " ".join(palabras)
print(frase)
