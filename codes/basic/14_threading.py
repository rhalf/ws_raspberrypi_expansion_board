#!/usr/bin/python3
import time, threading
def t1():
        for i in range(10): 
                print("t1 :" + str(i))
                time.sleep(0.1)
        print("t1 is terminated")
def t2():
        for i in range(10):
                print("t2 :" + str(i))
                time.sleep(0.2)
        print("t2 is terminated")
def main():
        threading.Thread(target=t1).start()
        threading.Thread(target=t2).start()
        while True: pass
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
        
