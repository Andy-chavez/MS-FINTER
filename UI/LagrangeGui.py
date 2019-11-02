from tkinter import *
from tkinter import ttk

class LagrangeGui:
    def __init__(self, l_window):
        self.lagrange_window = l_window

        validateDigit = self.lagrange_window.register(self.isADigit)

        self.xAxisEntry = ttk.Entry(self.lagrange_window, validate='key', validatecommand=(validateDigit, '%P'))
        self.yAxisEntry = ttk.Entry(self.lagrange_window, validate='key', validatecommand=(validateDigit, '%P'))

        ttk.Label(self.lagrange_window, text="xAxis: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.xAxisEntry.pack(side=TOP, fill=BOTH)

        ttk.Label(self.lagrange_window, text="yAxis: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.yAxisEntry.pack(side=TOP, fill=BOTH)

        ttk.Button(self.lagrange_window, text='Salir', command=self.lagrange_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.lagrange_window, text='Realizar').pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def isADigit(self, text):
        try:
            float(text)
        except ValueError:
            return False
        return True