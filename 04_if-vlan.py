# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:08:49 2020

@author: CEC
"""

nativeVLAN = 1
dataVLAN = 100
if nativeVLAN >= dataVLAN:
    print("the native VLAN and the data VLAN are the same.")
else:
    print("this native VLAN and the data VLAN are different.")
    