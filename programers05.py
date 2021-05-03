def solution(x):
    s = str(x)
    add = 0
    for i in range(len(s)):
        add += int(s[i])
    return x % add == 0
    
a= int(input())
print(solution(a))