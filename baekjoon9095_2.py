def go(s , goal):
    if s >goal:
        return 0
    if s == goal:
        return 1 
    ans = 0 
    for i in range(1,n+1):
        ans += go(s+i, goal)
    return ans 

n = int(input())
for _ in range(n):
    num = int(input())
    print(go(0,num))