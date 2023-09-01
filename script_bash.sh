#!/bin/bash

while true;
do
    echo "1"> /sys/class/gpio/gpio18/value
    echo "0"> /sys/class/gpio/gpio18/value
done