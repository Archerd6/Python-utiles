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


def coeficienteAsimetriaFisher(vector):
    
    return (momentoCentral(vector,3))/((desviacionEstandarPoblacional(vector))**3)

def dimeInformacion(n):
    
    if(n<0):
        return "Distribución asimétrica inzquierda/negativa  (¡¡¡Hay más elementos a la derecha!!!)"
    if(n>0):
        return "Distribución asimétrica derecha/positiva  (¡¡¡Hay más elementos a la izquierda!!!)"
    if(n==0):
        return "Distribución simétrica"
    
vector=[18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 23.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 29.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 34.0, 34.0, 34.0, 34.0, 34.0, 34.0, 34.0, 34.0, 34.0, 34.0, 38.0, 38.0, 38.0, 38.0, 38.0, 38.0, 38.0, 38.0, 38.0, 38.0]
print(coeficienteAsimetriaFisher(vector))
print("\n"+dimeInformacion(coeficienteAsimetriaFisher(vector)))