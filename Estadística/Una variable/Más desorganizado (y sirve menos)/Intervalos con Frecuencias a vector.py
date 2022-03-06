def IntervalosFrecuenciasAVector(I,F):
    r = []
    I = I.split()
    
    for i in range(len(I)):
        I[i] = I[i].lstrip("(")
        I[i] = I[i].rstrip("]")
        I[i] = I[i].split(",")
        for j in range(len(I[i])):
            I[i][j] = float(I[i][j])
    
    for i in range(len(I)):
        for j in range(F[i]):
            r.append((I[i][0]+I[i][1])/2)
    
    
    return r




Intervalos="(16,20] (20,22] (22,24] (24,26] (26,28] (28,30] (30,32] (32,36] (36,40]"
Frecuencias=[30   ,   40   ,  35   ,  25   ,  15   ,   15  ,   20  ,   10  ,   10]

print(IntervalosFrecuenciasAVector(Intervalos,Frecuencias))