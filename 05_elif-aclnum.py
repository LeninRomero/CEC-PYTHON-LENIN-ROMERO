# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:28:07 2020

@author: CEC
"""

aclNum=int(input("What is the IPV4 ACL number?"))
if aclNum >= 1 and aclNum <=99:
    print("This is a standard IPV4 ACL.")
elif aclNum >=100 and aclNum <=199:
    print ("This is a extended IPV4 ACL.")
else:
    print("This is not a standard or exten IPV4 ACL.")
    