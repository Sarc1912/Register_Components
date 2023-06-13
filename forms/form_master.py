from cgitb import text
from pickle import GLOBAL
import tkinter as tk
from tkinter import CENTER, PhotoImage, ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import psycopg2

#import util.generic as utl

class Masterpanel:
    def __init__(self):
        #CONSTANTES
        TITLE = "Registro BBDP"
        BACKGROUND = "white"
        FONTCOLOR = "black"
        GEOMETRY = "800x700"
        #Creacion y Configuracion de la Ventana
        self._ventana = tk.Tk()
        self._ventana.iconbitmap(".\\imagenes\\star.ico")
        self._ventana.title(TITLE)
        self._ventana.resizable(True,True)
        self._ventana.geometry(GEOMETRY)
        
        photo = PhotoImage(file =".\\imagenes\\busqueda.png") 
        photoimage = photo.subsample(25, 25)
        
        photo1 = PhotoImage(file =".\\imagenes\\actualizar.png") 
        photoimage1 = photo1.subsample(25, 25)
        
        photo2 = PhotoImage(file =".\\imagenes\\star.png") 
        photoimage2 = photo2.subsample(3, 3)
        
        #Titulo y encabezado
        self._title = tk.Label(self._ventana, text=TITLE, font=("arial black", 20), bg=BACKGROUND, fg=FONTCOLOR,pady=15)
        self._title.pack(side=tk.TOP, fill="x")
        
        self._star = tk.Button(self._title,image = photoimage2, bg="white")
        self._star.pack(side=tk.LEFT, fill="x",pady=15)
        
        self._buttonAct = tk.Button(self._title,image = photoimage1, command=self.insertarDatos)
        self._buttonAct.pack(side=tk.RIGHT, fill="x",pady=15)
        
        self._buttonBus = tk.Button(self._title,image = photoimage, command=self.buscar)
        self._buttonBus.pack(side=tk.RIGHT, fill="x",pady=15)

        self._buscar = ttk.Entry(self._title, font=("Times",14))
        self._buscar.pack(side=tk.RIGHT, fill="x")

        
        #Creacion de la Tabla
        self._table = ttk.Treeview(height=40 ,columns=("username", "machinename","ip","disksize","processor","cores","ram","os", "architecture",),show="headings")
        
        vsb = tk.Scrollbar(self._ventana, orient="vertical", command=self._table.yview)
        vsb.pack(side='right', fill='y')
        hsb = tk.Scrollbar(self._ventana, orient="horizontal", command=self._table.xview)
        hsb.pack(side='bottom', fill='x')

        self._table.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._table.pack(side="left")
        self._table.pack(side=tk.TOP, fill="x")

        
        #Insertar Titulos de la Tabla
        self._table.heading("username", text="Usuario", anchor=CENTER)
        self._table.heading("machinename", text="Nombre de Maquina", anchor=CENTER)
        self._table.heading("ip", text="Direccion IP", anchor=CENTER)
        self._table.heading("disksize", text="Disco", anchor=CENTER)
        self._table.heading("processor", text="Procesador", anchor=CENTER)
        self._table.heading("cores", text="Nro. de Nucleos", anchor=CENTER)
        self._table.heading("ram", text="Memoria Ram", anchor=CENTER)
        self._table.heading("os", text="S.O", anchor=CENTER)
        self._table.heading("architecture", text="Arquitectura", anchor=CENTER)
        self.insertarDatos()
        
        self._ventana.mainloop()

    def insertarDatos(self):
        records = self._table.get_children()
        for element in records:
            self._table.delete(element)
        try:
            CONEXION = psycopg2.connect(database="postgres",user ="postgres",password="admin",host="localhost",port="5432")
            with CONEXION.cursor() as cursor:
                consulta = "SELECT * FROM componentes"
                cursor.execute(consulta)
                db_rows = cursor.fetchall()
                for row in db_rows:
                    self._table.insert("","end",text=row,values=row)
        except Exception as e:
            print(e)
        finally:
            CONEXION.close()
        
    def buscar(self):
        try:
            CONEXION = psycopg2.connect(database="postgres",user ="postgres",password="admin",host="localhost",port="5432")
            with CONEXION.cursor() as cursor:
                buscar = self._buscar.get()
                query = (buscar,buscar,buscar)
                consulta = "SELECT * FROM componentes WHERE ip = %s OR username = %s OR machinename = %s"
                cursor.execute(consulta, query)
                resultado = cursor.fetchall()
                
                self._ventanaNueva = tk.Tk()
                self._ventanaNueva.title("Busqueda Avanzada")
                self._ventanaNueva.resizable(False,True)
                self._ventanaNueva.geometry("800x200")
                self._ventanaNueva.iconbitmap(".\\imagenes\\star.ico")

                
                for datos in resultado:
                        self._lista = tk.Label(self._ventanaNueva, text=datos, bg="white")
                        self._lista.pack(side=tk.TOP, fill="x")

                
        except Exception as e:
            print(e)
        finally:
            CONEXION.close()


if __name__ =="__main__":
    Masterpanel()






