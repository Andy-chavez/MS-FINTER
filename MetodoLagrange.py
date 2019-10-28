from scipy.interpolate import lagrange
# se podra usar? de todas formas no ayuda mucho con el hecho de que hay que mostrar los pasos,
# aparte creo que es lib externa

class MetodoLagrange:

    def calcularPolinomio(self, ptosX, ptosY) :
        return lagrange(ptosX, ptosY)

    def especializarEnPto(self, numero) :
        return self.calcularPolinomio(self)(numero)
