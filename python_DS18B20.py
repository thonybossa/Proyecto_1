#!/usr/bin/env python

import time
import csv
from datetime import datetime
from w1thermsensor import W1ThermSensor

# Ruta del archivo CSV
csv_filename = datetime.now().strftime("%Y%m%d") + "_TEMPERATURA.csv"

# Configuración del sensor DS18B20
sensor = W1ThermSensor()

try:
    while True:
        temperature = sensor.get_temperature()
        temperature = round(temperature, 2)  # Redondear a 2 decimales
        current_datetime = datetime.now().strftime("%Y%m%d %H%M%S")

        with open(csv_filename, mode='a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([current_datetime, temperature])

        print(f"Temperatura: {temperature}°C - Fecha y Hora: {current_datetime}")
        time.sleep(10)  # Esperar 10 segundos

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")