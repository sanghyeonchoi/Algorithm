def solution(n):
    s = str(n)
    answer = sorted(s, reverse=True)
    answer = int(''.join(answer))
    return answer

print(solution(int(input())))
