from numpy.polynomial import Polynomial
import tkinter as tk
from tkinter import messagebox

class MainApp(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        ## Configurar columnas
        self.grid_columnconfigure((0, 7), weight=1)
        
        ## Crear diseño
        self.title = tk.Label(self, text='Calculadora', font=('Lucida Calligraphy', 16, 'bold'))
        self.title.grid(row=0, column=1, columnspan=6, pady=(18, 14))
        self.subtitle = tk.Label(self, text='Ingrese la ecuación homogénea:', font=('Comic Sans MS', 11))
        self.subtitle.grid(row=1, column=1, columnspan=6, pady=(2, 12), sticky='W')

        self.aEntry = tk.Entry(self, font=('Lucida Sans Typewriter', 10), width=8)
        self.aEntry.grid(row=2, column=1, padx=(0, 2))
        self.aLabel = tk.Label(self, text='y\'\' + ', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.aLabel.grid(row=2, column=2, padx=(2, 0))

        self.bEntry = tk.Entry(self, font=('Lucida Sans Typewriter', 10), width=8)
        self.bEntry.grid(row=2, column=3, padx=(0, 2))
        self.bLabel = tk.Label(self, text='y\' + ', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.bLabel.grid(row=2, column=4, padx=(2, 0))

        self.cEntry = tk.Entry(self, font=('Lucida Sans Typewriter', 10), width=8)
        self.cEntry.grid(row=2, column=5, padx=(0, 2))
        self.cLabel = tk.Label(self, text='y = 0', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.cLabel.grid(row=2, column=6, padx=(2, 0))

        self.resultButton = tk.Button(self, text='Resolver', font=('Comic Sans MS', 10), fg='#fff', bg='#198754', command=self.solve)
        self.resultButton.grid(row=3, column=1, columnspan=6, pady=(16, 5), sticky='WE')
        self.stepsButton = tk.Button(self, text='Mostrar pasos', font=('Comic Sans MS', 10), fg='#fff', bg='#0d6efd', command=self.step)
        self.stepsButton.grid(row=4, column=1, columnspan=6, pady=(5, 5), sticky='WE')
        self.theoryButton = tk.Button(self, text='Teoría', font=('Comic Sans MS', 10), fg='#fff', bg='#6610f2', command=self.theory)
        self.theoryButton.grid(row=5, column=1, columnspan=6, pady=(5, 0), sticky='WE')

        ## Enfocar en la primera entrada
        self.aEntry.focus()

    def solve(self) -> None:
        ## Obtener valores
        a = self.aEntry.get()
        b = self.bEntry.get()
        c = self.cEntry.get()

        ## Convertir en float
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            messagebox.showerror('Error', 'Algo salió mal, inténtalo de nuevo')
            return

        ## Calcular raices
        r1, r2 = Polynomial([c, b, a]).roots()

        ## Inicializar nueva ventana
        window = tk.Toplevel(self.master)
        window.title('Resultado')
        window.geometry('500x150')

        ## Crear ventana de resultado
        rs = ResultFrame(window)
        rs.pack(side='top', fill='both', expand=True)

        ## Poner resultado
        rs.setdata(r1, r2)

    def step(self) -> None:
        ## Obtener valores
        a = self.aEntry.get()
        b = self.bEntry.get()
        c = self.cEntry.get()

        ## Convertir en float
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            messagebox.showerror('Error', 'Algo salió mal, inténtalo de nuevo')
            return

        ## Calcular raices
        r1, r2 = Polynomial([c, b, a]).roots()

        ## Inicializar nueva ventana
        window = tk.Toplevel(self.master)
        window.title('Pasos')
        window.geometry('500x350')

        ## Crear ventana de pasos
        rs = StepsFrame(window)
        rs.pack(side='top', fill='both', expand=True)

        ## Poner pasos
        rs.setdata(a, b, c, r1, r2)

    def theory(self):
        ## Inicializar nueva ventana
        window = tk.Toplevel(self.master)
        window.title('Teoría')
        window.geometry('600x450')

        ## Crear ventana de pasos
        rs = TheoryFrame(window)
        rs.pack(side='top', fill='both', expand=True)

class ResultFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        ## Configurar columnas
        self.grid_columnconfigure((0, 2), weight=1)
        
        ## Crear diseño
        self.subtitle = tk.Label(self, text='Resultado:', font=('Comic Sans MS', 11))
        self.subtitle.grid(row=0, column=1, pady=(18, 12), sticky='W')

        self.resultLabel = tk.Label(self, font=('Lucida Sans Typewriter', 10, 'italic'))
        self.resultLabel.grid(row=1, column=1)

        self.okButton = tk.Button(self, text='Aceptar', font=('Comic Sans MS', 10), fg='#fff', bg='#0d6efd', command=self.close)
        self.okButton.grid(row=2, column=1, pady=(16, 5), sticky='WE')

        ## Enfocar botón
        self.okButton.focus()

    def setdata(self, r1, r2) -> None:
        self.resultLabel.config(text='y = c\u2081 e^({:.2f}x) + c\u2082 e^({:.2f}x)'.format(r1, r2))

    def close(self) -> None:
        ## Cerrar master
        self.master.destroy()

class StepsFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        ## Configurar columnas
        self.grid_columnconfigure((0, 2), weight=1)
        
        ## Crear diseño
        self.subtitle = tk.Label(self, text='Solución paso a paso:', font=('Comic Sans MS', 11))
        self.subtitle.grid(row=0, column=1, pady=(18, 12), sticky='W')

        self.b1 = tk.Label(self, text='Ecuación diferencial:', font=('Levenim MT', 10), fg='#fd7e14')
        self.b1.grid(row=1, column=1, pady=(2, 0), sticky='W')
        self.s1 = tk.Label(self, font=('Lucida Sans Typewriter', 10, 'italic'))
        self.s1.grid(row=2, column=1)

        self.b2 = tk.Label(self, text='Ecuación característica:', font=('Levenim MT', 10), fg='#fd7e14')
        self.b2.grid(row=3, column=1, pady=(2, 0), sticky='W')
        self.s2 = tk.Label(self, font=('Lucida Sans Typewriter', 10, 'italic'))
        self.s2.grid(row=4, column=1)
        self.s3 = tk.Label(self, font=('Lucida Sans Typewriter', 10, 'italic'))
        self.s3.grid(row=5, column=1)
        self.s4 = tk.Label(self, font=('Lucida Sans Typewriter', 10, 'italic'))
        self.s4.grid(row=6, column=1)

        self.b3 = tk.Label(self, text='Solución general:', font=('Levenim MT', 10), fg='#fd7e14')
        self.b3.grid(row=7, column=1, pady=(2, 0), sticky='W')
        self.s5 = tk.Label(self, font=('Lucida Sans Typewriter', 10, 'italic'))
        self.s5.grid(row=8, column=1)
        self.resultLabel = tk.Label(self, font=('Lucida Sans Typewriter', 10, 'italic'))
        self.resultLabel.grid(row=9, column=1)

        self.okButton = tk.Button(self, text='Aceptar', font=('Comic Sans MS', 10), fg='#fff', bg='#0d6efd', command=self.close)
        self.okButton.grid(row=10, column=1, pady=(16, 5), sticky='WE')

        ## Enfocar botón
        self.okButton.focus()

    def setdata(self, a, b, c, r1, r2) -> None:
        self.s1.config(text='({})y\'\' + ({})y\' + ({})y = 0'.format(a, b, c))

        self.s2.config(text='({})r\u00b2 + ({})r + ({}) = 0'.format(a, b, c))
        self.s3.config(text='[r + ({:.2f})] [r + ({:.2f})]] = 0'.format(-r1, -r2))
        self.s4.config(text='r\u2081 = {:.2f}, r\u2082 = {:.2f}'.format(r1, r2))

        self.s5.config(text='y\u2081 = e^({:.2f}x), y\u2082 = e^({:.2f}x)'.format(r1, r2))
        self.resultLabel.config(text='y = c\u2081 e^({:.2f}x) + c\u2082 e^({:.2f}x)'.format(r1, r2))

    def close(self) -> None:
        ## Cerrar master
        self.master.destroy()

class TheoryFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        ## Configurar columnas
        self.grid_columnconfigure((0, 2), weight=1)
        
        ## Crear diseño
        self.subtitle = tk.Label(self, text='Teoría:', font=('Comic Sans MS', 11))
        self.subtitle.grid(row=0, column=1, pady=(18, 12), sticky='W')

        self.p1 = tk.Label(self, text='Para resolver una ecuación diferencial homogénea de segundo orden de la forma', font=('Levenim MT', 10))
        self.p1.grid(row=1, column=1, pady=(2, 0), sticky='W')
        self.p2 = tk.Label(self, text='ay\'\' + by\' + y = 0', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.p2.grid(row=2, column=1)
        self.p3 = tk.Label(self, text='es necesario identificar la ecuación característica, teniendo a', font=('Levenim MT', 10))
        self.p3.grid(row=3, column=1, sticky='W')
        self.p4 = tk.Label(self, text='y = e^(rx).', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.p4.grid(row=4, column=1)

        self.p5 = tk.Label(self, text='Al sustituir en la ecuación, tenemos', font=('Levenim MT', 10))
        self.p5.grid(row=5, column=1, pady=(10, 0), sticky='W')
        self.p6 = tk.Label(self, text='a[r\u00b2e^(rx)] + b[re^(rx)] + ce^[rx] = 0', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.p6.grid(row=6, column=1)

        self.p7 = tk.Label(self, text='Simplificando y razionalizando la ecuación, tenemos', font=('Levenim MT', 10))
        self.p7.grid(row=7, column=1, pady=(10, 0), sticky='W')
        self.p8 = tk.Label(self, text='(r + m)(r + n) = 0', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.p8.grid(row=8, column=1)
        self.p9 = tk.Label(self, text='por lo tanto', font=('Levenim MT', 10))
        self.p9.grid(row=9, column=1, sticky='W')
        self.p10 = tk.Label(self, text='r\u2081 = -m, r\u2082 = -n', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.p10.grid(row=10, column=1)

        self.p11 = tk.Label(self, text='Por último, creamos una solución general para la ecuación diferenciañ', font=('Levenim MT', 10))
        self.p11.grid(row=11, column=1, pady=(10, 0), sticky='W')
        self.p12 = tk.Label(self, text='y = c\u2081 e^(-mx) + c\u2082 e^(-nx)', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.p12.grid(row=12, column=1)

        self.okButton = tk.Button(self, text='Aceptar', font=('Comic Sans MS', 10), fg='#fff', bg='#0d6efd', command=self.close)
        self.okButton.grid(row=13, column=1, pady=(16, 5), sticky='WE')

        ## Enfocar botón
        self.okButton.focus()

    def close(self) -> None:
        ## Cerrar master
        self.master.destroy()
