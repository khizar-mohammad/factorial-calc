#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fact(x):
  y = 1
  for i in range(x,1,-1):
    y = y * i
  return y

print("Please enter the number for which the factorial will be calculated: ")
factNumber = int(input())
print("the factorial of ",factNumber, " is ", fact(factNumber))

