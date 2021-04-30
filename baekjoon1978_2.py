import sys

input = sys.stdin.readline

n = int(input())


def prime(num):
    if num <2:
        return False
    i =2
    while i*i <= num:
        if num % i ==0:
            return False
        i += 1
    return True

count = 0
number = map(int, input().split())
for i in number:
    if prime(i):
        count +=1
print(count)