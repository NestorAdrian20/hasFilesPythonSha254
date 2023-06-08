import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import hashlib, easygui
from checksumdir import dirhash


class GeneradorHash(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Generador Hash')
        # Configuración de ventana
        self.geometry('+450+200')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)
        # Creación de componentes
        self._crear_componentes()
        self._crear_menu()

    def _crear_componentes(self):
        # Frame de botones
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
    
        boton_hash_documento = Button(frame_botones, text='Hash Documento: ', command=self._hash_documento)
        boton_hash_directorio = Button(frame_botones, text='Hash Directorio: ', command=self._hash_directorio)

        
        boton_hash_documento.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_hash_directorio.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        frame_botones.grid(row=0, column=0, sticky='ns')

    def _crear_menu(self):
        # Creamos el menú de la app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)

        # Opciones del menú
        # Archivo
        menu_opciones = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label='Opciones', menu=menu_opciones)
        # Opciones de archivo
        menu_opciones.add_command(label='Hash documento;', command=self._hash_documento)
        menu_opciones.add_command(label='Has directorio;', command=self._hash_directorio)
        menu_opciones.add_separator()
        menu_opciones.add_command(label='Salir', command=self.quit)
    
    def _hash_documento(self):
        file = easygui.fileopenbox()
        fp = open(file, "rb")
        buffer = fp.read()
        hashObj = hashlib.sha256()
        hashObj.update(buffer)
        lastHash = hashObj.hexdigest().upper()
        sha256 = lastHash
        fp.close()
                
        etiqueta02 = Label(generador_hash, text="El documento tiene el siguiente valor hash:")  
        etiqueta02.place(x=270, y=130)         
        etiqueta = Label(generador_hash, text=sha256)  
        etiqueta.place(x=200, y=150)  

    def _hash_directorio(self):

        directory  = askdirectory()
        md5hash    = dirhash(directory, 'sha256')

        etiqueta01 = Label(generador_hash, text="El directorio tiene el siguiente valor hash-")  
        etiqueta01.place(x=270, y=270) 
        etiqueta = Label(generador_hash, text=md5hash)  
        etiqueta.place(x=200, y=300) 

if __name__ == '__main__':
    generador_hash = GeneradorHash()
    generador_hash.mainloop()
