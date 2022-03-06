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


X = [1,2,3,4]
Y = [2,4,8,16]

b = Covarianza(X,Y)/Covarianza(Y,Y) # Covarianza muestral
a = mediaDe(X) - (b*mediaDe(Y))


print("x = " + str(a) + " + " + str(b) + "y")