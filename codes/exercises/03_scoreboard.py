#!/usr/bin/python3

import RPi.GPIO as gpio
import time

interval = 0.5
number = 0

sclk = 20 #clock
dio = 21 #datain / ser
rclk = 26 #latch

digits = {
        "0" : 0x3f, 
        "1" : 0x06, 
        "2" : 0x5b, 
        "3" : 0x4f, 
        "4" : 0x66, 
        "5" : 0x6d, 
        "6" : 0x7d, 
        "7" : 0x07, 
        "8" : 0x7f, 
        "9" : 0x6f 
}

gpio.setmode(gpio.BCM)

gpio.setup(rclk, gpio.OUT)
gpio.setup(sclk, gpio.OUT)
gpio.setup(dio, gpio.OUT)

button1 = 27
button2 = 18
button3 = 17

gpio.setup(button1, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(button2, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(button3, gpio.IN, pull_up_down = gpio.PUD_UP)

def handler1(arg):
        global number
        if (number < 9):
                number += 1
		
def handler2(arg):
        global number
        if (number > 0):
                number -= 1
		
def handler3(arg):
		global number
		number = 0
		
def tick():
        gpio.output(sclk,gpio.HIGH)
        gpio.output(sclk,gpio.LOW)

def shift():
        gpio.output(rclk, gpio.HIGH)
        gpio.output(rclk, gpio.LOW)

def setBit(value):
        if (value) : 
                gpio.output(dio, gpio.HIGH)
        else:
                gpio.output(dio, gpio.LOW)
        tick()

def setByte(value):
        #setBit(1)      #h
        #setBit(1)      #g
        #setBit(1)      #f
        #setBit(1)      #e
        #setBit(1)      #d
        #setBit(1)      #c
        #setBit(1)      #b
        #setBit(1)      #a
        for index in range(8):
                temp = (value & 0x80) / 0x80
                setBit(temp)
                value = value << 1

    
        setBit(0)
        setBit(0)
        setBit(0)
        setBit(0)
        setBit(0)       #!digit1
        setBit(1)       #!digit2
        setBit(1)       #!digit3
        setBit(1)       #!digit4
        shift()

def setDigits(value):
        digit = value % 10
        digit1 = digits[str(int(digit))]
        setByte(digit1)
 
def main():
        global number
        gpio.add_event_detect(button1, gpio.RISING, handler1, 200)
        gpio.add_event_detect(button2, gpio.RISING, handler2, 200)
        gpio.add_event_detect(button3, gpio.RISING, handler3, 200)
        while True:
                setDigits(number)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
