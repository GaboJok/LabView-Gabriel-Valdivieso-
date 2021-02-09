# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:30:58 2021

@author: gabri
"""

while True:
    x=input("Enter a number to count to: ")
    if x=='q' or x=='quit':
        break
    
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break