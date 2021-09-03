#!/usr/bin/python3
import RPi.GPIO as gpio
import time
# gpio led pins
leds = [19, 16, 12]
gpio.setmode(gpio.BCM)
for led in leds:
        gpio.setup(led, gpio.OUT)
def main() :
        while True :
                for led in leds:
                        gpio.output(led,gpio.LOW)
                        time.sleep(0.1)
                        gpio.output(led,gpio.HIGH)
                        #time.sleep(0.1)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()

