from tkinter import *
from tkinter import ttk
from metodosLagrangeNewton import especializar
from ast import literal_eval
from tkinter import messagebox

class PantallaIngreso:

	xAxisEntry = NotImplemented
	yAxisEntry = NotImplemented
	ingreso_window = NotImplemented
	instanciaDeMetodo = NotImplemented

	def __init__(self,instanciaDeMetodo, window):
		self.configure_ingreso_window(instanciaDeMetodo, window)

	def configure_ingreso_window(self, instanciaDeMetodo, window):
		self.ingreso_window = Toplevel(window)
		self.instanciaDeMetodo = instanciaDeMetodo
		self.ingreso_window.geometry('300x200')
		self.ingreso_window.title("FINTER")
		validateDigit = self.ingreso_window.register(self.isADigit)
		self.xAxisEntry = ttk.Entry(self.ingreso_window, validate='key', validatecommand=(validateDigit, '%P'))
    
		self.yAxisEntry = ttk.Entry(self.ingreso_window, validate='key', validatecommand=(validateDigit, '%P'))

		ttk.Label(self.ingreso_window, text="Eje x: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
		self.xAxisEntry.pack(side=TOP, fill=BOTH, padx=5, pady=5)
		ttk.Label(self.ingreso_window, text="Eje y: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
		self.yAxisEntry.pack(side=TOP, fill=BOTH, padx=5, pady=5)

		ttk.Button(self.ingreso_window, text='Aceptar', command=self.cerrarVentana).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

	def isADigit(self, text):
		try:
			float(text)
		except ValueError:
			messagebox.showerror("Error", "Ingreso invalido. Pruebe ingresando numeros.")
			return False
		return True

	def cerrarVentana(self):
		if(self.yAxisEntry.get()=='' or self.xAxisEntry.get()==''):
			messagebox.showerror("Error", "Ingreso invalido. Pruebe ingresando numeros en ambos campos.")
			return
		self.instanciaDeMetodo.agregarPunto(int(self.xAxisEntry.get()),int(self.yAxisEntry.get()))
		self.ingreso_window.destroy()

class PantallaRemover:

    puntoElegido = NotImplemented
    puntos = NotImplemented
    
    def __init__(self,instanciaDeMetodo, window, puntosEnX, puntosEnY):
        if(not puntosEnX):
            messagebox.showerror("Error", "No hay puntos para remover")
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

class SolucionGui:
    solucion_window = NotImplemented
    pasos = "Pasos: "
    valorK = NotImplemented
    polinomio = NotImplemented
    especializacion = NotImplemented
    puntosEnX = []
    puntosEnY = []
    pasosDelMetodo = []

    def __init__(self, claseMetodo, root, equiespaciados, mostrarLosPasos, unosPuntosEnX, unosPuntosEnY):
        self.puntosEnX = unosPuntosEnX
        self.puntosEnY = unosPuntosEnY
        self.metodoClase = claseMetodo
        self.mostrarPasos = mostrarLosPasos

        try:
            self.polinomio=self.realizarMetodo(claseMetodo, mostrarLosPasos)
        except:
            messagebox.showerror("Error", "hubo un error al realizar el metodo")
            return

        #self.polinomio = self.realizarMetodo(claseMetodo, mostrarLosPasos)
        self.solucion_window = Toplevel(root)
        self.solucion_window.geometry('500x500')
        self.solucion_window.title("FINTER")
        validateDigit = self.solucion_window.register(self.isADigit)

        self.puntosLabel = ttk.Label(self.solucion_window, text="Puntos Ingresados: { }")
        self.puntosLabel.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.formatearPuntos()

        ttk.Label(self.solucion_window, text="Son Equiespaciados: {}".format(equiespaciados)).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Label(self.solucion_window, text="Grado: {}".format(self.polinomio.order)).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        if(self.mostrarPasos):
            scrollbar = Scrollbar(self.solucion_window)
            scrollbar.pack( side = RIGHT, fill = Y )
            listaDePasos = Listbox(self.solucion_window, yscrollcommand = scrollbar.set )
            for i in range(len(self.pasosDelMetodo)):
               listaDePasos.insert(END,self.pasosDelMetodo[i])
            listaDePasos.pack( side = RIGHT, fill = BOTH, padx=5, pady=5 )
            scrollbar.config( command = listaDePasos.yview )
            #ttk.Label(self.solucion_window, text=self.pasos).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        self.solucion = ttk.Label(self.solucion_window, text="Resultado Final: \n{}".format(str(self.polinomio)))
        self.solucion.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.valorK = ttk.Entry(self.solucion_window, validate='key', validatecommand=(validateDigit, '%P'))
        ttk.Label(self.solucion_window, text="Especializar Polinomio en: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.valorK.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.solucion_window, text='Especializar', command=self.especializarPolinomio).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.especializacion = ttk.Label(self.solucion_window, text="Resultado: ")
        self.especializacion.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        ttk.Button(self.solucion_window, text='Ingresar Punto', command=self.abrirVentanaIngreso).pack(side=TOP, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.solucion_window, text='Remover Punto', command=self.abrirVentanaRemover).pack(side=TOP, fill=BOTH, padx=5, pady=5)

        ttk.Button(self.solucion_window, text='Salir', command=self.solucion_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def formatearPuntos(self):
        puntosTxt = ""

        for i in range(len(self.puntosEnX)):
            if i == 0:
                puntosTxt = "({0}; {1})".format(str(self.puntosEnX[i]), str(self.puntosEnY[i]))
            else:
                puntosTxt = puntosTxt + ", ({0}; {1})".format(str(self.puntosEnX[i]), str(self.puntosEnY[i]))

        puntosAMostrarTxt = "Puntos Ingresados: {" + puntosTxt + "}"

        self.puntosLabel["text"] = puntosAMostrarTxt

    def isADigit(self, text):
        try:
            float(text)
        except ValueError:
            return False
        return True

    def realizarMetodo(self, claseMetodo, mostrarPasos):
        self.pasosDelMetodo = []
        if mostrarPasos:
            return claseMetodo.miMetodo(self.agregarPasos)
        else:
            return claseMetodo.miMetodo(self.pase)

    def agregarPasos(self, paso, polinomio):
        #self.pasos += "\nPaso {0}:\n  {1}\n".format(str(paso), str(polinomio))
        self.pasosDelMetodo.append("Paso/diferencia " + str(paso) + ":\n" + str(polinomio) + "\n")

    def pase(self, paso, polinomio):
        pass

    def agregarPunto(self,x,y):
        self.puntosEnX.append(x)
        self.puntosEnY.append(y)
        self.formatearPuntos()
        try:
            polinomioNuevo = self.realizarMetodo(self.metodoClase, self.mostrarPasos)
        except:
            messagebox.showerror("Error", "Hubo un error al realizar el metodo de nuevo")
            return

        self.solucion["text"] = "Resultado Final: \n{}".format(str(polinomioNuevo))
        self.compararPolinomios(self.polinomio, polinomioNuevo)
        self.polinomio = polinomioNuevo

    def compararPolinomios(self, unPolinomio, otroPolinomio):
        if str(unPolinomio) == str(otroPolinomio):
            self.solucion["text"] = self.solucion["text"] + ", igual al anterior"



    def removerPunto(self, puntoARemover):
        self.puntosEnX.remove(puntoARemover[0])
        self.puntosEnY.remove(puntoARemover[1])
        self.formatearPuntos()
        try:
            polinomioNuevo = self.realizarMetodo(self.metodoClase, self.mostrarPasos)
        except:
            messagebox.showerror("Error", "hubo un error al realizar el metodo de nuevo")
            return
        self.solucion["text"] = "Resultado Final: \n{}".format(str(polinomioNuevo))
        self.compararPolinomios(self.polinomio, polinomioNuevo)
        self.polinomio = polinomioNuevo

    def abrirVentanaIngreso(self):
        PantallaIngreso(self, self.solucion_window)
    
    def abrirVentanaRemover(self):
        PantallaRemover(self, self.solucion_window, self.puntosEnX, self.puntosEnY)

    def especializarPolinomio(self):
        self.especializacion["text"] = "Resultado: " + str(especializar(self.polinomio, int(self.valorK.get())))

