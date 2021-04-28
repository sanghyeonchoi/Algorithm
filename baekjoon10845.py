import sys

input = sys.stdin.readline

n = int(input())

queue = []
def push(X):
    return queue.append(X)
def pop():
    if (not queue):
        return -1
    else:
        return queue.pop(0)
def size():
    return len(queue)
def empty():
    return 0 if queue else 1
def front():
    return queue[0] if queue else -1
def back():
    return queue[-1] if queue else -1


for _ in range(n):
    x = input().rstrip().split()
    order = x[0]
    if order == "push":
        push(x[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())
