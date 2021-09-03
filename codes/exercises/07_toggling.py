#!/usr/bin/python3
import RPi.GPIO as gpio
import time
f0 = f1 = f2 = False
# gpio led pins
leds = [19, 16, 12]
btns = [27, 18, 17]
# mode : gpio.BCM | gpio.BOARD 
gpio.setmode(gpio.BCM)
for led in leds : gpio.setup(led, gpio.OUT)
for btn in btns : gpio.setup(btn, gpio.IN, gpio.PUD_UP)

def onPressedB1(arg):
        global f0
        if (f0) :
            gpio.output(leds[0], gpio.HIGH)
        else :
            gpio.output(leds[0], gpio.LOW)
        f0 = not f0

def onPressedB2(arg):
        global f1
        if (f1) :
            gpio.output(leds[1], gpio.HIGH)
        else :
            gpio.output(leds[1], gpio.LOW)
        f1 = not f1

def onPressedB3(arg):
        global f2
        if (f2) :
            gpio.output(leds[2], gpio.HIGH)
        else :
            gpio.output(leds[2], gpio.LOW)
        f2 = not f2

def main():
        #gpio.add_event_detect( 
        #       pin,edge,callback,bouncetime)
        gpio.add_event_detect(
                btns[0], gpio.RISING, onPressedB1, 300)
        gpio.add_event_detect(
                btns[1], gpio.RISING, onPressedB2, 300)
        gpio.add_event_detect(
                btns[2], gpio.RISING, onPressedB3, 300)
        while True:
              pass
try:
        main()
except KeyboardInterrupt:
       pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
