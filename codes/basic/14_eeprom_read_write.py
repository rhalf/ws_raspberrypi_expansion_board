#!/usr/bin/python3
import smbus, time
#eepromWrite=0xa0,eepromRead=0xa1
#eeprom address

eeprom = 0x50
i2c = smbus.SMBus(1)

def main():
        #writing data on eeprom
        for index in range(16):
                i2c.write_byte_data(eeprom, index, 143)
                time.sleep(0.1)
        #reading from eeprom
        for index in range(16):
                data = i2c.read_byte_data(eeprom, index)
                print(data)
        while True:
                pass
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)



