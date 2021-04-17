import sys

input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
max_score = max(score)

list = []
for i in score:
    list.append(i/max_score*100)
avg = sum(list)/n

print("%.2f" % avg)
