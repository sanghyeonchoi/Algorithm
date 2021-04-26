list = [9,22,3,6,7,4,5]

def solution(list):
    result = list[0]
    for num in list[1:]:
        if result<num:
            result = num
        print(num , result)
        
    
    return result 

def solution2(list):
    result = list[0]
    for num in range(1, len(list)):
        if result < list[num]:
            result = list[num]
    return result

# min 은 부호만 바꾸면 됨

print('=>',solution(list))
print('=>',solution2(list))