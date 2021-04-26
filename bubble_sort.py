# random_number =[4,35,7,5,9,1,2,24,78] 

def bubble(lst):
    for a in range(0, len(lst)-1):
        for b in range(a+1,len(lst)):
            if lst[a]> lst[b]:
                temp = lst[a]
                lst[a]= lst[b]
                lst[b] = temp
    return lst


result = bubble(list(map(int, input().split())))
print(result)