a = int(input())
b = int(input())
def solution(x,n):
    answer = []
    temp =0
    for i in range(n):
        
        temp +=x
        answer.append(temp)
        
    return answer

print(solution(a,b))
