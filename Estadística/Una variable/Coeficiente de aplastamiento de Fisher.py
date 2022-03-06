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

def momentoCentral(vector,orden):
    n = mediaDe(vector)
    sum = 0
    for elemento in vector:
        sum += (elemento-n)**orden
    
    return sum/len(vector)


def coeficienteApuntamientoFisher(vector):
    
    return (((momentoCentral(vector,4))/((desviacionEstandarPoblacional(vector))**4))-3)

def dimeInformacion(n):
    
    if(n<0):
        return "Menos apuntamiento que la normal (Platicúrtica)"
    if(n>0):
        return "Más apuntamiento que la normal (Leptocúrtica)"
    if(n==0):
        return " Igual apuntamiento que la normal (Mesocúrtica)"
    
vector=(1,2,3,4,5,5,6)
print(coeficienteApuntamientoFisher(vector))
print("\n"+dimeInformacion(coeficienteApuntamientoFisher(vector)))