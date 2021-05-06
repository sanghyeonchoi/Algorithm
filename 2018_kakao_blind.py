# def solution(dartResult):
#     score = []
#     n = ''
#     for i in dartResult:
#         if i.isnumeric():
#             n += i
#         elif i =="S":
#             score.append(int(n)**1)
#             n = ''
#         elif i == "D":
#             score.append(int(n)**2)
#             n = ''
#         elif i == "T":
#             score.append(int(n) **3)
#             n = ''
#         elif i == "*":
#             if len(score) >1:
#                 score[-2] *= 2
#             score[-1] *= 2
#         elif i == "#":
#             score[-1] *= -1
#     return sum(score)

import re

def solution(dartResult):
    bonus = {'S' :1 , 'D' : 2, 'T' : 3}
    option = {'' :1, '*' : 2, '#': -1}
    regex = re.compile('(\d+)([SDT])([*#]?)')
    dart = regex.findall(dartResult)
    for i in range(len(dartResult)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]]* option[dart[i][2]]
    answer = sum(dart)
    return answer