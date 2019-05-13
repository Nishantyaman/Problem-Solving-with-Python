a=[6,0,8,0,2,0,3,0,4,0,1]
def arrange(a):
	count = 0
	for i in range(len(a)-1,-1,-1):
	   if a[i] == 0:
	      del a[i]
	      count+=1

	a.extend([0]*count)
	return a

print(arrange(a))
