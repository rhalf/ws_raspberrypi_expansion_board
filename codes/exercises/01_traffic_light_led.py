#!/usr/bin/python3
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

led1 = 19
led2 = 16
led3 = 12

button1 = 27
button2 = 18
button3 = 17


flag = False

gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)
gpio.setup(led3, gpio.OUT)

gpio.output(led1, gpio.HIGH)
gpio.output(led2, gpio.HIGH)
gpio.output(led3, gpio.HIGH)

gpio.setup(button1, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(button2, gpio.IN, pull_up_down = gpio.PUD_UP)

def onStart(arg):
         global flag
         flag = True

def onStop(arg):
         global flag
         flag = False

def run():
    global flag 
    for index in range(10): # Green
        gpio.output(led1, gpio.LOW)
        gpio.output(led2, gpio.HIGH)
        gpio.output(led3, gpio.HIGH)
        time.sleep(1)
        if (flag == False):
            return
    for index in range(3): # Orange
        gpio.output(led1, gpio.HIGH)
        gpio.output(led2, gpio.LOW)
        gpio.output(led3, gpio.HIGH)
        time.sleep(1)
        if (flag == False):
            return
    for index in range(7): # Red
        gpio.output(led1, gpio.HIGH)
        gpio.output(led2, gpio.HIGH)
        gpio.output(led3, gpio.LOW)
        time.sleep(1)
        if (flag == False):
                return

def main():
        gpio.add_event_detect(button1, gpio.RISING, callback = onStart, bouncetime=200)
        gpio.add_event_detect(button2, gpio.RISING, callback = onStop, bouncetime=200)

        while True:
                if flag == True:
                        run()
                  
              
try:
        main()
except KeyboardInterrupt:
       pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
