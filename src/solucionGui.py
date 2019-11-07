from tkinter import *
from tkinter import ttk

class SolucionGui:
    solucion_window = NotImplemented

    def __init__(self, root, polinomio, equiespaciados, pasos, mostrarLosPasos):
        self.solucion_window = Toplevel(root)
        self.solucion_window.geometry('500x500')
        self.solucion_window.title("FINTER")
        ttk.Label(self.solucion_window, text="Son Equiespaciados: {}".format(equiespaciados)).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Label(self.solucion_window, text="Grado: {}".format(polinomio.order)).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.mostrarPasos(pasos, mostrarLosPasos)
        ttk.Label(self.solucion_window, text="Resultado Final: {}".format(str(polinomio))).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.especializarPolinomio(polinomio)
        ttk.Button(self.solucion_window, text='Salir', command=self.solucion_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)


    def mostrarPasos(self, pasos, mostrarlos):
        pass

    def especializarPolinomio(self, polinomio):
        pass

