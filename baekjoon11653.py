n = int(input())

sosu = 2
list = []

while n != 1:
    if n % sosu == 0:
        n = n/sosu
        print(sosu)
    else:
        sosu += 1
