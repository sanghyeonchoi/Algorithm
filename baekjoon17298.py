# n = int(input())
# list_num = list(map(int, input().split()))
# stack = []
# result = [-1 for _ in range(n)]

# for i in range(len(list_num)):
#     try:
#         while list_num[stack[-1]] < list_num[i]:
#             result[stack.pop()] = list_num[i]
#     except:
#         pass
#     stack.append(i)
# for i in range(n):
#     print(result[i], end=" ")























n = int(input())
list_num = list(map(int, input().split()))
stack = []

result = [-1 for _ in range(n)]

for i in range(len(list_num)):
    try:
        while list_num[stack[-1]] < list_num[i]:
            result[stack.pop()] = list_num[i]
    except:
        pass
    stack.append(i)

for i in range(n):
    print(result[i], end=" ")