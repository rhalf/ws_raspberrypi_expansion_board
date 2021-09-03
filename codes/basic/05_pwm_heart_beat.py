#!/usr/bin/python3
import RPi.GPIO as gpio
import time
p1, p2, p3 = 19, 16, 12
gpio.setmode(gpio.BCM)
gpio.setup(p1, gpio.OUT)
gpio.setup(p2, gpio.OUT)
gpio.setup(p3, gpio.OUT)
# gpio.PWM(pin, frequency)
pwm1 = gpio.PWM(p1, 100)
pwm1.start(0)
pwm2 = gpio.PWM(p2, 100)
pwm2.start(0)
pwm3 = gpio.PWM(p3, 100)
pwm3.start(0)

def main():
        while True:
                for value in range(100):
                        pwm1.ChangeDutyCycle(value)
                        pwm2.ChangeDutyCycle(value)
                        pwm3.ChangeDutyCycle(value)
                        time.sleep(0.005)
                for value in range(100):
                        pwm1.ChangeDutyCycle(100 - value)
                        pwm2.ChangeDutyCycle(100 - value)
                        pwm3.ChangeDutyCycle(100 - value)
                        time.sleep(0.003)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        pwm1.stop()
        pwm2.stop()
        pwm3.stop()
        gpio.cleanup()
