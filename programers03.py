
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr[i])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    
    return answer

def solutrion(x,y):
    answer = [[c+d for c,d in zip(a,b)] for a,b in zip(x,y)]
    return answer