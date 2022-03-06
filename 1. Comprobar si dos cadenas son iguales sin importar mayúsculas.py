def iguales(primeraLista,segundaLista):
    r=False
    A=[]
    B=[]
    
    for i in range (len(primeraLista)):
        A += (primeraLista[i].upper())
        
    for i in range (len(segundaLista)):
        B += (segundaLista[i].upper())
        
    if (A == B):
        r=True
    return r


A = 'hola'
B = 'jola'

print(iguales(A,B))