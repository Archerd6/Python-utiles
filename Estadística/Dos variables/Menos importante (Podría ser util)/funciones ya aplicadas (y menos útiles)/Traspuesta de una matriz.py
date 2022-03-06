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

Matriz = [[0, 0, 2, 0, 0], [1, 3, 0, 0, 0], [0, 1, 0, 1, 1], [0, 1, 0, 0, 0]]

print(Traspuesta(Matriz))