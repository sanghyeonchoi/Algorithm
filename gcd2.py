#유클리드 호제법
#시간복잡도(logN)
def gcd(a,b):
    while(b!=0):
        r = a%b
        a= b
        b = r
    return a

a,b = map(int, input().split())

print(gcd(a,b))