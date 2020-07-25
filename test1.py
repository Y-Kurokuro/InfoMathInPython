import numpy as np

print("mod:",end="")
m = int(input())

a = np.zeros((2,2))
print("左辺の行列を入力してください")
for i in range(2):
    for j in range(2):
        a[i][j] = int(input())

b = np.zeros((2,1))
print("右辺の行列を入力してください")
for i in range(2):
    for j in range(1):
        b[i][j] = int(input())

det = (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % m   #行列式を計算

c = 1
while c < m:    #ac≡1(mod m)となるcを見つける
    if (c * det) % m == 1:
        break
    c += 1

d = np.zeros((2,2))
d[0][0] = a[1][1]
d[0][1] = -a[0][1]
d[1][0] = -a[1][0]
d[1][1] = a[0][0]

inv = np.zeros((2,2))   #逆行列invを計算
for i in range(2):
    for j in range(2):
        inv[i][j] = (d[i][j] * c) % m


xy = np.zeros((2,1))    #答えを計算
xy[0][0] = (inv[0][0] * b[0][0] + inv[0][1] * b[1][0]) % m
xy[1][0] = (inv[1][0] * b[0][0] + inv[1][1] * b[1][0]) % m

print("x,y=" ,xy)

print("検算", a, "*", xy, "=", (a[0][0] * xy[0][0] + a[0][1] * xy[1][0]) % m, (a[1][0] * xy[0][0] + a[1][1] * xy[1][0]) % m)
