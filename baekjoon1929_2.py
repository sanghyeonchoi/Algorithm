import sys
input = sys.stdin.readline
a, b = map(int, input().split())

max = 1000000
check = [0]*(max+1)
check[0] = check[1]= True


for i in range(2, max+1):
    if not check[i]:
        j = i+i
        while j <=max:
            check[j] = True
            j += i
for i in range(a, b+1):
    if check[i] == False:
        print(i)
    