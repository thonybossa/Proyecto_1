CÓDIGOS FUENTE Y ESQUEMÁTICOS

Este documento proporciona una descripción de los códigos fuente utilizados en el proyecto y los esquemáticos cuando aplican. A continuación se detalla cada uno de los códigos junto con su respectiva descripción.

1. Código en Python para control de GPIO:
   - Archivo: scritp_python.py
   - Descripción: Este script controla un pin GPIO en una Raspberry Pi para generar una señal de conmutación a maxima velocidad. Utiliza la biblioteca RPi.GPIO y alterna entre estados alto y bajo en el pin especificado.


2. Código en C para control de GPIO:
   - Archivo: scritp_c.c
   - Descripción: Este programa, implementado en C y compilado con la biblioteca WiringPi, controla un pin GPIO para generar una señal de conmutación rápida. Se utiliza la función pinMode() para configurar el pin y digitalWrite() para cambiar su estado.


3. Script en Bash para control de GPIO:
   - Archivo: scritp_bash.sh
   - Descripción: Este script en Bash genera una señal de conmutación en un pin GPIO mediante el acceso al sistema de archivos /sys/class/gpio. Utiliza los comandos "echo" para alternar entre los valores 1 y 0 en el pin.


4. Código en Python para lectura de sensor DS18B20:
   - Archivo: python_DS18b20.py
   - Descripción: Este script en Python interactúa con el sensor DS18B20 a través de la biblioteca w1thermsensor. Captura datos de temperatura y los almacena en un archivo CSV con marca de tiempo. La precisión de la temperatura se redondea a 2 decimales.


5. Script en Bash para lectura de sensor DS18B20:
   - Archivo: bash_DS18b20.sh
   - Descripción: Este script en Bash utiliza el sensor DS18B20 para medir la temperatura y luego almacena los datos en un archivo CSV con marca de tiempo. La temperatura se redondea a 2 decimales y se utiliza el comando "bc" para cálculos.
