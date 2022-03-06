def mediaDe(v):
    suma=0
    for elemento in v:
        suma+=elemento
    media=((suma)/(len(v)))
    
    return media

def desviacionEstandarPoblacional(v):
    lista=v
    media=mediaDe(v)
    
    # Ahora tenemos que hacer la sumatoria esa que sale en la formula :0
    sumatoria=0
    for num in lista:
        sumatoria+=(num-media)**2
    
    #                  len(lista)=N 

    desviacionEstandar= (sumatoria/(len(lista)))**0.5
    
    
    respuesta=desviacionEstandar

    
    return respuesta

def desviacionEstandarMuestral(v):
    lista=v
    media=mediaDe(v)
    
    # Ahora tenemos que hacer la sumatoria esa que sale en la formula :0
    sumatoria=0
    for num in lista:
        sumatoria+=(num-media)**2
    
    #                  len(lista)=N 

    desviacionEstandar= (sumatoria/((len(lista))-1))**0.5
    
    
    respuesta=desviacionEstandar

    
    return respuesta

vector = [1,2,2,3]
#print(desviacionEstandarPoblacional(vector))
print(desviacionEstandarMuestral(vector))