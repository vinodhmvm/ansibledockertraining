#!/usr/bin/python

def F1():
   print("F1() with zero arguments")

def F2(val1):
   print("F2() with one arguments" + str(val1))
   return val1

F1()
F2(val1=" passed variable")
print(val1)

