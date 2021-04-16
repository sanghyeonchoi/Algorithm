import sys

input = sys.stdin.readline

num = out = int(input())


count = 0

while True:
    ten = num//10
    one = num % 10
    total = ten + one
    count += 1
    num = int(str(num % 10)+str(total % 10))
    if(out == num):
        break
print(count)
