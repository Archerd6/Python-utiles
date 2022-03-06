def mediaDe(v):
    suma=0
    for elemento in v:
        suma+=elemento
    media=((suma)/(len(v)))
    
    return media

def desviacionEstandarMuestral(v):
    lista=v
    media=mediaDe(v)
    
    # Ahora tenemos que hacer la sumatoria esa que sale en la formula :0
    sumatoria=0
    for num in lista:
        sumatoria+=(num-media)**2
    
    #                  len(lista)=N 

    desviacionEstandar= (sumatoria/(len(lista)-1))**0.5
    
    
    respuesta=desviacionEstandar

    
    return respuesta

def Covarianza(x,y):
    cov = 0
    mediaX = mediaDe(x)
    mediaY = mediaDe(y)
    for i in range(len(x)):
        cov += (x[i]-mediaX)*(y[i]-mediaY)
    
    cov = cov/(len(x)-1)
    
    return cov

X = [0, 1, 3, -1, 2]
Y = [2, 6, 14, -2, 10]

print(Covarianza(X,Y)/(desviacionEstandarMuestral(X)*desviacionEstandarMuestral(Y))) # La covarianza es muestral