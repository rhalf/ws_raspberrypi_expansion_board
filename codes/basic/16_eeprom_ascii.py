#!/usr/bin/python3-
import smbus, time
eeprom = 0x50
i2c = smbus.SMBus(1)

dO = "rhalf wendel caacbay"
dI = ""

def main():
        global dO, dI
        #loop that writes the data
        for index, char in enumerate(dO):
                i2c.write_byte_data(
                        eeprom, index, ord(char))
                time.sleep(0.01)
        #loop that reads the data
        for index in range(len(dO)):
                char = chr(i2c.read_byte_data(
                        eeprom, index))
                dI += char
        print(dI)

        while True:
                pass

try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)



