def ContarTuplas(x,y):
    D ={}
    
    for i in range(len(x)):
        primero=x[i]
        segundo=y[i]
        if (primero,segundo) in D.keys():
            D[(primero,segundo)] += 1
        else:
            D[(primero,segundo)]=1
    
    return D

X = [3,2,4,2,1,2,5,2,3,2]
Y = [2,5,4,3,3,4,4,3,2,3]
print(ContarTuplas(X,Y))