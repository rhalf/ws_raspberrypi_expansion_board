#!/usr/bin/python3
import RPi.GPIO as gpio, time, threading
no = 0
isEn = True
cDelay = 0.001
dDelay = 0.000001
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
def setBit(bit):
        if (bit == 1) : gpio.output(io, gpio.HIGH)
        else : gpio.output(io, gpio.LOW)
        tick()

def setBytes(a, b):
        for index in range(8):
                bit = (a & 0x80) / 0x80
                setBit(bit)
                a = a << 1
        for index in range(8):
                bit = (b & 0x80) / 0x80
                setBit(not bit)
                b = b << 1
        save()
def setDigits(value):
        d = value % 10          #1434
        digit1 = nos[str(d)]    #4

        value = value // 10     #143
        d = value % 10          #3
        digit2 = nos[str(d)]

        value = value // 10     #14
        d = value % 10          #4
        digit3 = nos[str(d)]

        value = value // 10     #1
        d = value % 10          #1
        digit4 = nos[str(d)]

        setBytes(digit1, 0x08) #digit1
        time.sleep(dDelay)
        setBytes(digit2, 0x04) #digit2
        time.sleep(dDelay)  
        setBytes(digit3, 0x02) #digit3
        time.sleep(dDelay) 
        setBytes(digit4, 0x01) #digit4
        time.sleep(dDelay) 
        
def display():
        global no, isEn
        try:
                while isEn:
                        setDigits(no)
        except Exception as exception:
                print(exception)
        finally:
                print("display thread is closed")
                        
def main():
        global no
        threading.Thread(target=display).start()
        while True:
                for count in range(10000):
                        no = count
                        time.sleep(cDelay)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        isEn = False
        time.sleep(1)
        gpio.cleanup()
