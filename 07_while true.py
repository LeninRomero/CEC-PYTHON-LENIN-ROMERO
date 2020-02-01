# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:10:42 2020

@author: CEC
"""

while True:
    x=input("Enter a numbre to count to:")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break