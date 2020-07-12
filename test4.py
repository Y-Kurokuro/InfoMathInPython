print("mod =",end="")
n = int(input())
print("a=",end="")
a = int(input())

m = a % n

i = -1

while -i < n:
    if i % n == m:
        break
    i -= 1

print(a,"と合同な一番大きな負の数は",i)