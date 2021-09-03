#!/usr/bin/python3

def main():
        number = 0
        while(True):
                number += 1
                print("Enter your name :")
                name = input()
                write(number, name)
   
def write(number, a):
	# Open a file
        file = open("log.txt", "a")
        file.write(
                str(number) + "," +
                a + "\n")
	# Close opend file
        file.close()
   
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)


