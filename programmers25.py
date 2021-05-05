def solution(n):
    cnt = [True] * (n+1)
    c = 0
    for i in range(2, int(n**0.5)+1):
        if cnt[i] == True:
            for j in range(i+i, n+1, i):
                cnt[j] = False
    for i in range(2, n+1):
        if cnt[i]:
            c += 1
    return c
    

print(solution(int(input())))
