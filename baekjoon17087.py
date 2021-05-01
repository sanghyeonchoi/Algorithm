n,s = map(int,input().split())
#n은 동생의 수 , s 는 수빈이의 현재 점

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

a = list(map(int,input().split()))
a = [abs(x-s) for x in a]
ans = a[0]

for i in range(1, n):
    ans = gcd(ans,a[i])
print(ans)
