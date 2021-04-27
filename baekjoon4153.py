
while True:
    x = list(map(int, input().split()))
    max_num =max(x)
    if sum(x) ==0:
        break
    x.remove(max_num)
    if x[0]**2 + x[1]**2 == max_num**2:
        print("right")
    else:
        print("wrong")