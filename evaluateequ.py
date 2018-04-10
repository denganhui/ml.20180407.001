#!/usr/bin/env python3
sum = 0
print("计算 1/x + 1/(x+1) + 1/(x+2 + ... + 1/n)")
n = int(input("请输入N值:"))
for i in range(1, n):
	sum += 1.0 / i
	print("{:2d} {:6.4f}".format(i, sum)); 

