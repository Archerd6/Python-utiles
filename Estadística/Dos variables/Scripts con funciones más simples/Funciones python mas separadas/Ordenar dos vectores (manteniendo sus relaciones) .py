def OrdenarDiccionario(D):
    
    return dict(sorted(D.items()))

def Diccionario(x,y):
    D ={}
    
    for i in range(len(x)):
        if (x[i]) in D.keys():
            D[x[i]] = [D[x[i]],y[i]]
        else:
            D[x[i]] = y[i]
    
    return D

def DtoVector(D):
    x = []
    y = []
    
    for elemento in D:
        if(isinstance(D[elemento], list)):
            for i in range(len(D[elemento])):
                x.append(elemento)
                y.append(D[elemento][i])
        else:
            x.append(elemento)
            y.append(D[elemento])
    
    return x,y

def Reordena(x,y):
    D=Diccionario(x,y)
    DO=OrdenarDiccionario(D)
    return DtoVector(DO)

X = [3,2,4,2]
Y = [2,5,4,3]

print(Reordena(X,Y))