# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:23:28 2021

@author: gabri
"""

lista=[]
file=open('devices.txt')
for a in file:
    a=a.strip()
    lista.append(a)
    print(a)
file.close()

print(lista)