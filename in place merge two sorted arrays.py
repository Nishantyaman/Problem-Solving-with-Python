X = [1,4,7,8,10]
Y=[2,3,9]

Z = X+Y
Z.sort()

X = Z[:len(X)]
Y = Z[len(X):]

print(X,Y)
