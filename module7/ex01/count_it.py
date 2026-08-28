#!/usr/bin/env python3
import sys

if len(sys.argv)==1:
	print("none")
	sys.exit()
sys.argv.pop(0)
print(f"parameters: {len(sys.argv)}")
for i in range(len(sys.argv)):
	print(f"{sys.argv[i]}: {len(sys.argv[i])}")

