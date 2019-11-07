from tkinter import *
from tkinter import ttk
from metodoGui import MetodoGui
from solucionGui import SolucionGui
from metodosLagrangeNewton import *

class LagrangeGui(MetodoGui):
    def realizarMetodo(self):
        SolucionGui(self, self.root, True, self.mostrarPasos.get())
    
    def miMetodo(self, funcion):
        return lagrange(self.puntosEnX, self.puntosEnY, funcion)