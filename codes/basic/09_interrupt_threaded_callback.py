#!/usr/bin/python3
import RPi.GPIO as gpio, time
b1, b2 = 27, 18
gpio.setmode(gpio.BCM)
#gpio.setup(pin, direction, pull_up_down)
gpio.setup(b1, gpio.IN, gpio.PUD_UP)
gpio.setup(b2, gpio.IN, gpio.PUD_UP)

def onB1(arg):
         print("b1 is pressed.")
def onB2(arg):
         print("b2 is pressed.")
def main():
        #gpio.add_event_detect( 
        #       pin,edge,callback,bouncetime)
        gpio.add_event_detect(
                b1, gpio.RISING, onB1, 300)
        gpio.add_event_detect(
                b2, gpio.FALLING, onB2, 300)
        while True:
              pass
try:
        main()
except KeyboardInterrupt:
       pass
except Exception as exception:
        print(exception)
finally:
        gpio.remove_event_detect(b1)
        gpio.remove_event_detect(b2)
        gpio.cleanup()
