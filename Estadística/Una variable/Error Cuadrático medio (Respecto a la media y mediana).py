def dif(n1,n2):                                     # Difecencia en valor absoluto
    return abs(n1-n2)

def media(v):
    suma=0
    for elemento in v:
        suma+=elemento
    media=((suma)/(len(v)))
    
    return media

def ECMmedia(vector):                                # Error cuadrático medio RESPENTO A LA MEDIA:
    diferencias=0
    lamedia=media(vector)
    for elemento in vector:
        diferencias+=(dif(elemento,lamedia))**2
    
    return diferencias/len(vector)




def mediana(vector):
    posicion=len(vector)*0.5
    if (posicion).is_integer():
        return((vector[int(posicion-1)]+vector[int(posicion)])/2)
    else:
        return(vector[int(posicion)])

def ECMmediana(vector):                                # Error cuadrático medio RESPENTO A LA MEDIANA:
    diferencias=0
    Mediana=mediana(vector)
    
    for elemento in vector:
        diferencias+=(dif(elemento,Mediana))**2
    
    return diferencias/len(vector)

v=(5, 2, 3, 3, 3, 5, 7)
print("Error cuadrático medio respecto a la media: "+str(ECMmedia(v)))
print("Error cuadrático medio respecto a la mediana: "+str(ECMmediana(v)))