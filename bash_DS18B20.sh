#!/bin/bash

GPIO_PIN=4  # Cambia esto al número de pin GPIO que desees usar

while true; do
    temperature=$(cat /sys/bus/w1/devices/28-*/w1_slave | awk '/t=/ {print $10}' | sed 's/t=//')
    temperature=$(echo "scale=2; $temperature / 1000" | bc)
    current_datetime=$(date +'%Y%m%d %H%M%S')
    csv_filename=$(date +'%Y%m%d')_TEMPERATURA.csv

    echo "$current_datetime,$temperature" >> "$csv_filename"

    echo "Temperatura: $temperature°C - Fecha y Hora: $current_datetime"
    sleep 1
done