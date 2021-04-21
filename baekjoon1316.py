n = int(input())

count = 0

for _ in range(n):
    S = input()
    error = 0
    for j in range(len(S)-1):
        if S[j] != S[j+1]:
            next = S[j+1:]
            if next.count(S[j]) > 0:
                error += 1
    if error == 0:
        count += 1

print(count)
