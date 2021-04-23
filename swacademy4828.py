T = int(input())


for i in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    print("#{0} {1}".format(i+1, max(lst)-min(lst)))
