from collections import defaultdict

d = defaultdict(int)
s = "helloworld"
for c in s:
    d[c] += 1
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0])