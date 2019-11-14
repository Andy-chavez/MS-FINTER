from tkinter import *
from tkinter import ttk
from ast import literal_eval

class PantallaRemover:

    puntoElegido = NotImplemented
    puntos = NotImplemented
    
    def __init__(self,instanciaDeMetodo, window, puntosEnX, puntosEnY):
        if(not puntosEnX):
            messagebox.showinfo("Error", "No hay puntos para remover")
            return
        self.configure_remover_window(instanciaDeMetodo, window, puntosEnX, puntosEnY)

    def configure_remover_window(self, instanciaDeMetodo, window, puntosEnX, puntosEnY):
        self.remover_window = Toplevel(window)
        self.instanciaDeMetodo = instanciaDeMetodo
        self.remover_window.geometry('300x200')
        self.remover_window.title("FINTER")
		
        self.puntoElegido = StringVar()

        elecciones = self.armarLista(puntosEnX, puntosEnY)
        self.puntoElegido.set(elecciones[0])
        popupMenu = ttk.OptionMenu(self.remover_window, self.puntoElegido, elecciones[0], *tuple(elecciones))
        ttk.Label(self.remover_window, text="Elija un punto a eliminar").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        popupMenu.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        ttk.Button(self.remover_window, text='Cancelar', command=self.remover_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.remover_window, text='Aceptar', command=self.cerrarVentana).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def armarLista(self, puntosEnX, puntosEnY):
        lista = []
        for i in range(len(puntosEnX)):
            lista.append("(" + str(puntosEnX[i]) + "," + str(puntosEnY[i]) + ")")
        print(tuple(lista))
        return lista

    def cerrarVentana(self):
        print(literal_eval(self.puntoElegido.get())[0])
        self.instanciaDeMetodo.removerPunto(literal_eval(self.puntoElegido.get()))
        self.remover_window.destroy()