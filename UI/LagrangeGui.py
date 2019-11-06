from tkinter import *
from tkinter import ttk
from pantallaIngreso import PantallaIngreso

class LagrangeGui:

    puntosEnX = []
    puntosEnY = []

    root = NotImplemented
    def __init__(self, l_window, window):
        self.lagrange_window = l_window
        self.root = window

        ttk.Label(self.lagrange_window, text="Ingrese punto en el plano: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.lagrange_window, text='Ingresar', command=self.abrirVentanaIngreso).pack(side=TOP, fill=BOTH, padx=5, pady=5)

        ttk.Button(self.lagrange_window, text='Salir', command=self.lagrange_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.lagrange_window, text='Realizar').pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def agregarPunto(self,x,y):
        self.puntosEnX.append(x)
        self.puntosEnY.append(y)

    def abrirVentanaIngreso(self):
        PantallaIngreso(self, self.root)