#Crear una clase que contenga 2 métodos
#1.	Obtener número primo
#2.	Verificar si es número par.
class Numeros():
    def __init__(self, a):
        self.a = int(a)

    #Self.a para hacer referencia a la variable de la clase
    def primo(self):
        for i in range(2, self.a):
            if self.a % i == 0:
                print("No es primo, ", i, "es divisor")
                return False
        print("Es primo")
        return self.a

    def par(self):
        if self.a % 2 == 0:
            print('El número', self.a, 'es par.')
        else:
            print('El número', self.a, 'es impar.')
        return self.a

resultado = Numeros(7)

resultado.primo()
resultado.par()