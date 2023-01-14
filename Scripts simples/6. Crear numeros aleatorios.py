import random
def Aleatorio(Cantidad_de_cifras,DEL,AL):  # Numeros DEL 0 AL 9 (Ejemplo)
    c = ''
    for _ in range(Cantidad_de_cifras):
        c = c + (str(random.randint(DEL,AL)))
    return c


print(Aleatorio(5,0,9))