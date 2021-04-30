n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    def gcd(a,b):
        while b !=0:
            r = a%b
            a = b
            b = r
        return a

    lcm = (a*b)/gcd(a,b)
    print(int(lcm))