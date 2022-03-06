def mismosigno(a,b):
    if (a>0 and b>0):
        return True
    if (a<0 and b<0):
        return True
    if (a==0 and b==0):
        return True
    
    else:
        return False
    

def comprueba(x,y):
    x = x.split("+")
    y = y.split("+")
    
    xb = float(x[1].strip("x"))
    yb = float(y[1].strip("y"))
    return mismosigno(xb,yb)


ysobrex = "y = 1 + 2x"

xsobrey = "x = 10 + 5y"

print(comprueba(ysobrex,xsobrey))  # Si es verdadero SI pueden ser regresiones de las mismas variables | si es falso NO