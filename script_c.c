#include <stdio.h>
#include <wiringPi.h>

#define GPIO_PIN 8  // Cambia esto al número de pin GPIO que desees usar

int main(void) {
    if (wiringPiSetup() == -1)
        return 1;

    pinMode(GPIO_PIN, OUTPUT);

    while (1) {
        digitalWrite(GPIO_PIN, HIGH);
        digitalWrite(GPIO_PIN, LOW);
        }

    return 0;
}