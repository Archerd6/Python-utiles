def suma(v):
    r = 0
    for elemento in v:
        r += elemento
    return r

def sumaColumna(n,matrizx):
    r = 0
    for fila in matrizx:
        r += fila[n]
    return r

def marginales(m):
    print("↓X   Y→ \n")
    for i in range(len(m)):
        for j in range (len(m[i])):
            print(str(m[i][j]) + " ",end="")
            if (j == len(m[i])-1):
                print("| " + str(suma(m[i])))
    
    print("-"*(len(m[1])*2),end="")
    print("▫")
    
    for j in range(len(m[1])):
        print(str(sumaColumna(j,m)) + " ",end="")
    
    SumaUltimaColumna = 0
    for j in range(len(m[1])):
        SumaUltimaColumna += sumaColumna(j,m)

    print(" " + str(SumaUltimaColumna))
    return

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

def ContarElementos(v):
    r = {}
    for i in range(len(v)):
        if(v[i] in r.keys()):
            r[v[i]] += 1 
        else:
            r[v[i]] = 1

    return list(r.keys())

def preparaMatriz(m,ny,nx):
    for i in range(ny):
        m.append([])
    for i in range(ny):
        for j in range(nx):
            m[i].append(0)
    
    return m

def Traspuesta(m):
    nm = []
    nm = preparaMatriz(nm,len(m[1]),len(m))
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            nm[j][i] = m[i][j]
    
    return nm

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

def vectoresAMatriz(X,Y):

    elementosx = ContarElementos(X)
    elementosy = ContarElementos(Y)
    elementosx.sort()
    elementosy.sort()

    equises = len(ContarElementos(X))
    ises = len(ContarElementos(Y))

    Diccionario_de_coordenadas = ContarTuplas(X,Y)
    X,Y = DtoVector(Diccionario_de_coordenadas)

    Matriz = []
    Matriz = preparaMatriz(Matriz,ises,equises)

    for i in range(ises):
        for j in range(equises):
            if(not (elementosx[j],elementosy[i]) in X):
                Matriz[i][j] = 0
            else:
                Matriz[i][j] = Diccionario_de_coordenadas[elementosx[j],elementosy[i]]

    Matriz = Traspuesta(Matriz)
    return Matriz

X,Y = ([75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 275, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550], [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 90, 90, 125, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 125, 125, 160, 50, 50, 50, 50, 50, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 160, 160, 160, 70, 70, 70, 70, 70, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 160, 160, 160, 160, 160, 160, 160, 160, 70, 90, 90, 125, 125, 125, 125, 125, 125, 125, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160])
Matriz = vectoresAMatriz(X,Y)
print(suma(Y)/len(Y))
print(Y)
marginales(Matriz)
#print(sonDependientes(X,Y))