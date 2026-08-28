#!/usr/bin/env python3
var = input("Enter a number less than 25: ")
num = int(var)
if num  > 25:
	print("Error")
else:
	while  num <= 25:
		print("Inside the loop. my variable is " +str(num))
		num+=1

