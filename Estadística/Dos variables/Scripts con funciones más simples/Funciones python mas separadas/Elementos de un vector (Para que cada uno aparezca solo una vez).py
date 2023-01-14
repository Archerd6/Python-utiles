def ContarElementos(v):
    r = {}
    for i in range(len(v)):
        if(v[i] in r.keys()):
           r[v[i]] += 1 
        else:
            r[v[i]] = 1

    return list(r.keys())

print(ContarElementos([1,3,3]))