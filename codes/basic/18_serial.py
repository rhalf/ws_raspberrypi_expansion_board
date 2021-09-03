#!/usr/bin/python3
import serial, time
# raspberry 2 - /dev/ttyAMA0 - gpio serial
# raspberry 3 - /dev/ttyAMA0 - bluetooth - 
#               /dev/serial0 - gpio serial

# add enable_uart=1 to boot.config
# remove console=serial0,115200 in commandline.text
port = serial.Serial(
        '/dev/serial0',
        timeout = None,
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS
)

def main():
        message = "hi\n"
        port.write(message.encode())
        time.sleep(1)
        while True:
            pass
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)