from collections import Counter

l = Counter(d)
print(l.most_common(1)[0][0])

###############################################

d = [1,2,3,4,4]

print(max(d,key=d.count))

################################################
from collections import defaultdict

L = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]
d = defaultdict(int)
for i in L:
    d[i] += 1
result = max(d.items(), key=lambda x: x[1])
print(result)