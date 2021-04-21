S = input().upper()
S_list = list(set(S))

cnt = []

for i in S_list:
    count = S.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(S_list[(cnt.index(max(cnt)))])
