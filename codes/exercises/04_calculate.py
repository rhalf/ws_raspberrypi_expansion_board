#!/usr/bin/python3

# import module sys
import sys

def main():
	result = calculate(
		sys.argv[1], 
		sys.argv[2], 
		sys.argv[3])
	print(result)
		
def calculate(o, s1, s2):
	if (not s1.isdigit()):
		raise Exception("Invalid number1")
		
	elif(not s2.isdigit()):
		raise Exception("Invalid number2")
		
	x, y = float(s1), float(s2)
	
	if (o == "add"):
		return x + y
	elif (o == "sub"):
		return x - y
	elif (o == "mul"):
		return x * y
	elif (o == "div")
		return x / y
	else:
		raise Exception("Unknown operator")
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
