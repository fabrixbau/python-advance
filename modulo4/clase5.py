import numpy as np


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros)

# Usando numpy
np_numeros = list(np.arange(1, 10))
print(np_numeros)

# Matrices
lista_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(lista_matriz)
print(matriz)
print(type(matriz))
suma = matriz[0] + matriz[1]
print(suma)

# Suma de un solo valor
suma_valor = matriz[0, 0] + matriz[1, 2]
print(suma_valor)

# Calculos estadísticos
data = np.array([12, 15, 17, 83, 34, 56, 98])

# Media
mean = np.mean(data)
print("Media : ", mean)

# Desviación estandar
std = np.std(data)
print("Desviación estandar : ", std)

# Máximos y mínimos
max_val = np.max(data)
max_index = np.argmax(data)
print("Maximo : ", max_val, " Indice : ", max_index)
