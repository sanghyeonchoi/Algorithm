n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input())

set_word_list = list(set(word_list))  # 중복제거

sort_word_list = []

for j in set_word_list:
    sort_word_list.append((len(j), j))
sort_word_list.sort()

for count, word in sort_word_list:
    print(word)
