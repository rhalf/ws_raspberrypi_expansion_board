#!/usr/bin/python3
import RPi.GPIO as gpio, time
leds = [19, 16, 12]
# mode : gpio.BCM | gpio.BOARD 
gpio.setmode(gpio.BCM)
for led in leds:
        gpio.setup(led, gpio.OUT)
# gpio.PWM(pin, frequency)
pwm1 = gpio.PWM(leds[0], 100)
pwm1.start(0) #dutycycle
pwm2 = gpio.PWM(leds[1], 100)
pwm2.start(0) #dutycycle
pwm3 = gpio.PWM(leds[2], 100)
pwm3.start(0) #dutycycle

def main():
        while True:
                for value in range(100):
                        pwm1.ChangeDutyCycle(100 - value)
                        pwm2.ChangeDutyCycle(100 - value)
                        pwm3.ChangeDutyCycle(100 - value)
                        time.sleep(0.03)
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
