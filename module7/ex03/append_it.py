#!/usr/bin/env python3
import sys

if len(sys.argv) ==1:
	print("none")
	sys.exit()

i=1
while i< len(sys.argv):
	arg = sys.argv[i]
	if arg.find("ism", len(arg)-3)==-1:
		print(arg+"ism")
	i+=1
