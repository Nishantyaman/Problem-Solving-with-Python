#https://www.hackerrank.com/contests/hourrank-30/challenges/video-conference
from collections import defaultdict

def solve(names):
    s = set()
    d = defaultdict(int)
    l = list()
    for name in names:
        if name in d:
            d[name] += 1
            l.append(name+" "+str(d[name]))
        else:
            d[name] = 1
            t = ""
            inserted = False;
            for i in range(len(name)):
                t += name[i:i+1]
                if t not in s and not inserted:
                    inserted = True
                    l.append(t)
                s.add(t)
            if not inserted:
                l.append(name)
    return l

a=solve(['nis','nishant','nis'])
print(a)

# n = 3
# seen = {}
# for _ in range(n):
#     enter='nis nishant nish'
#     name = enter.strip()
#     l = len(name)
#     this_done = False
#     for x in range(1, l+1):
#         cur_name = name[:x]
#         if not this_done and cur_name not in seen:
#             print(cur_name)
#             this_done = True
#         seen.setdefault(cur_name, 0)
#     seen[name] += 1
#     if not this_done and seen[name] == 1:
#         print(name)
#     elif not this_done:
#         print('{} {}'.format(name, seen[name]))
