#!/usr/bin/python
# created by Morgan, 20191004

import RPi.GPIO as GPIO
import os

OurMsg = "Welcome_Morgan"
filepath = "python ./lcd16x2.py"
LCD_Str = filepath + " " + OurMsg
print(LCD_Str)
os.system(LCD_Str)
