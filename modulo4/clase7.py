import datetime


def dia_nacimiento(fecha_nacimiento):
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes',
            'sábado', 'domingo']
    index_dia = fecha_nacimiento.weekday()
    return dias[index_dia]


if __name__ == '__main__':
    fecha_string = input("Ingrese fecha de nacimiento (YYYY-MM-DD) : ")
    fecha_objeto = datetime.datetime.strptime(fecha_string, "%Y-%m-%d")
    dia = dia_nacimiento(fecha_objeto)
    print(f"Naciste un {dia}")
