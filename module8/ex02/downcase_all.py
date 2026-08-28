#!/usr/bin/env python3
import sys

def downcase_it(word):
	text= word.lower()
	return text

if len(sys.argv) ==1:
	print("none")

sys.argv.pop(0)
for i in range(len(sys.argv)):

	result = downcase_it(sys.argv[i])
	print(result)
