#!/usr/bin/env python3
import sys


def shrink(word):
        print(word[0:8])

def enlarge(word):
        while len(word) <8:
                word+="Z"
        print(word)

if len(sys.argv)==1:
	print("none")

for arg in sys.argv[1:]:
	if len(arg) > 8:
		shrink(arg)
	elif len(arg) < 8:
		enlarge(arg)
	elif len(arg)==8:
		print(arg)
	


	
