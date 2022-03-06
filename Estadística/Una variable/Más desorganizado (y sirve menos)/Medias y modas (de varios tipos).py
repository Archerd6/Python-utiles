#Tabla estadística

def Media(m,f):
    x=0
    for i in range(len(m)):
        x+=m[i]*f[i]
    suma=0
    for i in range(len(f)):
        suma+=f[i]
    x=x/suma
    return  x

def MediaPonderada(v,p):
    x=0
    for i in range(len(v)):
        x+=v[i]*p[i]
    suma=0
    for i in range(len(p)):
        suma+=p[i]
    x=x/suma
    return  x

def freq(lista):
    r={}            # Diccionario al principio vacio
    for elemento in lista:     # Para cada letra
        if elemento in r:  # Si ya esta
            r[elemento]+=1 # Le sumamos uno
        else:
            r[elemento]=1  # Si no esta, la creamos con el valor 1
    return r        # Devolvemos el diccionario lleno
    
    
def maxDict(diccionariox):
    listadevalores=[]
    for entrada in diccionariox:
        
        listadevalores+=[diccionariox[entrada]]
        
    maximo=listadevalores[0]
    
    for elemento in listadevalores:
        if elemento>maximo:
            maximo=elemento
            
    return maximo

def maximos(H,n):
    r=[]
    for key in H:
        if H[key]==n:
            if n in r:
                print("")
            else:
                r.append(key)
    return r

def Moda(k):
    n=maxDict(freq(k))
    return maximos(freq(k),n)

def ModaIntervalos(Intervalos,Frecuencias):
    
    Partes=Intervalos.split(" ")
    
    D=[]
    for i in range(len(Partes)):
        Partes[i]=Partes[i].strip("(")
        Partes[i]=Partes[i].strip("]")
    
    for i in range(len(Partes)):
        Partes[i]=Partes[i].split(",")
    
    for i in range(len(Partes)):
        primero=True
        valor=0
        for ii in range(len(Partes[i])):
            if primero:
                primero=False
                valor=Partes[i][ii]
            else:
                D.append(float(Partes[i][ii])-float(valor))
                primero=True
    Dic={}
    for i in range(len(D)):
        Dic[Intervalos.split(" ")[i]]=Frecuencias[i]/D[i]
            
    return maximos(Dic,maxDict(Dic))

#-------------------------------------------------------------
print("¡¡Cuidado, los ejemplos son de ejercicios diferentes!!")
print();

marcasdeclase=(18,21,23,25,27,29,31,34,38)

frecuencias=(30,40,35,25,15,15,20,10,10)

print("~ Media: ",Media(marcasdeclase,frecuencias))



valores=(2.6, 3.7, 5.1, 4.9, 6.4)
pesos=(1,1,1,2,3)

print("~ Media Ponderada: ",MediaPonderada(valores,pesos))
print()


A = (7,11,11,8,12,9,6,6)
B = (7,11,11,8,12,12,12,7,6,6)
C = (7,11,8,12,9,6)
print("~ Moda: ",Moda(A),"¡Pueden ser varios valores!")

Intervalos="(0,3] (3,5] (5,7]"
Frecuencias=(102,80,50)
print("~ Moda con intervalos: ",ModaIntervalos(Intervalos,Frecuencias))