from tkinter import *
from tkinter import messagebox as mb
from Automata import Automata
from tkinter import filedialog
import time
import os

autom = Automata()

ventana2 = Tk()
ventana2.title("COMPILADOR LEXICO EPICO")
ventana2.geometry("800x600")
EtiquetaArchivo = Label(text="ARCHIVO", font=("Consolas 16"))
EtiquetaAyuda = Label(text="AYUDA", font=("Consolas 16"))
EtiquetaCarga = Label(text="Archivo Cargado con Exito!", font=("Consolas 14"), fg="green")
EtiquetaTemasAyuda = Label(text="Jonathan Josue Alvarez Chacon", font=("Consolas 14"))
EtiquetaTemasAyuda2 = Label(text="Facultad de Ingenieria, USAC", font=("Consolas 14"))
EtiquetaGuardar = Label(text="Documento Guardado!", font=("Consolas 14"), fg="green")
Caja = Text(ventana2,width=50,height=20, bd=4, selectbackground="red")

def Abrir():
    print("ABIERTO...")
    global filename
    filename=filedialog.askopenfilename(filetype="/", title="Select a file", filetypes=(("Text files","*.txt"),("json files", "*.json"),("all files","*.*")))
    if filename != " ":
        archivo = open(filename, "r")
        Codificado = archivo.read()
        archivo.close() 
        print(Codificado)
            #print(Codificado)
        Caja.insert(INSERT, Codificado)

        r = mb.askokcancel("Mensjae", "Archivo abierto exitosamente")

def Analizar():
    #entrada = Caja.get("1.0","end")
    #print(entrada)
    entrada = open(filename, "r").read()
    resultado = autom.analizar(entrada)
    #print(entrada)
    #autom.imprimir_tokens()
    autom.imprimir_lexemas()
    print("------------------------------")
    autom.detectar_operacion()

def Salir():
    quit()    

def GuardarComo():
    print("Guardado como...")
    entrada = Caja.get("1.0","end")
    NewFile = filedialog.asksaveasfilename(filetype="/", title="Save as", filetypes=(("Text files","*.txt"),("json files", "*.json"),("all files","*.*")))
    NewFile = open("C:/Users/jonat/OneDrive/Escritorio/testeo.txt", "w")
    NewFile.write(entrada + os.linesep)
    NewFile.close()

def TemasAyuda():
    EtiquetaTemasAyuda.grid(row=1, column=0)
    EtiquetaTemasAyuda2.grid(row=2, column=0)

def ManualTecnico():
    path = "Manual_Tecnico.pdf"
    os.system(path)

def ManualUsuario():
    path2 = "Manual_De_Usuario.pdf"
    os.system(path2)

def Guardar():
    print("GUARDADO...")
    entrada = Caja.get("1.0","end")
    archivo2 = open(filename, "w")
    archivo2.write(entrada)
    archivo2.close()
    r = mb.askokcancel("Mensaje", "Archivo guardardado exitosamente")
    #EtiquetaGuardar.grid(row=3, column=0)


#DECLARANDO LOS BOTONES-------------------------------------------------------
botonGuardar = Button(ventana2, text="Guardar", width=20, height=2, bg="lightgreen", command=Guardar)
botonAbrir = Button(ventana2, text="Abrir", width=20, height=2, bg="purple", foreground="white", command=Abrir)
botonGuardarComo = Button(ventana2, text="Guardar Como", width=20, height=2, bg="lightgreen", command=GuardarComo)
botonAnalizar = Button(ventana2, text="Analizar", width=20, height=5, bg="lightblue", command=Analizar)
botonErrores = Button(ventana2, text="Errores", width=20, height=2, bg="Red", foreground="white")
botonSalir = Button(ventana2, text="Salir", width=20, height=2, bg="Orange", command=Salir)
botonManualU = Button(ventana2, text="Manual de Usuario", width=20, height=2,bg="darkgray", command=ManualUsuario)
botonManualT = Button(ventana2, text="Manual Tecnico", width=20, height=2,bg="darkgray", command=ManualTecnico)
botonTemas = Button(ventana2, text="Temas de Ayuda", width=20, height=2,bg="darkgray", command=TemasAyuda)
#CajadeTexto = Entry(ventana2, font=("Consolas", 20), width=55, selectforeground="white", selectbackground="red")

#COLOCANDO LOS BOTONES EN LA VENTANA--------------------------------------
#EtiquetaAyuda.grid(row=2, column=0)
botonAbrir.grid(row=1, column=1, padx=10, pady=10)
botonGuardar.grid(row=2, column=1, padx=10, pady=10)
botonGuardarComo.grid(row=3, column=1, padx=10, pady=10)
botonAnalizar.grid(row=0, column=1, padx=10, pady=10)
botonErrores.grid(row=4, column=1, padx=10, pady=10)
botonSalir.grid(row=4, column=2, padx=10, pady=10)
botonManualU.grid(row=1, column=2, padx=10, pady=10)
botonManualT.grid(row=2, column=2, padx=10, pady=10)
botonTemas.grid(row=3, column=2, padx=10, pady=10)
#CajadeTexto.grid(row=1, column=3, padx=10, pady=10)
Caja.grid(row=0, column=0, padx=10, pady=10)

ventana2.mainloop()

#RE COLOCAR TODOS LOS BOTONES Y LAS WEAS PARA QUE SE MIRE CHIDO