import random
import math

def prime(n):   #素数判定関数をつくる
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    i = 3
    while i < r:
        if n % i == 0:
            break
        i += 2
    if i > r:
        return True
    else:
        return False

p, q = 0, 0
while (p == q) or not prime(p) or not prime(q):   #p == q または　p が素数でない　または　q が素数でない間続ける (p != q かつ p 素数 q 素数 ならば抜ける)
    p = random.randint(10**10, 10**11)
    q = random.randint(10**10, 10**11)
#p,qは互いに素な素数なので、最大公約数は1

n = p * q

print(p)    #受信側はこれを記憶しておく
print(q)

print(n)    #これを送信者側に渡す
