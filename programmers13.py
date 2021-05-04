def solution(n):
    answer= []
    s = reversed(str(n))

    for i in s:
        answer.append(int(i))
    return answer
print(solution(int(input())))

def solution2(n):
    return list(map(int, reversed(str(n))))

def solution3(n):
    return [int(n) for i in str(n)][::-1]