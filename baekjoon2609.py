a,b = map(int, input().split())

def gcd(n,m):
    while m != 0:
        r = n%m
        n = m
        m = r
    return n
lcm = (a*b)/gcd(a,b)

print(gcd(a,b))
print(int(lcm))
