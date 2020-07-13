#平文は27文字のいずれかの組み合わせとする
chara = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


print("plane:",end="")  #平文を入力
pl = list(input())

plnum = []
for i in range(len(pl)):    #平文を数字にする
    for j in range(27):
        if pl[i] == chara[j]:
            plnum.append(j)
            break

p = 0
for i in range(len(plnum)):     #数字を1つの10進数にする
    p += plnum[i] * 27 ** (len(plnum) - 1 - i)

print("n:",end="")
n = int(input())    #受信者側から受け取ったnを入力
e = 65537   #Wikipedia「RSA暗号」より

#暗号化
c = pow(p, e, n)

rad = []    #暗号化したものを27進数にする
while c != 0:
    rad.append(c % 27)
    c = c // 27
rad.reverse()

cchar = []
for i in range(len(rad)):    #暗号文に直す
    for j in range(27):
        if rad[i] == j:
            cchar.append(chara[j])
            break

print(cchar)