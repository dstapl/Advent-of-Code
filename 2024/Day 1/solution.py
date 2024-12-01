# Each line is <int> [spaces] <int>
file = open(0).readlines()

lists = [[int(x.strip()) for x in filter(lambda y:y, line.split(" "))] for line in file]
lists = [list(x) for x in zip(*lists)]


## Part 1
total_dist = sum(abs(x[0]-x[1]) for x in zip(*map(sorted, lists)))
print(total_dist)


## Part 2
from collections import Counter

occurences = Counter(lists[1])
similarity_score = sum(num*occurences[num] for num in lists[0])
print(similarity_score)
