test_case = int(input())
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

for _ in range(test_case):
    a = list(map(int, input().split()))
    n = a[0]
    a = a[1:]
    ans = 0
    for i in range(0, n-1):
        for j in range(i+1,n):
            ans += gcd(a[i],a[j])
    print(ans)



