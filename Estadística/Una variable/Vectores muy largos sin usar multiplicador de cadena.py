def Rep(X):
    r = []
    
    for i in range(len(X)):
        for j in range(X[i][1]):
            r.append(X[i][0])
    
    return r



x = [(0,10),(1,8),(2,12),(3,9),(4,7),(5,3)]               #    ("El numero que se repite" , "Las veces que se repite")

print(Rep(x))