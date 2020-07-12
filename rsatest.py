import math
import random


listss = []
listss.append("happy")
print(listss)

lists = ["13", "0", "14"]
print(lists)

c = (2398 ** 3251) % 89711

amari = []

while c != 0:
    amari.append(c % 26)
    c = c // 26

amari.reverse()
print(amari)