# Antiguo
OldMax = 90
OldMin = -90
OldValue = 0 # Un valor (Entre minimo y maximo)

# Nuevo
NewMax = 180
NewMin = 0

OldRange = (OldMax - OldMin)
NewRange = (NewMax - NewMin)

NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

print("El valor ",OldValue, " en el intervalo antiguo pasaría en el intervalo nuevo a: ",NewValue)