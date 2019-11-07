from tkinter import *
from tkinter import ttk
from metodoGui import MetodoGui
from solucionGui import SolucionGui
from metodosLagrangeNewton import newtonProgre, newtonRegre

class NewtonGui(MetodoGui):
    def __init__(self, l_window, window):
        MetodoGui.__init__(self, l_window, window)

        self.metodoNewton = StringVar(self.root)

        elecciones = {"regresivo", "progresivo"}
        self.metodoNewton.set("regresivo")
        popupMenu = OptionMenu(self.method_window, self.metodoNewton, *elecciones)
        ttk.Label(self.method_window, text="elija un metodo a utilizar").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        popupMenu.pack(side=TOP, fill=BOTH, padx=5, pady=5)

    def realizarMetodo(self):
        SolucionGui(self, self.root, True, self.mostrarPasos.get())

    def miMetodo(self, funcion):
        if self.metodoNewton == "regresivo":
            return newtonRegre(self.puntosEnX, self.puntosEnY)
        else:
            return newtonProgre(self.puntosEnX, self.puntosEnY)
