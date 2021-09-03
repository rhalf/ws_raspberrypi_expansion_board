#!/usr/bin/python3
import RPi.GPIO as gpio
# gpio.BCM led pins
p1, p2, p3 = 19, 16, 12
# gpio.BCM | gpio.BOARD
gpio.setmode(gpio.BCM)
#gpio.BOARD led pins
#p1, p2, p3 = 35, 36, 32
#gpio.setmode(gpio.BOARD)
gpio.setup(p1, gpio.OUT)
gpio.setup(p2, gpio.OUT)
gpio.setup(p3, gpio.OUT)

def main():
        gpio.output(p1,gpio.LOW)
        gpio.output(p2,gpio.LOW)
        gpio.output(p3,gpio.LOW)
        while True:
                pass
        #sudo python3 
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()

