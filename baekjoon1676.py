def calc(n,v):
    result =0
    i = v
    while i <= n:
        result += n//i
        i *= v
    return result
n = int(input())
print(calc(n,5))