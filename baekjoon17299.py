
n = int(input())
list_num = list(map(int, input().split()))
f = [0] *1000001
for num in list_num:
    f[num] += 1

stack = []

result = [-1 for _ in range(n)]

for i in range(len(list_num)):
    try:
        while f[list_num[stack[-1]]] < f[list_num[i]]:
            result[stack.pop()] = list_num[i]
    except:
        pass
    stack.append(i)

for i in range(n):
    print(result[i], end=" ")