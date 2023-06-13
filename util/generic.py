from PIL import ImageTk, Image

def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

def centrar_ventanas(ventana, aplicacion_ancho, aplicacion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenwidth()
    x = int((pantalla_ancho/2)- (aplicacion_ancho/2))
    y = int((pantalla_largo/2)- (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")