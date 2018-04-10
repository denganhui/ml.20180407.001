#!/usr/bin/env python3
import math
a = int(input("输入值a："))
b = int(input("输入值b："))
c = int(input("输入值c："))
d = b * b - 4 * a *c
if d < 0:
	print("Roots are imaginary");
else:
	root1 = (-b + math.sqrt(d)) / (2 * a)
	root2 = (-b - math.sqrt(d)) / (2 * a)
	print("Root1 = ", root1)
	print("Root2 = ", root2)
