#!/usr/bin/env python3
i = 1	
print("-" * 150)
while i < 15:
	n = 1
	while n <= 14:
		print("{:10d}".format(i * n), end = ' ')
		n += 1
	print()
	i += 1
print("-" * 150)
