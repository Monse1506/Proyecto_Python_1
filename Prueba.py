from tkinter import *
import random

# Crear la ventana
ventana = Tk()

# Crear el canvas
canvas = Canvas(ventana, width=600, height=400, bg="black")
canvas.pack()

# Cargar las imágenes
imagenes = []
def cargar_imagenes(i=0):
    if i < 3:
        imagen = PhotoImage(file="nave.png")
        imagenes.append(imagen)
        cargar_imagenes(i+1)
cargar_imagenes()

# Crear las imágenes en el canvas
objetos_imagenes = []
def crear_imagenes(i=0):
    if i < 10:
        x = random.randint(50, 550)
        y = random.randint(50, 350)
        imagen_objeto = canvas.create_image(x, y, image=random.choice(imagenes))
        objetos_imagenes.append(imagen_objeto)
        crear_imagenes(i+1)
crear_imagenes()

# Función para mover una imagen
def mover_imagen(canvas, imagen_objeto):
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    canvas.move(imagen_objeto, dx, dy)

# Función para mover varias imágenes
def mover_varias_imagenes(canvas, objetos_imagenes, i=0):
    if i < len(objetos_imagenes):
        mover_imagen(canvas, objetos_imagenes[i])
        mover_varias_imagenes(canvas, objetos_imagenes, i+1)

# Función para animar las imágenes
def animar():
    mover_varias_imagenes(canvas, objetos_imagenes)
    ventana.after(50, animar)

# Iniciar la animación
animar()

ventana.mainloop()

