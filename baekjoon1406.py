import sys

input = sys.stdin.readline

left_stack = list(input().rstrip())
right_stack = []
m = int(input())
for i in range(m):
    s = input().rstrip().split()
    order = s[0]
    if order == "L":
        if len(left_stack)==0:
            continue
        right_stack.append(left_stack.pop())
    elif order == "D":
        if len(right_stack) == 0:
            continue
        left_stack.append(right_stack.pop())
    elif order == "B":
        if len(left_stack) == 0:
            continue
        left_stack.pop()
    elif order == "P":
        left_stack.append(s[1])

left_stack.extend(right_stack[::-1])

print("".join(left_stack))