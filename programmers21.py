def solution(s):
    count = 0
    for i in s:
        if i == "P" or i == "p":
            count +=1
        if i == "Y" or i == "y":
            count -=1
    if count == 0:
        return True
    else:
        return False