#!/usr/bin/python3
import RPi.GPIO as gpio
import time
b1, b2 = 27, 18
# mode : gpio.BCM | gpio.BOARD 
gpio.setmode(gpio.BCM)
#gpio.setup(pin, direction, pull_up_down)
gpio.setup(b1, gpio.IN, gpio.PUD_UP)
gpio.setup(b2, gpio.IN, gpio.PUD_UP)
#gpio.add_event_detect(pin, edge)
gpio.add_event_detect(b1, gpio.RISING)
gpio.add_event_detect(b2, gpio.FALLING)

def main():
        while True:
                if (gpio.event_detected(b1)):
                        print("b1 is pressed.")
                elif (gpio.event_detected(b2)):
                        print("b2 is pressed.")
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
