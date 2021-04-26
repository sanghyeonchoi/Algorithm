n,m = map(int,input().split())
card_num = list(map(int, input().split()))
card_len= len(card_num)
sum = 0

for i in range(0,card_len-2):
    for j in range(i+1,card_len-1):
        for k in range(j+1,card_len):
            if card_num[i]+card_num[j]+card_num[k]>m:
                continue
            else:
                sum = max(sum,card_num[i]+card_num[j]+card_num[k])
print(sum)

