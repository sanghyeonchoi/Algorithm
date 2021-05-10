import sys

n,m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

a = [0]*m

def go(index, start, n,m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return 

    for i in range(start, n):
        a[index] = num[i]
        go(index+1, i,n,m)

go(0,0,n,m)