### Dates ###
"""
En dates se va a ver lo que son las Fechas y sus manejos
hora, dia, horas, minutos, segundos, etc
"""

# === Importacion de date ===
from datetime import datetime # o mas general: import datetime
from datetime import time # esto es meramente cosas del propio TIEMPO
from datetime import date #
from datetime import timedelta # ESCENCIAL para trabajar con rangos de tiempo

# === Funciones utiles === ** primero revisa mas abajo, "Inicializacion de fecha"
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

# === Inicializacion de fecha === ** puede haber mas tipos de inicializaciones, now es de actual
now = datetime.now() 
current_timne = time()
#current_date = date()
time_delta = timedelta()

# === DATETIME ===
print(now.year)
print(now.month)
print(now.day)
print(now.hour)

# === Pruebas/Otros || DATETIME ===
print(datetime.hour) # no saldria nada si no tuvieramos algo inicializado
timestamp = now.timestamp() # Representar unica de un tiempo ** sirve cuando alguien registra algo en ese tiempo
print(timestamp)
year_2027 = datetime(2027, 1, 1) # lo MINIMO requerido, se puede agregar las horas tambien
print_date(year_2027)

# === TIME === ** especifica para tiempos/tiempo
current_timne = time(21, 6, 0) # esto SI o SI se debe rellenar
print(current_timne.hour)
print(current_timne.min)
print(current_timne.second)

# === DATE === ** especificas para fechas enteras
current_date = date(2026, 1, 17) # SI o SI rellenar con los datos correctos, podemos ocupar today igual...
print(current_date.year)
print(current_date.month)
print(current_date.day)

# === Pruebas/Otros || DATE ===
current_date = date(current_date.year, current_date.month + 1, current_date.day) # ejemplo de suma de mes, 1 pasa a 2.
print(current_date.month)

# === TIMEDELTA === ** Sirve para trabajar normalmente con FRANGAS o RANGOS de fechas establecidas
start_timedelta = timedelta(200, 100, 100, weeks = 10) # weeks, entr otros se definen dentro del mismo
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(f"Delta: ", end_timedelta - start_timedelta) # lanza una representacion en formato strings
print(end_timedelta + start_timedelta)

# === OPERACIONES SIN TIMEDELTA ===
# Operaciones con fechas
diff = year_2027 - now
print(diff)

diff = year_2027.date() - current_date
print(diff)