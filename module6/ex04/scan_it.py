#!/usr/bin/env python3
import re
import sys

if len(sys.argv) !=3: 	
	print("none")
	sys.exit()

keyword=sys.argv[1]
target= sys.argv[2]
result = re.findall(keyword,target)

if not result:
	print("none")
else:
	print(len(result))
