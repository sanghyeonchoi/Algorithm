def solution(n, lost, reserve):
    set_reverse = set(reserve)-set(lost)
    set_lost = set(lost)- set(reserve)
    #set자료형은 - 기호를 이용해 각 집합별로 차집합을 수행할 수 있지만 list자료형은 지원되지 않기 때문에 차집합으로 lost와 reserve의 공통되는 값을 제거
    #set 자료형을 쓴다고 해서 lost와 reserve의 값에는 변화가 없음
    for i in set_reverse:
        if i-1 in set_lost:
            set_lost.remove(i-1) #왼쪽 부터 해야함
        elif i+1 in set_lost:
            set_lost.remove(i+1)# #왼쪽에 없다면 오른쪽에 빌려줌

    return n-len(set_lost)