from tkinter import *
from tkinter import ttk
from pantallaIngreso import PantallaIngreso
from pantallaRemover import PantallaRemover
from solucionGui import SolucionGui
from metodosLagrangeNewton import *


class MetodoGui:

    puntosEnX = []
    puntosEnY = []
    puntosLabel = NotImplemented
    mostrarPasos = NotImplemented

    root = NotImplemented
    def __init__(self, l_window, window):
        self.method_window = l_window
        self.root = window

        ttk.Label(self.method_window, text="Ingrese punto en el plano: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.method_window, text='Ingresar Punto', command=self.abrirVentanaIngreso).pack(side=TOP, fill=BOTH, padx=5, pady=5)

        ttk.Button(self.method_window, text='Remover Punto', command=self.abrirVentanaRemover).pack(side=TOP, fill=BOTH, padx=5, pady=5)

        self.puntosLabel = ttk.Label(self.method_window, text="Puntos Ingresados: { }")
        self.puntosLabel.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Label(self.method_window, text="Seleccione si desea ver los pasos: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.mostrarPasos = IntVar()
        Checkbutton(self.method_window, text="Mostrar pasos", variable=self.mostrarPasos).pack(side=TOP, anchor = "center")#, padx = 10, pady = 10) 

        ttk.Button(self.method_window, text='Salir', command=self.root.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.method_window, text='Realizar', command=self.realizarMetodo).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def agregarPunto(self,x,y):
        self.puntosEnX.append(x)
        self.puntosEnY.append(y)
        self.formatearPuntos()

    def formatearPuntos(self):
        puntosTxt = ""

        for i in range(len(self.puntosEnX)):
            if i == 0:
                puntosTxt = "({0}; {1})".format(str(self.puntosEnX[i]), str(self.puntosEnY[i]))
            else:
                puntosTxt = puntosTxt + ", ({0}; {1})".format(str(self.puntosEnX[i]), str(self.puntosEnY[i]))

        puntosAMostrarTxt = "Puntos Ingresados: {" + puntosTxt + "}"

        self.puntosLabel["text"] = puntosAMostrarTxt
        

    def abrirVentanaIngreso(self):
        PantallaIngreso(self, self.root)
    
    def abrirVentanaRemover(self):
        PantallaRemover(self, self.root, self.puntosEnX, self.puntosEnY)

    def removerPunto(self, puntoARemover):
        self.puntosEnX.remove(puntoARemover[0])
        self.puntosEnY.remove(puntoARemover[1])
        self.formatearPuntos()
        

    def realizarMetodo(self):
        pass
    
    def miMetodo(self, funcion):
        pass