#!/usr/bin/python3
import RPi.GPIO as gpio, time
buttons = [27, 18, 17]
# mode : gpio.BCM | gpio.BOARD 
gpio.setmode(gpio.BCM)
#gpio.setup(pin, direction, pull_up_down)
for b in buttons:
        gpio.setup(b, gpio.IN, gpio.PUD_UP)
def main():
        while True:
                for i, b in enumerate(buttons):
                        if (gpio.input(b) == gpio.LOW):
                                print("b " + str(i) +" is pressed.")        
                                while(gpio.input(b) == gpio.LOW):
                                        time.sleep(0.1)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
