#!/usr/bin/python3
import RPi.GPIO as gpio
import time

buzzer, duration = 13, 0.8

gpio.setmode(gpio.BCM)
gpio.setup(buzzer, gpio.OUT)
# equivalent frequency dictionary
frequencies = { 
        "C" : 261, "D" : 294, "E" : 329, 
        "F" : 349, "G" : 392, "A" : 440, "B" : 493, 
        "c" : 523, "d" : 587, "e" : 659, 
        "f" : 699, "g" : 784, "a" : 880, "b" : 989
}
chords = "GGAGcB GGAGdc GGgecBA ffecdc"
beats = [ 
        4, 4, 2, 2, 2, 1, 16,   
        4, 4, 2, 2, 2, 1, 16,   
        4, 4, 2, 2, 2, 2, 1,   
        16, 4, 4, 2, 2, 2, 1]

def tone(pin, frequency, duration):
        pwm = gpio.PWM(pin, frequency)
        pwm.start(50)
        time.sleep(duration)
        pwm.stop()

def playChords(chord, duration):
        if (chord == " "): time.sleep(duration)
        else:
                tone(buzzer, frequencies[chord], duration)
                time.sleep(duration)
        print("chord", chord)
        
def main():
        while True:
                for index in range(0, len(chords)):
                        playChords(chords[index], 
                        duration / beats[index])

try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()
