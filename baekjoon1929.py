
import math

a, b = map(int, input().split())
end = b+1


def prime(num):
    if num == 1:
        return False

    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0:
            return False
    return True


for i in range(a, end):
    if prime(i):
        print(i)
