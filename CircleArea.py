#!/usr/bin/env python3
import math as m 
area= 0
print("计算 圆的面积")
PI=m.pi
print("PI:{:.8f}".format(PI))

r = int(input("请输入半径R:"))
area = PI * r * r

print("半径{:2d}的圆面积为{:6.8f}".format(r, area)); 

