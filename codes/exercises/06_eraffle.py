#!/usr/bin/python3

#import module random
import random, time

def main():
        participants = range(28)

        for count in range(10):
            print(random.choice(participants) + 1)
            time.sleep(1)
            
        print("The winner is number : ")
        print(random.choice(participants) + 1)
        
        
            
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)

