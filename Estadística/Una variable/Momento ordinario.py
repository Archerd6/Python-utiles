def mediana(vector):
    posicion = len(vector)*0.5
    if (posicion).is_integer():
        return ((vector[int(posicion-1)] + vector[int(posicion)])/2)
    else:
        return (vector[int(posicion)])
    
def media(v):
    suma = 0
    for elemento in v:
        suma += elemento
    media = ((suma)/(len(v)))
    
    return media

def conFrecuencias(v):
    r = []
    for elemento in v:
        if(isinstance(elemento, str)):
            valor = int(elemento.split("p")[0])
            frecuencia = int(elemento.split("p")[1])
            for i in range (frecuencia):
                r.append(valor)     
        else:
            r.append(elemento)
    return r
    
def momentoOrdinario(n,vector,orden):
    sum = 0
    for elemento in vector:
        sum += (elemento-n)**orden
    
    return sum/len(vector)

vector=("0p2", "2p4", "3p2", "4p2", "7p2")
vector=conFrecuencias(vector)                                        # 0p2  significa:  'cero' repetido 'dos' veces
orden=1
punto=(mediana(vector))
#Punto=(0)
#punto=media(vector)
print(momentoOrdinario(punto,vector,orden))