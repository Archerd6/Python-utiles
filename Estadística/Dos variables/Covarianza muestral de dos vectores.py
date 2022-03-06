def mediaDe(v):
    suma=0
    for elemento in v:
        suma+=elemento
    media=((suma)/(len(v)))
    
    return media

def Covarianza(x,y):
    cov = 0
    mediaX = mediaDe(x)
    mediaY = mediaDe(y)
    for i in range(len(x)):
        cov += (x[i]-mediaX)*(y[i]-mediaY)
    
    cov = cov/(len(x)-1)
    
    return cov

def info(n):
    if(n>0):
        return "La relación entre X e Y es directa, es decir, cuando X crece, Y también tiende a crecer, y viceversa"
    if(n<0):
        return "La relación es inversa, o sea, cuando X crece, Y tiende a decrecer, y viceversa"
    else:
        return "Las variables X e Y son incorreladas"

X = [0, 1, 3, -1, 2]
Y = [2, 6, 14, -2, 10]

print(Covarianza(X,Y)) # Covarianza muestral
print(info(Covarianza(X,Y)))