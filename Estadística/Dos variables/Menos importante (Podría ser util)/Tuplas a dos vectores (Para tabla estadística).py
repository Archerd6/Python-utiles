def tuplasAVector(t):
    x=[]
    y=[]
    for i in range(len(t)):
        x.append(t[i][0])
        y.append(t[i][1])

    return x,y

tuplas=[(0, 2), (1, 6), (3, 14), (-1, -2), (2, 10)]
print(tuplasAVector(tuplas))