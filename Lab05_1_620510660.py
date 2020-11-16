#!/usr/bin/env python3
# รัฏชพล ปุกคำ
# 620510660
# Lab 06
# Problem 1
# 204113 Sec 002
import time
import datetime
from pylab import *
def main():
    n = int(input())
    rand_float(n)
def rand_float(n):
    x = (int)(time.time()) 
    l = []
    for i in range(n):
        y = datetime.datetime.now()
        a = (int)(y.microsecond) 
        m = (int)(y.minute*y.second)
        c = (int)(y.minute*y.second)
        xn = (a*x+c) % m
        xn = xn/m
        l.append(xn) 
        x = xn #เปลี่ยนseedไปเรื่อยๆ
    plot(l,'ro')
    show()
    print("สวัสดีตอนง่วง")
    
if __name__ == '__main__' :
    main()
    
