#!/usr/bin/env python3
amount=float(input("输入金额："))
inrate=float(input("输入利率："))
period=float(input("输入期限: "))
value = 0
year = 1
while year <= period:
	value=amount + (inrate * amount)
	print("第{}年储蓄金额{:.2f}".format(year, value))
	amount = value
	year = year +1

	
