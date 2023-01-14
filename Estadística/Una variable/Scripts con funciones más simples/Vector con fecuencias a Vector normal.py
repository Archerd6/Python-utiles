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

vector=("0p2", "2p4", "3p2", "4p2", "7p2")
vector=conFrecuencias(vector)                                        # 0p2  significa:  'cero' repetido 'dos' veces

print(vector)