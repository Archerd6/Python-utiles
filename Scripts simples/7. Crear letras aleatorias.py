import random
def AleatorioLetras(Cantidad_de_letras):
    c = ''
    cantidad = Cantidad_de_letras             # Numero de letras
    for i in range(cantidad): 
        
        c = c + (str(random.randint(1,26)))   # Numeros del 1 al 26
        
        if(i < (cantidad-1)):
            c = c + ' '                       # Separo por espacio

    l = c.split(' ')                          # Creo una lista con los numeros random


    numerosAletras = {                        # Diccionario para pasar de numeros a las letras
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J',
        11: 'K',
        12: 'L',
        13: 'M',
        14: 'N',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
        26: 'Z'
    }
    
    l2 = []
    for numero in l:                               # Para cada numero en l
        for i in numerosAletras:
            
            if(str(i) == str(numero)):             # Comprobamos si ese numero esta en el diccionario
                l2.append(numerosAletras[i])

    return ''.join(l2)

print(AleatorioLetras(8))