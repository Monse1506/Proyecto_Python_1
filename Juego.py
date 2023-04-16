from tkinter import *
import time
import random
from PIL import ImageTk, Image
from threading import Thread

#CREACION DE VENTANA
root = Tk()
root.geometry('1000x800')
root.resizable(width=False, height=False)
root.title('SPACE IMPACT')

#CREACION DE FRAME
framePrin = Frame(root, bg= "black")
framePrin.pack(side=TOP)
framePrin.configure(width=1000,height=800)

#CREACION DE CANVAS PARA PONER IMAGEN
canvasPrin = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="black")
canvasPrin.place(relx=0.5, rely=0.5, anchor=CENTER)

#IMAGEN DEFAULT DEL CANVAS AKA. FONDO PRINCIPAL DEL MENU
fondoMenu = Image.open("fondoPrincipal.png")
fondoMenuRe = fondoMenu.resize((1000, 800), Image.ANTIALIAS)
fondoMenuReFin = ImageTk.PhotoImage(fondoMenuRe, master = canvasPrin)
canvasPrin.create_image(500,400, image=fondoMenuReFin)
def cambiar():
        canvasSobre = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="white")
        canvasSobre.place(relx=0.5, rely=0.5, anchor=CENTER)
        fondoSobre = Image.open("fondoAcerca.png")
        fondoSobreRe = fondoSobre.resize((1000, 800), Image.ANTIALIAS)
        fondoSobreReFin = ImageTk.PhotoImage(fondoSobreRe, master=canvasSobre)
        canvasSobre.create_image(500,400, image=fondoSobreReFin)
        def regresa():
                canvasSobre.destroy()
        btnRegresa = Button(canvasSobre, text="REGRESA", font=("Britannic Bold", 16) , width= 10,height= 1, fg="black", command=regresa)
        btnRegresa.place(x=850, y=750)
        canvasSobre.lift()

btnA = Button(canvasPrin, text="Acerca de", font=("Britannic Bold", 16) ,fg="white", bg= "#EFCA2E", width= 20,height= 1, anchor="center",command=cambiar)
btnA.place(x=50, y=500)

def juego():
        #CANVAS DEL JUEGO
        canvasJuego = Canvas(framePrin, width=1000, height=750, bg="white")
        canvasJuego.place(relx=0.5, rely=0.53, anchor=CENTER)
        # CANVAS DISPLAY (MUESTRA EL SCORE Y LAS VIDAS)
        top = Canvas(framePrin, width=1000, height=50, bg= "black")
        top.place(relx=0, rely=0)
        #PUNTAJE
        global score
        score = 0
        scoreLabel = Label(top, text="Score: " + str(score), bg = "green", fg= "white", font=(50))
        scoreLabel.place(x=50, y=15)
        #VIDAS
        global lives
        lives=3
        livesLabel = Label(top, text="Vidas Extra: " + str(lives), bg="red", fg="white", font=(50))
        livesLabel.place(x=450, y=15)
        # CREACION NAVE
        ship = Image.open("nave.png")
        shipRe = ship.resize((75, 75), Image.ANTIALIAS)
        shipReFin = ImageTk.PhotoImage(shipRe, master=canvasJuego)
        myship = canvasJuego.create_image(100, 100, image=shipReFin)

        # ALIENS
        #LISTA PARA ALMACENAR TRES TIPOS DE ALIENS
        imagenes = []
        #FUNCION ALMACENA ALIENS EN LA LISTA
        def cargar_imagenes(i=1):
                if i <= 3:
                        alien1 = Image.open(f"alien{i}.jpg")
                        alien1Re = alien1.resize((50, 50), Image.ANTIALIAS)
                        imagen = ImageTk.PhotoImage(alien1Re, master=canvasJuego)
                        imagenes.append(imagen)
                        cargar_imagenes(i + 1)

        cargar_imagenes()

        # CREA IMAGENES EN EL CANVAS Y LAS ALMACENA EN UNA LISTA
        objetos_imagenes = []
        def crear_imagenes(i=0,y=100):
                #DEFINE LA CANTIDAD DE IMAGENES QUE SE CREAN
                if i < 10:
                        x = random.randint(800, 1000)
                        imagen_objeto = canvasJuego.create_image(x, y, image=random.choice(imagenes))
                        objetos_imagenes.append(imagen_objeto)
                        crear_imagenes(i + 1, y + 75)

        crear_imagenes()

        # FUNCION QUE MUEVE LAS IMAGENES
        def mover_imagen(canvas, imagen_objeto):
                #NAVE LLEGA AL BORDE IZQUIERDO
                global lives
                myX = random.randint(-35, 0)
                coordY = random.randint(30, 720)
                canvas.move(imagen_objeto, myX, 0)
                aliencito = imagen_objeto
                alienCoords = canvas.bbox(aliencito)
                if alienCoords[0] < 0:
                        canvasJuego.coords(aliencito, 1000, coordY)
                        lives = lives
                        livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                        if lives < 1:
                                livesLabel.configure(text="Se murio", bg="red", fg="white")
                                GameOver = Canvas(canvas, width=1000, height=750, bg="black")
                                GameOver.place(x=0, y=0)
                #COLISION CON LA NAVE
                shipCoords = canvasJuego.bbox(myship)
                if ((shipCoords[2] > alienCoords[0] > shipCoords[0]) and shipCoords[1] < alienCoords[3]  < shipCoords[3]) :
                        canvasJuego.coords(aliencito, 1000, 300)
                        lives = lives -1
                        livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                        if lives < 1:
                                livesLabel.configure(text="Se murio", bg="red", fg="white")
                                GameOver = Canvas(canvasJuego, width=1000, height=750, bg="black")
                                GameOver.place(x=0, y=0)

        # FUNCION QUE LLAMA A LA FUNCION PARA MOVER UNA IMAGEN PARA QUE RECURSIVAMENTE MUEVA VARIAS IMAGENES
        def mover_varias_imagenes(canvas, objetos_imagenes, i):
                if i < len(objetos_imagenes):
                        # LLamada a funcion mover una imagen
                        mover_imagen(canvas, objetos_imagenes[i])
                        #LLamada recursiva
                        mover_varias_imagenes(canvas, objetos_imagenes, i + 1)

        # FUNCION PARA ANIMAR A LAS IMAGENES
        def animar():
                mover_varias_imagenes(canvasJuego, objetos_imagenes,0)
                #LLAMADA RECURSIVA
                root.after(50, animar)
        animar()


        # MOVIMIENTOS NAVE
        def moverArriba(event):
                shipCoords = canvasJuego.bbox(myship)
                if shipCoords[1] < 0:
                        return canvasJuego.move(myship, 0, 0)
                else:
                        return canvasJuego.move(myship, 0, -10)
        def moverAbajo(event):
                shipCoords = canvasJuego.bbox(myship)
                if shipCoords[3] > 750:
                        return canvasJuego.move(myship, 0, 0)
                else:
                        return canvasJuego.move(myship, 0, 10)
        def moverDerecha(event):
                shipCoords = canvasJuego.bbox(myship)
                if shipCoords[2] > 1000:
                        return canvasJuego.move(myship, 0, 0)
                else:
                        return canvasJuego.move(myship, 10, 0)
        def moverIzquierda(event):
                shipCoords = canvasJuego.bbox(myship)
                if shipCoords[0] < 0:
                        return canvasJuego.move(myship, 0, 0)
                else:
                        return canvasJuego.move(myship, -10, 0)

        #DEFINE LOS CONTROLES DE LA NAVE
        #FLECHAS
        canvasJuego.bind_all("<Up>", moverArriba)
        canvasJuego.bind_all("<Down>", moverAbajo)
        canvasJuego.bind_all("<Right>", moverDerecha)
        canvasJuego.bind_all("<Left>", moverIzquierda)
        #TECLADO
        canvasJuego.bind_all("<w>", moverArriba)
        canvasJuego.bind_all("<s>", moverAbajo)
        canvasJuego.bind_all("<d>", moverDerecha)
        canvasJuego.bind_all("<a>", moverIzquierda)
        # REGRESAR AL MENU DE INICIO
        def regresa():
            canvasJuego.destroy()
            top.destroy()

        btnRegresa = Button(top, text="REGRESA", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=regresa)
        btnRegresa.place(x=850, y=8)
        myship.lift(AboveThis=btnRegresa)


btnA = Button(canvasPrin, text="Juego", font=("Britannic Bold", 16) ,fg="white", bg= "#EFCA2E", width= 20,height= 1, anchor="center",command=juego)
btnA.place(x=400, y=700)
root.mainloop()
