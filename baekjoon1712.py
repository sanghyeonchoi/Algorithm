A, B, C = map(int, input().split())
bp = 0

if C <= B:
    bp = -1
else:
    bp = A//(C-B)+1
print(bp)
