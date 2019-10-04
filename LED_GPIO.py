#!/usr/bin/python
# update by Morgan, 20191004
import RPi.GPIO as GPIO
import time
import os

# Define GPIO to LED mapping
LED_1 = 13
LED_2 = 26
LED_GND = 19
GPIO.setwarnings(False)

# Main program block
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_GND, GPIO.OUT)  # as GND

GPIO.output(LED_GND, False)
GPIO.output(LED_1, True)
GPIO.output(LED_2, True)
time.sleep(1)

count = 0
while count < 6:
    GPIO.output(LED_1, True)
    GPIO.output(LED_2, False)
    time.sleep(0.25)
    GPIO.output(LED_1, False)
    GPIO.output(LED_2, True)
    time.sleep(0.25)
    count = count + 1

GPIO.output(LED_1, False)
GPIO.output(LED_2, False)

# LCD Show
OurMsg = "LED_GPIO_TEST"
filepath = "python ./lcd16x2.py"
LCD_Str = filepath + " " + OurMsg
print(LCD_Str)
os.system(LCD_Str)
