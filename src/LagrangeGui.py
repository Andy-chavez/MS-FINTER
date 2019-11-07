from tkinter import *
from tkinter import ttk
from pantallaIngreso import PantallaIngreso
from metodosLagrangeNewton import *

class LagrangeGui:

    puntosEnX = []
    puntosEnY = []
    puntosLabel = NotImplemented
    mostrarPasos = NotImplemented

    root = NotImplemented
    def __init__(self, l_window, window):
        self.lagrange_window = l_window
        self.root = window

        ttk.Label(self.lagrange_window, text="Ingrese punto en el plano: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.lagrange_window, text='Ingresar', command=self.abrirVentanaIngreso).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.puntosLabel = ttk.Label(self.lagrange_window, text="Puntos Ingresados: { }")
        self.puntosLabel.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Label(self.lagrange_window, text="Mostrar Pasos?: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        Checkbutton(self.lagrange_window, text="Check si quiere mostrar pasos.", variable=self.mostrarPasos).pack(side=TOP)

        ttk.Button(self.lagrange_window, text='Salir', command=self.lagrange_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.lagrange_window, text='Realizar', command=self.realizarMetodo).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def agregarPunto(self,x,y):
        self.puntosEnX.append(x)
        self.puntosEnY.append(y)
        puntosTxt = ""

        for i in range(len(self.puntosEnX)):
            if i == 0:
                puntosTxt = "({0}; {1})".format(str(self.puntosEnX[i]), str(self.puntosEnY[i]))
            else:
                puntosTxt = puntosTxt + ", ({0}; {1})".format(str(self.puntosEnX[i]), str(self.puntosEnY[i]))

        puntosAMostrarTxt = "Puntos Ingresados: {" + puntosTxt + "}"

        self.puntosLabel["text"] = puntosAMostrarTxt
        

    def realizarMetodo(self):
        print(self.puntosEnX)
        print(self.puntosEnY)
        lagrange(self.puntosEnX, self.puntosEnY)

    def abrirVentanaIngreso(self):
        PantallaIngreso(self, self.root)