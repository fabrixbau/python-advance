from datetime import datetime


name = "Fabrizio"
age = 30
print(f"Mi nombre es {name} y tengo {age} años")
print("Mi nombre es {} y tengo {} años".format(name, age+10))

sql_insert = ("insert into users(name, age) values ('{}, '{}')"
              .format(name, age))
print("Nombre : {1}, Edad : {0}".format(age, name))

# print con parametros
producto = "Celular Iphone 12"
precio = 599.99

print(("Producto : {prod}, Precio : {pre:.2f}"
       .format(prod=producto, pre=precio)))

#  Formatear numeros
num = 12345.6889
print("{:.2f}".format(num))
print("{:,}".format(num))
print("{:e}".format(num))

# Formatear fechas
now = datetime.now()
print("Fecha y hora : {:%d/%m/%Y %H:%M:%S}".format(now))

# Alineación y relleno
number = 42
print("Número : {:>10}".format(number))
print("Número : {:0<5}".format(number))
