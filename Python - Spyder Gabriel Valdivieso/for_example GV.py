# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:38:34 2021

@author: gabri
"""

lista1=['R1','R2','R3',"S1","S2","S3"]
switches=[]
routers=[]

for i in lista1:
    if "R" in i:
        routers.append(i)
    if "S" in i:
        switches.append(i)

for i in routers:
    print(i)
    
print("\n")
    
for i in switches:
    print(i)


