#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:47:43 2020

@author: y.kurodou
"""

a = int(input())
i = 2
while i < a:
    if a % i == 0:
        break
    i += 1
if i == a:
    print("素数")
else:
    print(i,"で割れます")