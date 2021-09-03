import RPi.GPIO as gpio
#!/usr/bin/python3
import serial, time
# raspberry 2 - /dev/ttyAMA0 - gpio serial
# raspberry 3 - /dev/ttyAMA0 - bluetooth - 
#               /dev/serial0 - gpio serial
# add enable_uart=1 to boot.config
# remove console=serial0,115200 in commandline.text
enable = 4
gpio.setmode(gpio.BCM)
gpio.setup(enable, gpio.OUT)
gpio.output(enable, gpio.LOW)

port = serial.Serial(
        '/dev/serial0',
        timeout=None,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
)

def main():
        message = "hi!"
        port.write(message.encode())
        message = ""
        print(port.readline())
        while True:
                pass    
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        gpio.cleanup()