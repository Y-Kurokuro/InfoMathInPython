import random

def prime(n):   #素数判定関数をつくる
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1
    if i == n:
        return True
    else:
        return False

p, q = 0, 0
while (p == q) or not prime(p) or not prime(q):   #p == q または　p が素数でない　または　q が素数でない間続ける (p != q かつ p 素数 q 素数 ならば抜ける)
    p = random.randint(10**5, 10**6)
    q = random.randint(10**5, 10**6)
#p,qは互いに素な素数なので、最大公約数は1

n = p * q
print(n)    #これを送信者側に渡す
