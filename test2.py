#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:08:15 2020

@author: y.kurodou
"""

print("mod =",end="")
n = int(input())
print("a=",end="")
a = int(input())
x = 1
while x < n:
    if(a*x) % n == 1:
        break
    x += 1

print(x,"がaの逆数です")