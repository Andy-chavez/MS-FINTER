from tkinter import *
from tkinter import ttk
from metodoGui import MetodoGui
from solucionGui import SolucionGui
from metodosLagrangeNewton import newtonProgre, newtonRegre

class NewtonGui(MetodoGui):
    def __init__(self, l_window, window):
        MetodoGui.__init__(self, l_window, window)

        self.metodoNewton = StringVar(self.root)

        elecciones = {"Regresivo", "Progresivo"}
        self.metodoNewton.set("Regresivo")
        popupMenu = OptionMenu(self.method_window, self.metodoNewton, *elecciones)
        ttk.Label(self.method_window, text="Elija un metodo a utilizar").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        popupMenu.pack(side=TOP, fill=BOTH, padx=5, pady=5)

    def realizarMetodo(self):
        puntosOrdenados = sorted(self.puntosEnX)
        equiespaciados = True
        ptosEquiespaciados = "No"
        if(len(puntosOrdenados) > 1):
            diferencia = self.modulo(puntosOrdenados[0] - puntosOrdenados[1])
        for i in range (len(self.puntosEnX) - 1):
            diferenciaEnI = self.modulo(puntosOrdenados[i] - puntosOrdenados[i+1])
            equiespaciados = (diferenciaEnI == diferencia) and equiespaciados
        if equiespaciados:
            ptosEquiespaciados = "Si"
        SolucionGui(self, self.root, ptosEquiespaciados, self.mostrarPasos.get(), self.puntosEnX, self.puntosEnY)

    def miMetodo(self, funcion):
        if self.metodoNewton.get() == "Regresivo":
            return newtonRegre(self.puntosEnX, self.puntosEnY,funcion)
        else:
            return newtonProgre(self.puntosEnX, self.puntosEnY, funcion)

    def agregarPasos(self, paso, polinomio):
        return str(polinomio)

    def modulo(self, numero):
        if(numero < 0):
            return numero * (-1)
        else:
            return numero
