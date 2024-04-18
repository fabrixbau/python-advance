from geometria import area
from geometria.perimetros import (
    perimetro_cuadrado,
    perimetro_circulo,
    perimetro_rectangulo
)


area = area.area_cuadrado(4)
perimetro = perimetro_cuadrado(4)
circulo = perimetro_circulo(5)
rectangulo = perimetro_rectangulo(4, 8)

print("AREA DEL CUADRADO : ", area)
print("PERIMETRO DEL CUADRADO : ", perimetro)
print("PERIMETRO DEL CIRCULO : ", round(circulo, 2))
print("PERIMETRO DEL RECTANGULO : ", rectangulo)
