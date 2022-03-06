def Rep(X):
    r = []
    
    for i in range(len(X)):
        for j in range(X[i][1]):
            r.append(X[i][0])
    
    return r



x = [(1,3),(2,5),(3,3)]               #    ("El numero que se repite" , "Las veces que se repite")

print(Rep(x))