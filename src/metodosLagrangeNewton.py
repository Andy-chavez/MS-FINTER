import numpy as np
# se podra usar? de todas formas no ayuda mucho con el hecho de que hay que mostrar los pasos,
# aparte creo que es lib externa

class MetodoLagrange:

    def calcularPolinomio(self, ptosX, ptosY) :
        return lagrange(ptosX, ptosY)

    def especializarEnPto(self, numero) :
        return self.calcularPolinomio(self)(numero)

def newtonRegre(listaX, listaY):
	matrizDeCoeficientes = []

	longX = len(listaX)
	longY = len(listaY)

	# Inicializo la matriz
	matrizDeCoeficientes = [[0 for i in range(longX + 1)] for j in range(longY + 1)]

	# Seteo las X
	j = longX-1
	y = longY-1
	for i in range(longX):
		matrizDeCoeficientes[i][0] = listaX[j]
		j = j-1

	# Seteo las Y
	for i in range(longY):
		matrizDeCoeficientes[i][1] = listaY[y]
		y = y-1

	# Calculo las diferencias
	for i in range(1, longX):
		k = i - 1
		for j in range(longX - i):
			matrizDeCoeficientes[j][i + 1] = (matrizDeCoeficientes[j + 1][i] - matrizDeCoeficientes[j][i]) / (
						matrizDeCoeficientes[j + 1 + k][0] - matrizDeCoeficientes[j][0])

#	print(matrizDeCoeficientes)

	raices = 1
	pol = 0
	for k in range(longX):
		for i in range(k):
			raices = np.poly1d([matrizDeCoeficientes[i][0]], True) * raices

		pol = pol + raices * matrizDeCoeficientes[0][k + 1]
		raices = 1
		print(pol)

	return pol

def newtonProgre(listaX, listaY):
	matrizDeCoeficientes = []

	longX = len(listaX)
	longY = len(listaY)

	#Inicializo la matriz
	matrizDeCoeficientes = [[ 0 for i in range(longX+1)] for j in range(longY+1) ] 

	#Seteo las X
	for i in range (longX):
		matrizDeCoeficientes[i][0] = listaX[i]

	#Seteo las Y
	for i in range (longY):
		matrizDeCoeficientes[i][1] = listaY[i]

	#Calculo las diferencias
	for i in range (1,longX):
		k = i - 1
		for j in range (longX - i):
			matrizDeCoeficientes[j][i+1] = (matrizDeCoeficientes[j+1][i] - matrizDeCoeficientes[j][i])/(matrizDeCoeficientes[j+1+k][0] - matrizDeCoeficientes[j][0])

	raices = 1
	pol = 0
	for k in range(longX):
		for i in range(k):
			raices = np.poly1d([matrizDeCoeficientes[i][0]], True) * raices

		pol = pol + raices * matrizDeCoeficientes[0][k+1]
		raices = 1
		print(pol)

	return pol

def especializar(pol, punto):
	return pol(punto)

def lagrange(listaX,listaY,mostrador):
	p = np.poly1d(0.0)
	longX = len(listaX)
	lagrangeDePto = 1

	for i in range(longX):
		for j in range(longX):
			if i == j:
				continue
			else:
				lagrangeDePto = (lagrangeDePto * np.poly1d([listaX[j]],True)/(listaX[i]-listaX[j]))
		p = p + lagrangeDePto*listaY[i]
		mostrador(i, p)
		lagrangeDePto = 1
	return p

#main para ir haciendo pruebitas
	
#import numpy as np --> np.NombreDeFuncionDeNumpy --> Te deja usar la funcion
#poly1d([1,2],True) genera el polinomio de las raices [1,2]
#poly1d([1,2]) arma el polinomio con esos coeficientes (x+2)(decreciente)
#Especializar --> pol(punto)