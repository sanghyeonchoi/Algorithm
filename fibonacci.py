def fib(num):
    result =[]

    first = 1
    second = 1
    result.append(first)
    result.append(second)
    for i in range(2, num):
        third = first+second
        result.append(third)
        first = second
        second = third
    return result

print(fib(int(input())))
