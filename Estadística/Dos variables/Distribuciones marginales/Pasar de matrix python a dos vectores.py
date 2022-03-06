def MatrizAVectores(m,x,y):
    X = []
    Y = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            for k in range(m[i][j]):
                Y.append(y[i])
                X.append(x[j])
    
    return Y,X



Matriz = [[20, 18, 2, 1, 0], [25, 40, 30, 2, 1], [5, 10, 15, 25, 3], [0, 5, 15, 20, 8], [0, 1, 2, 7, 10]]

xtabla = [75,150,275,425,550]
ytabla = [50,70,90,125,160]

print(MatrizAVectores(Matriz,ytabla,xtabla))