def agregar_acentos_circunflejos(cadena):
    nueva_cadena = ''
    for letra in cadena:
        if letra.isalpha():
            nueva_cadena += letra + '\u0302'  # Agregar acento circunflejo después de cada letra
        else:
            nueva_cadena += letra
    return nueva_cadena

cadena = input("Ingresa una cadena: ")
cadena_con_acentos = agregar_acentos_circunflejos(cadena)
print("Respuesta:", cadena_con_acentos)
