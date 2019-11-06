from tkinter import *
from tkinter import ttk

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
		self.ingreso_window.geometry('500x500')
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
			return False
		return True

	def cerrarVentana(self):
		self.instanciaDeMetodo.agregarPunto(self.xAxisEntry,self.yAxisEntry)
		self.ingreso_window.destroy()