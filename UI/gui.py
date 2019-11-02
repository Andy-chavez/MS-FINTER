from tkinter import *
from tkinter import ttk

class Gui:
    lagrange_window = NotImplemented
    newton_window = NotImplemented
    window = Tk()

    xAxisEntry = NotImplemented
    yAxisEntry = NotImplemented

    def initialize(self):
        self.configure_window()
        self.configure_lagrange_widgets()
        self.lagrange_window.mainloop()

    def configure_window(self):
        self.window.geometry('500x500')
        self.window.title("FINTER")
        tab_control = ttk.Notebook(self.window)
        self.lagrange_window = ttk.Frame(tab_control)
        self.newton_window = ttk.Frame(tab_control)
        tab_control.add(self.lagrange_window, text='Metodo Lagrange')
        tab_control.add(self.newton_window, text='Metodo Newton-Gregory')
        tab_control.pack(expand=True, fill=BOTH)

    def configure_lagrange_widgets(self):
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



def main():
    Gui().initialize()

if __name__ == "__main__":
    main()