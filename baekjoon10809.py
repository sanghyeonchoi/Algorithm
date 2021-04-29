# import string

# a = input()
# for i in string.ascii_lowercase:
#     print(a.find(i), end=" ")



s = input()

for i in range(26):
    ch = chr(i+ord('a'))
    print(s.find(ch), end=" ")