from tkinter import *
from tkinter import ttk
from metodoGui import MetodoGui
from solucionGui import SolucionGui
from metodosLagrangeNewton import lagrange

class LagrangeGui(MetodoGui):
    def realizarMetodo(self):
        equiespaciados = True
        ptosEquiespaciados = "No"
        if(len(self.puntosEnX) > 1):
            diferencia = self.modulo(self.puntosEnX[0] - self.puntosEnX[1])

        for i in range(len(self.puntosEnX) - 1):
            diferenciaEnI = self.modulo(self.puntosEnX[i] - self.puntosEnX[i+1])
            equiespaciados = (diferenciaEnI == diferencia) and equiespaciados
        if equiespaciados:
            ptosEquiespaciados = "Si"
        SolucionGui(self, self.root, ptosEquiespaciados, self.mostrarPasos.get())
    
    def miMetodo(self, funcion):
        return lagrange(self.puntosEnX, self.puntosEnY, funcion)

    def modulo(self, numero):
        if(numero < 0):
            return numero * (-1)
        else:
            return numero