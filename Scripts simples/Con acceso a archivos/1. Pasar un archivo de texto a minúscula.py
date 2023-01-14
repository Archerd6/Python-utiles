import pathlib
ruta = str(pathlib.Path(__file__).parent.resolve()) +'\\1.txt'
file = open(ruta, 'r')

lines = [line.lower() for line in file]

with open(ruta, 'w') as out:
    out.writelines(lines)