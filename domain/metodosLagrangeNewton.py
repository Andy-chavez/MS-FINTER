from scipy.interpolate import lagrange
import numpy as np
# se podra usar? de todas formas no ayuda mucho con el hecho de que hay que mostrar los pasos,
# aparte creo que es lib externa

class MetodoLagrange:

    def calcularPolinomio(self, ptosX, ptosY) :
        return lagrange(ptosX, ptosY)

    def especializarEnPto(self, numero) :
        return self.calcularPolinomio(self)(numero)

def newtonProgre(listaX, listaY):
	matrizDeCoeficientes = []

	longX = len(listaX)
	longY = len(listaY)

	matrizDeCoeficientes = [[ 0 for i in range(longX)] for j in range(longY) ] 

	#Paso las X
	for i in range (longX):
		matrizDeCoeficientes[i][0] = listaX[i]

	#Paso las Y
	for i in range (len(listaY)):
		matrizDeCoeficientes[i][1] = listaY[i]

	print(matrizDeCoeficientes)

def main():
	newtonProgre([1,2],[3,4])

if __name__ == "__main__":
    main()

#poly1d([1,2],True) genera el polinomio de las raices [1,2]
#poly1d([1,2]) arma el polinomio con esos coeficientes (x+2)(decreciente)