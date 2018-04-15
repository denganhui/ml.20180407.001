#!/usr/bin/env python3
import math as m 
a, b = 0, 1
while b < 100000000:
	print(b, end= ' ')
	print("黄金值：{:.10f}".format(a/b))
	a, b = b, a + b
print()

