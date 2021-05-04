def gcd(n,m):
    answer = []
    while m !=0:
        r = n%m
        n = m
        m = r
    return n
def solution(a,b):
    return [gcd(a,b),a*b/gcd(a,b)]
