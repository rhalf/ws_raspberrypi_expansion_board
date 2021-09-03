#!/usr/bin/python3
import RPi.GPIO as gpio, time
import 11_buzzer_frequencies as frequencies
pin, dura = 13, 1.5
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

chords = [ 
        "A6", "FS6", "G6", "A6", "FS6", "G6", "A6", "A5", 
        "B5", "CS6", "D6", "E6", "FS6", "G6", "FS6", "D6",
        "E6", "FS6", "FS5", "G5", "A5", "B5", "A5", "G5", 
        "A5", "FS5", "G5", "A5", "G5", "B5", "A5", "G5", 

        "FS5", "E5", "FS5", "E5", "D5", "E5", "FS5", "G5", 
        "A5", "B5", "G5", "B5", "A5", "B5", "CS6", "D6", 
        "A5", "B5", "CS6", "D6", "E6", "FS6", "G6", "A6"
        ]

beats = [
        8, 16, 16, 8, 16, 16, 16, 16,
        16, 16, 16, 16, 16, 16, 8, 16,
        16, 8, 16, 16, 16, 16, 16, 16,
        16, 16, 16, 16, 8, 16, 16, 8,

        16, 16, 16, 16, 16, 16, 16, 16,
        16, 16, 8, 16, 16, 8, 16, 16,
        16, 16, 16, 16, 16, 16, 16, 16
        ]

def tone(pin, freq, dura):
        pwm = gpio.PWM(pin, freq)
        pwm.start(50)
        time.sleep(dura)
        pwm.stop()

def playChord(chord, dura):
        tone(pin, frequencies.frequencies[chord], dura)
        time.sleep(dura * 1.3)
        print("chord", chord)

def main():
        while True:
                for i, chord in enumerate(chords):
                        playChord(chord, dura / beats[i])

try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()

