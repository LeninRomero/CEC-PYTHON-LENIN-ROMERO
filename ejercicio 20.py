# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:51:46 2020

@author: CEC
"""

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee.doc:", Employee.__doc__)
print ("Employee.name:", Employee.__name__)
print ("Employee.module:", Employee.__module__)
print ("Employee.bases:", Employee.__bases__)
print ("Employee.dict:", Employee.__dict__)