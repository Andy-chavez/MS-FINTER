from tkinter import *
from tkinter import ttk

class NewtonGui:
    def __init__(self, n_window):
        self.newton_window = n_window

        validateDigit = self.newton_window.register(self.isADigit)

        self.xAxisEntry = ttk.Entry(self.newton_window, validate='key', validatecommand=(validateDigit, '%P'))
        self.yAxisEntry = ttk.Entry(self.newton_window, validate='key', validatecommand=(validateDigit, '%P'))

        ttk.Label(self.newton_window, text="xAxis: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.xAxisEntry.pack(side=TOP, fill=BOTH)

        ttk.Label(self.newton_window, text="yAxis: ").pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.yAxisEntry.pack(side=TOP, fill=BOTH)

        ttk.Button(self.newton_window, text='Salir', command=self.newton_window.destroy).pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
        ttk.Button(self.newton_window, text='Realizar').pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)

    def isADigit(self, text):
        try:
            float(text)
        except ValueError:
            return False
        return True