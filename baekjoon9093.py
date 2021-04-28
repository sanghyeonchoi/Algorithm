n = int(input())


for _ in range(n):
    x = list(map(list,input().split()))
    for i in x:
        print(''.join(i[::-1]), end=' ')
    

