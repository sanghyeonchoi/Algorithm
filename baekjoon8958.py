import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = input()
    str = list(a)
    sum = 0
    count = 1
    for i in str:
        if i == "O":
            sum += count
            count += 1
        else:
            count = 1

    print(sum)
