def retnum(nf):
    l = [] 
    f = open(nf)
    for lin in f:
        l += [lin.split()]
    # ¡Tenemos una lista con strings! vamos a pasarla para que sean números
    for i in range(len(l)):
        for j in range (len(l[i])):
            l[i][j]=int(l[i][j])
    # Ya lo tenemos :)
    
    return l

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

Matriz = retnum('Números de tabla estadistica.txt')
print(Matriz)
marginales(Matriz)