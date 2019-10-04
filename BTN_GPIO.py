#!/usr/bin/python
# update by Morgan, 20191004
import RPi.GPIO as GPIO
import time
import os

# Pin definition
BTN_1 = 16
BTN_2 = 20
BTN_3 = 21

LED_1 = 13
LED_2 = 26
LED_GND = 19
GPIO.setwarnings(False)

# Main program block
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
GPIO.setup(BTN_1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BTN_2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BTN_3, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_GND, GPIO.OUT)  # as GND
GPIO.output(LED_GND, False)  # as GND


def LCD_SHOW(Msg):
    filepath = "python ./lcd16x2.py"
    LCD_Str = filepath + " " + Msg
    print(LCD_Str)
    os.system(LCD_Str)


def BTN_2_callback(channel):
    print("BTN 2 pressed. This is a edge event callback function!")
    LCD_SHOW("BTN_2_Pressed")


def BTN_3_callback(channel):
    print("BTN 3 pressed. This is a edge event callback function!")
    LCD_SHOW("BTN_3_Pressed")


GPIO.add_event_detect(BTN_1, GPIO.FALLING)

GPIO.add_event_detect(BTN_2, GPIO.FALLING)
GPIO.add_event_callback(BTN_2, BTN_2_callback)
GPIO.add_event_detect(BTN_3, GPIO.FALLING)
GPIO.add_event_callback(BTN_3, BTN_3_callback)

while True:
    # Blocking process
    # value1 = GPIO.input(BTN_1)
    # GPIO.output(LED_1, value1)
    # time.sleep(0.1)

    if GPIO.event_detected(BTN_1):
        print("BTN 1 pressed")

# press Ctrl+Z , leave the program

