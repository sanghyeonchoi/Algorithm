def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[i+1]

import collections

def solution(participant,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]