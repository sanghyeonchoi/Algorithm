import sys

input = sys.stdin.readline

n = int(input())


x = list(map(int, input().split()))
max_num = max(x)
min_num = min(x)

print(min_num, max_num)
