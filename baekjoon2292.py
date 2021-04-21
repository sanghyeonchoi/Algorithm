n = int(input())

start = 1
plus = 6
count = 1

while n > start:
    count += 1
    start += plus
    plus += 6
print(count)
