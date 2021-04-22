m = int(input())
n = int(input())

list = []
for i in range(m, n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
        list.append(i)
if len(list) != 0:
    print(sum(list))
    print(list[0])
else:
    print(-1)
