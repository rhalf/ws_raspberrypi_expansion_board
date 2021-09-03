#!/usr/bin/python3
import RPi.GPIO as gpio
# blue, red, green
b1, b2, b3 = 27, 18, 17
# mode : gpio.BCM | gpio.BOARD 
gpio.setmode(gpio.BCM)
#gpio.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#gpio.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#gpio.setup(pin, direction, pull_up_down)
gpio.setup(b1, gpio.IN, gpio.PUD_UP)
gpio.setup(b2, gpio.IN, gpio.PUD_UP)
gpio.setup(b3, gpio.IN, gpio.PUD_UP)
def main():
        while True:
                if (gpio.input(b1) == gpio.LOW):
                        print("b1 is pressed.")
                elif (gpio.input(b2) == gpio.LOW):
                        print("b2 is pressed.")
                elif (gpio.input(b3) == gpio.LOW):
                        print("b3 is pressed.")
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
