n = int(input())

stack =[]
result = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    
    while count <= num:
        stack.append(count)
        result.append('+')
        count+=1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        temp =False
if temp == False:
    print("NO")
else:
    for j in result:
        print(j)

