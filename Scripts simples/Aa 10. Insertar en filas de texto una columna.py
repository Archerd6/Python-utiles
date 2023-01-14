import pathlib

def mayor_longitud(Lista):
    maximo = Lista[0]
    for linea in Lista:
        if (len(linea) > len(maximo)):
            maximo = linea
    return len(maximo)

condimentos = ['Pimienta','Oregano','Perejil','Azafran','Ajo','Canela','Romero','Albahaca','Tomillo','Laurel']
Lineas = []

for i in range(10):
    Lineas.append(''.join([str(2021-i),'    -    ',condimentos[i]]))


# ----- Para que las filas tengan la misma longitud -----
Maxima_longitud_de_linea = mayor_longitud(Lineas)

for o in range(10):
    if(len(Lineas[o]) < Maxima_longitud_de_linea): # Si esa linea no tiene la maxima longitud
        
        # Le añadimos espacios al final
        Lineas[o] = ''.join( [ Lineas[o] , (' '*(Maxima_longitud_de_linea - len(Lineas[o]))) ] )




# Lineas es el array con las filas (strings)

ruta = str(pathlib.Path(__file__).parent.resolve()) +'\\Aa 10.txt'
file = open(ruta, 'r')
lines = [line for line in file]

for e in range(len(lines)):    # Para quitar las \n
    if('\n' in lines[e]):
        lines[e] = lines[e].replace('\n','')

for f in range(len(Lineas)):
    Lineas[f] = ''.join([Lineas[f],'    -   ', lines[f]])
    print(Lineas[f])


