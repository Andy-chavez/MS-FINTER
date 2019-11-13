from tkinter import *
from tkinter import ttk
from LagrangeGui import LagrangeGui
from NewtonGui import NewtonGui

class Gui:
    lagrange_window = NotImplemented
    newton_window = NotImplemented
    window = Tk()

    def initialize(self):
        self.configure_window()
        self.configure_lagrange_window()
        self.configure_newton_window()
        self.window.mainloop()

    def configure_window(self):
        self.window.geometry('450x400')
        self.window.title("FINTER")
        tab_control = ttk.Notebook(self.window)
        self.lagrange_window = ttk.Frame(tab_control)
        self.newton_window = ttk.Frame(tab_control)
        tab_control.add(self.lagrange_window, text='Metodo Lagrange')
        tab_control.add(self.newton_window, text='Metodo Newton-Gregory')
        tab_control.pack(expand=True, fill=BOTH)

    def configure_lagrange_window(self):
        LagrangeGui(self.lagrange_window, self.window)
        
    def configure_newton_window(self):
        NewtonGui(self.newton_window, self.window)

def main():
    Gui().initialize()

if __name__ == "__main__":
    main()