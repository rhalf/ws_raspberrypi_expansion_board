#!/usr/bin/python3

import RPi.GPIO as gpio
import time

buzzer = 13

button1 = 27
button2 = 18
button3 = 17

gpio.setmode(gpio.BCM)
gpio.setup(button1, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(button2, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(button3, gpio.IN, pull_up_down = gpio.PUD_UP)

gpio.setup(buzzer, gpio.OUT)

def handler1(arg):
        tone(buzzer, 440, 0.25)
		
def handler2(arg):
        tone(buzzer, 880, 0.25)
		
def handler3(arg):
        tone(buzzer, 1320, 0.25)
		
def tone(pin, frequency, duration):
        pwm = gpio.PWM(pin, frequency)
        pwm.start(50)
        time.sleep(duration)
        pwm.stop()

		
def main():
        gpio.add_event_detect(button1, gpio.RISING, handler1 , 200)
        gpio.add_event_detect(button2, gpio.RISING, handler2 , 200)
        gpio.add_event_detect(button3, gpio.RISING, handler3 , 200)
        while True:
              time.sleep(0.1)
try:
        main()
except KeyboardInterrupt:
       pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
