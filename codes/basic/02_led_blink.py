#!/usr/bin/python3
import RPi.GPIO as gpio, time
# gpio led pins
p1, p2, p3 = 19, 16, 12
gpio.setmode(gpio.BCM)
gpio.setup(p1, gpio.OUT)
gpio.setup(p2, gpio.OUT)
gpio.setup(p3, gpio.OUT)
def main() :
        while True :
                gpio.output(p1,gpio.LOW)
                gpio.output(p2,gpio.LOW)
                gpio.output(p3,gpio.LOW)
                time.sleep(0.5)
                gpio.output(p1,gpio.HIGH)
                gpio.output(p2,gpio.HIGH)
                gpio.output(p3,gpio.HIGH)
                time.sleep(0.5)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()

