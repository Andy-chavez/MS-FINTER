from tkinter import *

class Gui:
    window = Tk()

    def initialize(self):
        self.configure_window()
        self.window.mainloop()

    def configure_window(self):
        self.window.title("FINTER")
        self.window.geometry('500x500')

def main():
    Gui().initialize()

if __name__ == "__main__":
    main()