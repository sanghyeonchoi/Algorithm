import sys
n,m = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
check = [False]*(n+1)
a = [0]*m

def go(index, n,m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        a[index] = num[i]
        go(index+1,n,m)
        check[i] = False
go(0,n,m)