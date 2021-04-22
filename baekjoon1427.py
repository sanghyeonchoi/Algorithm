n = int(input())

ls = list(str(n))

ls.sort(reverse=True)
print(int("".join(ls)))
