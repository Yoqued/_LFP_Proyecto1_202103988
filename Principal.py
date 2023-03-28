import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Analizador_Lexico import *
from Instrucciones.aritmeticas import *
import os

global Nombre_Archivo
Nombre_Archivo = ''

Ventana_Inicial = Tk()
Ventana_Inicial.title("Proyecto 1")
Ventana_Inicial.protocol("WM_DELETE_WINDOW", lambda: None)
Ventana_Inicial.resizable(0,0)
Ventana_Inicial.geometry("500x700+700+150")
Label(Ventana_Inicial, text='Area de "EDITAR" o "CREAR" texto', font=("Arial",12)).place(x ="30", y ="15")
Caja_Grande = Text(Ventana_Inicial, width="40", height="28", font = ("Arial",14))
Caja_Grande.place(x = "30", y = "42")

def Abrir_Archivo():
    try:
        global Nombre_Archivo
        Nombre_Archivo = filedialog.askopenfilename(title='Seleccióne el "DOCUMENTO"')
        with open(Nombre_Archivo, 'r', encoding = "UTF-8") as fichero:
            linea = fichero.readline()
            while linea != '':
                Caja_Grande.insert(tk.END, linea)
                linea = fichero.readline()
    except:
        messagebox.showinfo("Mesanje", 'Hubo problemas al cargar el "ARCHIVO"')     

def Guardar_Archivo():
    if Nombre_Archivo != '':
        Archivo_Guardar = open(Nombre_Archivo, 'w', encoding = "UTF-8")
        Archivo_Guardar.write(Caja_Grande.get("1.0",'end-1c'))
        Archivo_Guardar.close()
        Caja_Grande.delete("1.0","end")
        messagebox.showinfo("Mesanje", '"ARCHIVO GUARDADO"')
    else:
        messagebox.showinfo("Mesanje", 'Se tiene que abrir antes un "ARCHIVO"')

def Guardar_Como():
    e = StringVar()
    Ventana_Inicial.withdraw()
    Ventana_Nombre_Arch = Toplevel()
    Ventana_Nombre_Arch.title('Escriba nombre del "Archivo"')
    Ventana_Nombre_Arch.geometry("410x150+700+250")
    Ventana_Nombre_Arch.protocol("WM_DELETE_WINDOW", lambda: None)
    Ventana_Nombre_Arch.resizable(0,0)
    Label(Ventana_Nombre_Arch, text = "Nombre:", font=("Arial",14)).place(x = "30", y = "42")
    Caja1 = Entry(Ventana_Nombre_Arch, font = ("Arial",14), textvariable = e)
    Caja1.place(x = "120", y = "42")

    def Guardar_Nombre():
        Archivo_Guardar = open(str(e.get())+'.lfp', 'w', encoding = "UTF-8")
        Archivo_Guardar.write(Caja_Grande.get("1.0",'end-1c'))
        Archivo_Guardar.close()
        e.set('')
        Caja_Grande.delete("1.0","end")
        messagebox.showinfo("Mesanje", '"ARCHIVO GUARDADO"')

    def Regresar1():
        Ventana_Nombre_Arch.withdraw()
        Ventana_Inicial.deiconify()
        Caja_Grande.delete("1.0","end")
        e.set('')

    Button(Ventana_Nombre_Arch, text = "Guardar", font=("Arial",12), command = Guardar_Nombre).place(x = "95", y = "80")
    Button(Ventana_Nombre_Arch, text = "Regresar", font=("Arial",12), command = Regresar1).place(x = "270", y = "80")

def Analizar():
    #try:
        Nombre_Archivo1 = filedialog.askopenfilename(title='Seleccióne el archivo a "ANALIZAR"')
        Contenido_Archivo1 = open(Nombre_Archivo1, 'r+', encoding = "UTF-8")
        lectura = Contenido_Archivo1.read()
        Contenido_Archivo1.close()
        llenarlistaNodos()
        Instruccion(lectura)
        b,c,d = operar_()
        Graficar(d)
        getErrores(None)

    #except:
        #messagebox.showinfo("Mesanje", 'Hubo problemas al cargar el "ARCHIVO"')

def Errores():
    path = 'Errores.txt'
    os.system(path)

def info():
    messagebox.showinfo("Mesanje", 'Nombre del curso: Lab. Lenguajes Formales de programación\nNombre del Estudiante: Raúl David Yoque Sum\nCarné del Estudiante: 202103988')


#Creación de la barra del menú
barra_menus = tk.Menu()
menu_archivo = tk.Menu(Ventana_Inicial, tearoff=False)
menu_ayuda = tk.Menu(Ventana_Inicial, tearoff=False)
#Imagenes y propiedades del menu Archivo
imagen_Abrir = tk.PhotoImage(file="Imagenes/Abrir.png")
zoom1 = imagen_Abrir.subsample(20)
imagen_Guardar = tk.PhotoImage(file="Imagenes/Guardar.png")
zoom2 = imagen_Guardar.subsample(20)
imagen_Guardar_Como = tk.PhotoImage(file="Imagenes/Guardar como.png")
zoom3 = imagen_Guardar_Como.subsample(20)
imagen_Analizar = tk.PhotoImage(file="Imagenes/Analizar.png")
zoom4 = imagen_Analizar.subsample(20)
imagen_Error = tk.PhotoImage(file="Imagenes/Error.png")
zoom5 = imagen_Error.subsample(20)
imagen_Salir = tk.PhotoImage(file="Imagenes/Salir.png")
zoom6 = imagen_Salir.subsample(20)
menu_archivo.add_command(
    label="Abrir",
    command=Abrir_Archivo,
    image=zoom1,
    compound=tk.LEFT
)
menu_archivo.add_command(
    label="Guardar",
    command=Guardar_Archivo,
    image=zoom2,
    compound=tk.LEFT
)
menu_archivo.add_command(
    label="Guardar como",
    command=Guardar_Como,
    image=zoom3,
    compound=tk.LEFT
)
menu_archivo.add_command(
    label="Analizar",
    command=Analizar,
    image=zoom4,
    compound=tk.LEFT
)
menu_archivo.add_command(
    label="Errores",
    command=Errores,
    image=zoom5,
    compound=tk.LEFT
)
menu_archivo.add_command(
    label="Salir",
    command=Ventana_Inicial.destroy,
    image=zoom6,
    compound=tk.LEFT
)
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
Ventana_Inicial.config(menu=barra_menus)
#Imagenes y propiedades del menu Archivo
imagen_Tecnico = tk.PhotoImage(file="Imagenes/Usuario.png")
zoom7 = imagen_Tecnico.subsample(20)
imagen_Usuario = tk.PhotoImage(file="Imagenes/Tecnico.png")
zoom8 = imagen_Usuario.subsample(20)
imagen_Ayuda = tk.PhotoImage(file="Imagenes/Ayuda.png")
zoom9 = imagen_Ayuda.subsample(20)
menu_ayuda.add_command(
    label="Manual de Usuario",
    image=zoom7,
    compound=tk.LEFT
)
menu_ayuda.add_command(
    label="Manual de Tecnico",
    image=zoom8,
    compound=tk.LEFT
)
menu_ayuda.add_command(
    label="Temas de Ayuda",
    command=info,
    image=zoom9,
    compound=tk.LEFT
)
barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")
Ventana_Inicial.config(menu=barra_menus)

Ventana_Inicial.mainloop()