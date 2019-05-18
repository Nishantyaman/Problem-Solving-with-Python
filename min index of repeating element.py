from collections import Counter
arr = [5,6,3,4,3,6,4]
# arr = [5,3,3,3,3,3,3,3,4,4,4,3]

x=Counter(arr)

# repeat_list = []
# for i in set(x.elements()):
# 	if x[i]>1:
# 		repeat_list.append(i)

repeat_list=[i for i in set(x.elements()) if x[i]>1 ]

def get_min_index():
	for i in arr:
		if i in repeat_list:
			return arr.index(i);

print(get_min_index())


