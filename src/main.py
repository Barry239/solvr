from tkinter import Tk

from app import MainApp

def main():
    ## Inicializar ventana
    root = Tk()
    root.title('Calculadora')
    root.geometry('500x350')

    ## Crear app
    MainApp(root).pack(side='top', fill='both', expand=True)

    ## Mostrar ventana
    root.mainloop()

if __name__ == '__main__':
    main()
