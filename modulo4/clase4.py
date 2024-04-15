import datetime
import pytz


fecha_hora_actual = datetime.datetime.now()
print("La fecha y hora actual : ", fecha_hora_actual)


# Formatear una fecha y hora
formato = "%d/%m/%Y %H:%M:%S"
fecha_formato = fecha_hora_actual.strftime(formato)
print("La fecha formateada : ", fecha_formato)

# Fecha especifica
fecha_especifica = datetime.datetime(2022, 8, 1, 12, 15, 30, 0)
print("Fecha y hora específica : ", fecha_especifica.strftime(formato))

# Calculos con fechas
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=23)
diff_dates = tomorrow - today
print("Mañana es : ", tomorrow)
print("Faltan", diff_dates.days, "días")

# Zonas horarias
zona_horaria = pytz.timezone("America/New_york")
fecha_hora_actual = datetime.datetime.now(zona_horaria)
print("Fecha y hora en New York: ", fecha_hora_actual)

# Convertir string a fecha
fecha_string = "2023-07-12 18:30:00"
fecha_objeto = datetime.datetime.strptime(fecha_string, "%Y-%m-%d %H:%M:%S")
print("Fecha y hora conveetida", fecha_objeto)
