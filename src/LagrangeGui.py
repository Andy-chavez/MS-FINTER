from tkinter import *
from tkinter import ttk
from metodoGui import MetodoGui
from solucionGui import SolucionGui
from metodosLagrangeNewton import lagrange

class LagrangeGui(MetodoGui):
    def realizarMetodo(self):
        puntosOrdenados = sorted(self.puntosEnX)
        equiespaciados = True
        ptosEquiespaciados = "No"
        if(len(puntosOrdenados) > 1):
            diferencia = self.modulo(puntosOrdenados[0] - puntosOrdenados[1])

        for i in range(len(puntosOrdenados) - 1):
            diferenciaEnI = self.modulo(puntosOrdenados[i] - puntosOrdenados[i+1])
            equiespaciados = (diferenciaEnI == diferencia) and equiespaciados
        if equiespaciados:
            ptosEquiespaciados = "Si"
        SolucionGui(self, self.root, ptosEquiespaciados, self.mostrarPasos.get(), self.puntosEnX, self.puntosEnY)
    
    def miMetodo(self, funcion):
        return lagrange(self.puntosEnX, self.puntosEnY, funcion)

    def agregarPasos(self, paso, polinomio):
        return self.polinomioParseadoParaListBox(str(polinomio).splitlines()[0].replace(' ', ''), str(polinomio).splitlines()[1])

    def polinomioParseadoParaListBox(self, potencias, polinomio):
        polinomioSpliteado = polinomio.split("x")
        
        for i in range(len(polinomioSpliteado)):
            if i >= len(potencias):
                break
            else:
                polinomioSpliteado[i+1] = "^" + potencias[i] + polinomioSpliteado[i+1]

        return "x".join(polinomioSpliteado)

    def modulo(self, numero):
        if(numero < 0):
            return numero * (-1)
        else:
            return numero