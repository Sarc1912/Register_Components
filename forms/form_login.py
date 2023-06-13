import tkinter as tk
from tkinter import *
from tkinter import BOTH, ttk,messagebox
from tkinter import font
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import Masterpanel

class App:
    
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        
        if (usu == "admin" and password == "admin"):
            self.ventana.destroy()
            Masterpanel()
        else:
            messagebox.showerror(message="El usuario o la contraseña no es correcta", title="Usuario desconocido o contraseña incorrecta")
    
    def __init__(self):
                
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesion")
        self.ventana.geometry("900x500")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0,height=0)
        self.ventana.iconbitmap(".\\imagenes\\star.ico")

        
        logo = utl.leer_imagen(".\\imagenes\\banco-bicentenario.jpeg", (250,400))
        
        #frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#dcdcdc")
        frame_logo.pack(side="left", expand=tk.NO, fill=BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#dcdcdc")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        #frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50,bd=0,relief=tk.SOLID, bg="black")
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="*Inicio de Sesion*\n*Registro BBDP*", font=("arial black",30), fg="black", bg="#fcfcfc",pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top
        
        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        #Label_usuarios
        label_usuario = tk.Label(frame_form_fill, text="Usuario", font=("Comic Sans MS",14),fg="black",bg="#fcfcfc", anchor="w")
        label_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=("Times",14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)
        #Label_pass
        label_password = tk.Label(frame_form_fill, text="Password", font=("Comic Sans MS",14),fg="black",bg="#fcfcfc", anchor="w")
        label_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=("Times",14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")
        
        button = tk.Button(frame_form_fill, text="Iniciar Sesion", font=("Comic Sans MS",15,BOLD),bg="#e83e37", bd=0, fg="#fff", command=self.verificar)
        button.pack(fill=tk.X, padx=20, pady=20)
        button.bind("<Return>",(lambda event: self.verificar()))
        
        self.ventana.mainloop()
