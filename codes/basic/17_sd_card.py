#!/usr/bin/python3

import spidev
import time

i2c = smbus.SMBus(1)

def main():
        while True:
                time.sleep(1)

try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)

