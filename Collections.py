from collections import Counter
a = 'aaabbabccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))