#!/usr/bin/python3
import RPi.GPIO as gpio,time
delay = 0.5
#clock, data, latch
clk, io, lat = 20, 21, 26
nos = {
        "0" : 0x3f, "1" : 0x06, "2" : 0x5b, "3" : 0x4f, "4" : 0x66, 
        "5" : 0x6d, "6" : 0x7d, "7" : 0x07, "8" : 0x7f, "9" : 0x6f 
}
gpio.setmode(gpio.BCM)
gpio.setup(lat, gpio.OUT)
gpio.setup(clk, gpio.OUT)
gpio.setup(io, gpio.OUT)

def tick():
        gpio.output(clk,gpio.HIGH)
        gpio.output(clk,gpio.LOW)
def save():
        gpio.output(lat, gpio.HIGH)
        gpio.output(lat, gpio.LOW)
def setBit(value):
        if (value == 1) : gpio.output(io, gpio.HIGH)
        else : gpio.output(io, gpio.LOW)
        tick()
def setBytes(a):
        #hgfedcba -> profile numbers
        #00000000 -> HIGH Nibble -> unused
        #         -> LOW Nibble -> digits
        #a = 00111111 & 10000000 / 10000000
        #a = 01111110
        for index in range(8):
                bit1 = (a & 0x80) / 0x80
                setBit(bit1)
                a = a << 1
        setBit(0)       # na
        setBit(0)       # na
        setBit(0)       # na
        setBit(0)       # na
        setBit(0)       #!digit1
        setBit(0)       #!digit2
        setBit(0)       #!digit3
        setBit(0)       #!digit4
        save()

def setDigits(value):
        digit = value % 10
        digit1 = nos[str(int(digit))]
        setBytes(digit1)

def main():
        while True:
                for value in range(10):
                        setDigits(value)
                        time.sleep(delay)          
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
