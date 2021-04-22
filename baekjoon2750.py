n = int(input())
lst = []
for _ in range(n):
    a = int(input())
    lst.append(a)
sort_list = sorted(lst)

for i in range(len(lst)):
    print(sort_list[i])
