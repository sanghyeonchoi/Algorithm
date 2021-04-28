import sys 

input = sys.stdin.readline

    

n= int(input())
deque = []
def push_front(X):
    return deque.insert(0,X)

def push_back(X):
    return deque.append(X)

def pop_front():
    if (not deque):
        return -1
    else:
        return deque.pop(0)
def pop_back():
    if (not deque):
        return -1
    else:
        return deque.pop(-1)
def size():
    return len(deque)
def empty():
    return 0 if deque else 1
def front():
    return deque[0] if deque else -1
def back():
    return deque[-1] if deque else -1

for _ in range(n):
    x = input().rstrip().split()

    order = x[0]

    if order == "push_front": 
        push_front(x[1])
    elif order == "push_back":
        push_back(x[1])
    elif order == "pop_front":
        print(pop_front())
    elif order == "pop_back":
        print(pop_back())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())