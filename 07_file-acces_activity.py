# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:18:15 2020

@author: CEC
"""

file = open ("devices.txt","a")
while True:
    newItem = input ("Enter device name: ")
    if newItem == "exit":
        print ("All done!")
        break
    file.write(newItem + "\n")
file.close()

