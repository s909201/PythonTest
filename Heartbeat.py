#!/usr/bin/python
# update by Morgan, 20191115
import RPi.GPIO as GPIO
import time

# Define GPIO to LED mapping
LED_Heart = 26
LED_GND = 19
GPIO.setwarnings(False)

# Main program block
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
GPIO.setup(LED_Heart, GPIO.OUT)
GPIO.setup(LED_GND, GPIO.OUT)  # as GND

GPIO.output(LED_GND, False)
GPIO.output(LED_Heart, False)
time.sleep(0.1)

while 1:
    GPIO.output(LED_Heart, True)
    time.sleep(0.01)
    GPIO.output(LED_Heart, False)
    time.sleep(0.99)

GPIO.output(LED_Heart, False)

