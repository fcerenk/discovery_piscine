#!/usr/bin/env python3
numbers=[2,8,9,48,8,22,-12,2]
print(f" {numbers}")
numbers = [x+ 2 for x in numbers if (x+2) >5]

print(f"{numbers}")
