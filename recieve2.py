import math

chara = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print("crypt:",end="")  #暗号文を入力
cr = list(input())

crnum = []
for i in range(len(cr)):    #暗号文を数字にする
    for j in range(27):
        if cr[i] == chara[j]:
            crnum.append(j)
            break


c = 0
for i in range(len(crnum)):     #数字を1つの10進数にする
    c += crnum[i] * 27 ** (len(crnum) - 1 - i)



print("p:",end="")  #記憶しておいたp,qを入力
p = int(input())

print("q:",end="")
q = int(input())

L = ((p-1) * (q-1)) / math.gcd(p-1,q-1) #L*gcd = 元の数の積になるので、ここから最小公倍数を求める

e = 65537   #Wikipedia「RSA暗号」より
d = 1
while d < L:    #複合化鍵を求める
    if (d * e) % L == 1:
        break
    d += 1



n = p * q
pl = (c ** d) % n   #平文を数字で複合化する
print(pl)

rad = []    #複号化したものを27進数にする
while pl != 0:
    rad.append(pl % 27)
    pl = pl // 27
rad.reverse()

print(rad)

pchar = []
for i in range(len(rad)):    #平文に直す
    for j in range(27):
        if rad[i] == j:
            pchar.append(chara[j])
            break

print(pchar)