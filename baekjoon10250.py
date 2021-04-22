n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split())
    floor = 0
    num = 0
    if n % h == 0:
        floor = h*100
        num = n//h
    else:
        floor = (n % h)*100
        num = 1+n//h
    print(floor+num)
