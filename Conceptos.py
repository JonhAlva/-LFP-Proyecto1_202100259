import tkinter

ventana = tkinter.Tk()
ventana.geometry("700x500")
nombre = "pepe"
edad = "22"
#Estas vainas sirven para poner texto en la ventana
#Etiqueta = tkinter.Label(ventana, text = "Que pedo")
#Etiqueta.pack(side= tkinter.BOTTOM)

#Definimos una funcion com objeto que es lo que pasara al presionar el boton
def saludo():
    print("hola")

#Aqui se crea el boton y se coloca en la ventana
#Con el subcomando "command=" se coloca la funcion que en este caso "saludo" y el boton ejecutara
#lo que este dentro de la funcion saludo, solo imprimira un hola
botonAbrir = tkinter.Button(ventana, text = "Abrir", padx=40, pady=20, command=saludo)
botonAbrir.pack()

#Asi es la forma en que podremos meter variables a los botones
#Es indispensable el uso de lambda para este caso... Dentro del parentesis de la funcion se meten las variables
#que se quieran usar para cuando se presione el boton
#y luego se coloca la funcion dentro del command, junto con las variables que se quieran
#AL PARECER SOLO ACEPTA VARIABLES DE INDOLE STRING, ES DECIR SOLO TEXTO
def parametros(nombre, edad):
    print("Hola" + nombre + edad)

botonParametro = tkinter.Button(ventana, text="parametro", padx=40, pady=20, command=lambda: parametros(nombre, edad))
botonParametro.pack()


#Asi es como se coloca la vaina de texto
cajatexto = tkinter.Entry(ventana, font="Helvetica 14")
cajatexto.pack()

#FUNCION QUE LEERA LO QUE SE ESCRIBA EN LA CAJA DE TEXTO
def TextoDeLaCaja():
    #Con este comando obtendremos el texto de la caja
    textobtenido = cajatexto.get()
    #Aqui irian las acciones que se quieran hacer, pero por ahora solo las imprime
    print(textobtenido)

botonCompilar = tkinter.Button(ventana, command=TextoDeLaCaja, text="Compilar")

ventana.mainloop()