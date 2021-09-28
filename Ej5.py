# Requerir al usuario que ingrese un número entero positivo
# Imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del cuádruple del mismo.
a = input("Indica un número entero positivo: ")
num = int(a)

if num <= 0:
    exit()
else:
    limite = (4 * num - 1)
    print("El limite es ", limite)
    while num <= limite:
        print(num)
        num += 1