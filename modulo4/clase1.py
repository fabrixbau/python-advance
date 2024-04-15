import math
from fractions import Fraction
from decimal import Decimal
from decimal import getcontext


# Constantes matemáticas
print("pi : ", math.pi)
print("Número de Euler", math.e)


# Funciones trigonométricas
angulo = math.radians(45)
print(angulo)
print("Seno : ", math.sin(angulo))
print("Coseno : ", math.cos(angulo))
print("Tangente : ", math.tan(angulo))


# Funciones exponenciales
print("Eponencial (e °2)", math.exp(2))

# Funciones logarítmicas
print("Log de 10 : ", math.log(10))

# Potencias
print("2 elevado al cubo : ", math.pow(2, 3))

# raices
print("Raíz cuadrada de 25", math.sqrt(25))

# Fracciones
frac1 = Fraction(3, 4)
frac2 = Fraction(1, 6)

suma = frac1 + frac2
resta = frac1 - frac2
multiplicacion = frac1 * frac2
division = frac1 / frac2

print("Suma : ", suma)
print("Resta : ", resta)
print("Multiplicación : ", multiplicacion)
print("División : ", division)

getcontext().prec = 10

num1 = Decimal("0.000001")
num2 = Decimal("0.000222")

suma_decimal = num1 + num2

print("Suma decimal : ", suma_decimal)
