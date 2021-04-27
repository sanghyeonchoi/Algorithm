n = int(input())

array = []

for _ in range(n):
    x = list(map(int, input().split()))
    array.append(x)

array = sorted(array)

for i in array:
    print(i[0],i[1])