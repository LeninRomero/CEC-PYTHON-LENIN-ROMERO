# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:23:28 2020

@author: CEC
"""

firstname=input ("what is your first name?")
lastname=input ("what is your last name?")
print("hello "+ firstname,lastname + "!")
age=int(input("What is your age?"))
if age >= 1 and age <=15:
    print("niño")
elif age >=16 and age  <=30:
    print ("joven")
else:
    print("adulto")