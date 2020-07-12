import math
import random

def prime(n):#素数判定
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if math.sqrt(n) < i:
            return True
        if n % i == 0:
            return False

p, q = 0, 0
while (p==q) or not prime(p) or not prime(q):#p == q または　p が素数でない　または　q が素数でない間続ける (p != q かつ p 素数 q 素数 ならば抜ける)
    p = random.randint(10**5, 10**6)
    q = random.randint(10**5, 10**6)

print('p:' + str(p))
print('q:' + str(q))