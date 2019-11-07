from tkinter import *
from tkinter import ttk
from metodosLagrangeNewton import especializar

class SolucionGui:
    solucion_window = NotImplemented
    pasos = "Pasos: "
    valorK = NotImplemented
    polinomio = NotImplemented

    def __init__(self, claseMetodo, root, equiespaciados, mostrarLosPasos):
        self.polinomio = self.realizarMetodo(claseMetodo, mostrarLosPasos)
        self.solucion_window = Toplevel(root)
        self.solucion_window.geometry('500x500')
        self.solucion_window.title("FINTER")
        validateDigit = self.solucion_window.register(self.isADigit)

        ttk.Label(self.solucion_window, text="Son Equiespaciados: {}".format(equiespaciados)).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Label(self.solucion_window, text="Grado: {}".format(self.polinomio.order)).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Label(self.solucion_window, text=self.pasos).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Label(self.solucion_window, text="Resultado Final: {}".format(str(self.polinomio))).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.valorK = ttk.Entry(self.solucion_window, validate='key', validatecommand=(validateDigit, '%P'))
        ttk.Label(self.solucion_window, text="especializar Polinomio en: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.valorK.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        
        
        ttk.Button(self.solucion_window, text='Especializar', command=self.especializarPolinomio).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.solucion_window, text='Salir', command=self.solucion_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def isADigit(self, text):
        try:
            float(text)
        except ValueError:
            return False
        return True

    def realizarMetodo(self, claseMetodo, mostrarPasos):
        if mostrarPasos:
            return claseMetodo.miMetodo(self.agregarPasos)
        else:
            return claseMetodo.miMetodo(self.pase)

    def agregarPasos(self, paso, polinomio):
        self.pasos += "\nPaso {0}: {1}\n".format(str(paso), str(polinomio))

    def pase(self, paso, polinomio):
        pass

    def especializarPolinomio(self):
        print(especializar(self.polinomio, int(self.valorK.get())))

