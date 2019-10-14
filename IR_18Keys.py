#!/usr/bin/python
# created by Morgan, 20191014
import RPi.GPIO as GPIO
import time
import os

GPIO_IR = 22


def setup():
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(GPIO_IR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time.time()
    results = []
    while (time.time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime / 1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i - 1]) or (i == len(data) - 1):
            pulses.append((data[i - 1], int((i - i_break) / rate * 1e6)))
            i_break = i
    # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None


def destroy():
    GPIO.cleanup()


# LCD Show
def LCD_SHOW(IRMsg):
    filepath = "python ./lcd16x2.py"
    LCD_Str = filepath + " " + IRMsg
    print(LCD_Str)
    os.system(LCD_Str)


if __name__ == "__main__":
    setup()
    try:
        print("Starting IR Listener")
        LCD_SHOW("IR_RECEIVER_TEST")
        while True:
            print("Waiting for signal")
            GPIO.wait_for_edge(GPIO_IR, GPIO.FALLING)
            code = on_ir_receive(GPIO_IR)
            if code:
                print(str(hex(code)))
                LCD_SHOW("IR_RECEIVER_TEST" + str(hex(code)))
            else:
                print("Invalid code")
                LCD_SHOW("IR_RECEIVER_TESTInvalid code")
    except KeyboardInterrupt:
        pass
    except RuntimeError:
        # this gets thrown when control C gets pressed
        # because wait_for_edge doesn't properly pass this on
        pass
    print("Quitting")
    destroy()

