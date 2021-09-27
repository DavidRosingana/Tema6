año_actual = input("En que año estamos? ")

año_azar = input("Elige otro año al azar: ")

if año_azar == año_actual:
    print("Es el mismo año")

elif año_azar < año_actual:
    print("Aun faltan ", int(año_actual) - int(año_azar), " años para llegar al año actual")

else:
    print("Estamos a ", int(año_azar) - int(año_actual), " años para llegar al año elegido")