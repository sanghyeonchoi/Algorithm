n = int(input())
a = [0] + list(map(int, input().split()))
d = [0]*(n+1)

for i in range(1, n+1):
    d[i] = 1000*10000
    for j in range(1, i+1):
        d[i] = min(d[i],d[i-j]+a[j])

print(d[n])