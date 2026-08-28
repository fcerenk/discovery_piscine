#!/usr/bin/env python3
var =int( input("Enter first number: "))
var1 = int(input("Enter second number: "))
result = var * var1
print(f"{var} x {var1} = {result}")
if (var * var1) > 0:
	print("The result is positive")
elif (var*var1) <0:
	print("The result is negative")
else:
	print("The result is positive and negative")
