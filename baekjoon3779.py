def check(s):
    n = len(s)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if s[i][j] == s[i][j-1]:
                cnt +=1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
            cnt = 1

            for j in range(1, n):
                if s[j][i] == s[j-1][i]:
                    cnt += 1
                else:
                    cnt = 1
                if ans < cnt:
                    ans = cnt
    return ans


n = int(input())
s = [list(input()) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n :
            s[i][j],s[i][j+1] = s[i][j+1],s[i][j]
            temp = check(s)
            if ans< temp:
                ans = temp
            s[i][j],s[i][j+1] = s[i][j+1],s[i][j]
        if i+1<n:
            s[i][j],s[i+1][j] = s[i+1][j],s[i][j]
            temp = check(s)
            if ans < temp:
                ans = temp
            s[i][j],s[i+1][j] = s[i+1][j],s[i][j]

print(ans)