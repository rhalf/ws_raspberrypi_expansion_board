#!/usr/bin/python3
import time

def callback1():
    print("hi im callback function")

def main():
        callback = callback1
        callback()
        while True:
               pass
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)

