# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:16:29 2020

@author: CEC
"""

def address (street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)
    
s=input("Street:")
pC=input("Postal Code:")
c=input("City:")

address (s, c, pC)