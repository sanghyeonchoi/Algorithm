import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

res = a*b*c
resList = list(str(res))
for i in range(10):
    resNumCount = resList.count(str(i))
    print(resNumCount)
