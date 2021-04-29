import sys
while True:
    lines = sys.stdin.readline()
    lower = 0
    upper = 0
    number = 0
    space = 0
    if not lines:
        break
    for s in lines:
        for ch in s:
            x = ord(ch)
            if ord('a') <= x <= ord('z'):
                lower += 1
            elif ord('A') <= x <= ord('Z'):
                upper += 1
            elif ord('0') <= x <= ord('9'):
                number += 1
            elif ch == ' ':
                space += 1
    print('%d %d %d %d' % (lower, upper, number, space))

# 다른 코드
import sys

while True:
    line = sys.stdin.readline().rstrip("\n")
    lo,up,nu,sp = 0,0,0,0

    if not line:
        break
    for i in line:
        if i.isupper():
            up +=1
        elif i.islower():
            lo +=1
        elif i.isdigit():
            nu +=1
        elif i.isspace():
            sp +=1
    sys.stdout.write("{} {} {} {}\n".format(lo, up , nu, sp))
    