#encoding: utf-8

a = [[1,0,0],[0,1,0],[0,0,1]]

contador = 0
contador1 = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j and a[i][j] == 1:
            contador+=1
        elif i != j and a[i][j] == 0:
            contador1+=1

if contador == len(a) and contador1 == len(a)*len(a)-len(a):
    print 'A matriz é identidade!'
else:
    print 'A matriz não é identidade!'

