#!/usr/bin/python3
import RPi.GPIO as gpio, time
pin, dura, freq = 13, 2, 500
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

def tone(pin, freq, dura):
        pwm = gpio.PWM(pin, freq)
        pwm.start(50)
        time.sleep(dura)
        pwm.stop()
def main():
        while True:
                tone(pin, freq, dura)
                time.sleep(2)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
