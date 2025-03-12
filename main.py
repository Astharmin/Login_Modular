import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('Nombre de la imagen . extencion de la imagen')
        self.resizable(0,0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()

    def _crear_componentes(self):
        usuario_etiqueta = ttk.Label(self, text='Username:')
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1,sticky=tk.W, padx=5, pady=5)

        pas_etiqueta = ttk.Label(self, text='Password:')
        pas_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.pas_entrada = ttk.Entry(self, show='*')
        self.pas_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column= 0, columnspan=2)

    def _login(self):
        messagebox.showinfo('Datos Login',
    f'Usuario: {self.usuario_entrada.get()}\nPassword: {self.pas_entrada.get()}')

if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()