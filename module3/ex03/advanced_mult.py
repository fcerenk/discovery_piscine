#!/usr/bin/env python3

for x in range(11):
	print("Table of " + str(x) + ": ", end="")
	y=0
	while(y<=10):
		result = x*y
		print(str(result)+ " ",  end ="")
		y+=1
	print()
