from tkinter import *
import time
import random
from PIL import ImageTk, Image
import pygame

#CREACION DE VENTANA
root = Tk()
root.geometry('1000x600')
root.resizable(width=False, height=False)
root.title('SPACE IMPACT')

#MUSIQUITA VENTANA INICIAL
pygame.mixer.init()
pygame.mixer_music.load("Fondo.mp3")
pygame.mixer_music.play(-1)

#CREACION DE FRAME
framePrin = Frame(root, bg= "white")
framePrin.pack(side=TOP)
framePrin.configure(width=1000,height=600)

#CREACION DE CANVAS PARA PONER IMAGEN
canvasPrin = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="black")
canvasPrin.place(relx=0.5, rely=0.5, anchor=CENTER)

#IMAGEN DEFAULT DEL CANVAS AKA. FONDO PRINCIPAL DEL MENU
fondoMenu = Image.open("fondoPrincipal.jpg")
fondoMenuRe = fondoMenu.resize((1000, 600), Image.ANTIALIAS)
fondoMenuReFin = ImageTk.PhotoImage(fondoMenuRe, master = canvasPrin)
canvasPrin.create_image(500,400, image=fondoMenuReFin)
def cambiar():
        canvasSobre = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="white")
        canvasSobre.place(relx=0.5, rely=0.5, anchor=CENTER)
        fondoSobre = Image.open("fondoAcerca.png")
        fondoSobreRe = fondoSobre.resize((1000, 600), Image.ANTIALIAS)
        fondoSobreReFin = ImageTk.PhotoImage(fondoSobreRe, master=canvasSobre)
        canvasSobre.create_image(500,400, image=fondoSobreReFin)
        def regresa():
                canvasSobre.destroy()
        btnRegresa = Button(canvasSobre, text="REGRESA", font=("Britannic Bold", 16) , width= 10,height= 1, fg="black", command=regresa)
        btnRegresa.place(x=850, y=650)
        canvasSobre.lift()

btnA = Button(canvasPrin, text="Acerca de", font=("Britannic Bold", 16) ,fg="black", bg= "white", width= 20,height= 1, anchor="center",command=cambiar)
btnA.place(x=175, y=475)

def niveles():
        canvasNiveles = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="white")
        canvasNiveles.place(relx=0.5, rely=0.5, anchor=CENTER)
        fondoNiveles = Image.open("2.jpg")
        fondoNivelesRe = fondoNiveles.resize((1000, 600), Image.ANTIALIAS)
        fondoNivelesReFin = ImageTk.PhotoImage(fondoNivelesRe, master=canvasPrin)
        canvasNiveles.create_image(500, 400, image=fondoNivelesReFin)

        def juego1():
                # Musicquita
                pygame.mixer.init()
                pygame.mixer_music.load("Morado.mp3")
                pygame.mixer_music.play(-1)
                # CANVAS DEL JUEGO
                canvasJuego = Canvas(framePrin, width=1000, height=550, bg="green")
                canvasJuego.place(relx=0.5, rely=0.54, anchor=CENTER)
                fondoPlanetaMorado = Image.open("NaranjaPlaneta.jpg")
                fondoPlanetaMoradoRe = fondoPlanetaMorado.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaMoradoFin = ImageTk.PhotoImage(fondoPlanetaMoradoRe, master=canvasPrin)
                canvasJuego.create_image(500, 280, image=fondoPlanetaMoradoFin)
                #IMAGEN DE BALA
                balas = Image.open("bala.png")
                balasRe = balas.resize((20, 10), Image.ANTIALIAS)
                balasReFin = ImageTk.PhotoImage(balasRe, master=canvasJuego)
                # CANVAS DISPLAY (MUESTRA EL SCORE Y LAS VIDAS)
                top = Canvas(framePrin, width=1000, height=50, bg="black")
                top.place(relx=0, rely=0)
                # PUNTAJE
                global score
                score = 0
                scoreLabel = Label(top, text="Score: " + str(score), bg="green", fg="white", font=("Arcade Gamer", 10))
                scoreLabel.place(x=50, y=15)
                # VIDAS
                global lives
                lives = 3
                livesLabel = Label(top, text="Vidas Extra: " + str(lives), bg="red", fg="white", font=(50))
                livesLabel.place(x=450, y=15)
                # CREACION NAVE
                ship = Image.open("nave.png")
                shipRe = ship.resize((75, 75), Image.ANTIALIAS)
                shipReFin = ImageTk.PhotoImage(shipRe, master=canvasJuego)
                myship = canvasJuego.create_image(100, 100, image=shipReFin)

                # ALIENS
                # LISTA PARA ALMACENAR TRES TIPOS DE ALIENS
                imagenes = []

                # FUNCION ALMACENA ALIENS EN LA LISTA
                def cargar_imagenes(i=1):
                        if i <= 3:
                                alien1 = Image.open(f"alien{i}.png")
                                alien1Re = alien1.resize((50, 50), Image.ANTIALIAS)
                                imagen = ImageTk.PhotoImage(alien1Re, master=canvasJuego)
                                imagenes.append(imagen)
                                cargar_imagenes(i + 1)

                cargar_imagenes()

                # CREA IMAGENES EN EL CANVAS Y LAS ALMACENA EN UNA LISTA
                objetos_imagenes = []

                def crear_imagenes(i=0, y=50):
                        # DEFINE LA CANTIDAD DE IMAGENES QUE SE CREAN
                        if i < 5:
                                x = random.randint(800, 1000)
                                imagen_objeto = canvasJuego.create_image(x, y, image=random.choice(imagenes))
                                objetos_imagenes.append(imagen_objeto)
                                crear_imagenes(i + 1, y + 50)

                crear_imagenes()

                # FUNCION QUE MUEVE LAS IMAGENES
                def mover_imagen(canvas, aliencito):
                        # NAVE LLEGA AL BORDE IZQUIERDO
                        global lives
                        myX = random.randint(-35, 0)
                        coordY = random.randint(30, 720)
                        canvas.move(aliencito, myX, 0)
                        alienCoords = canvas.bbox(aliencito)
                        if alienCoords[0] < 0:
                                canvasJuego.coords(aliencito, 1000, coordY)
                                lives = lives
                                livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                                if lives < 1:
                                        livesLabel.configure(text="Se murio", bg="red", fg="white")
                                        GameOver = Canvas(canvas, width=1000, height=750, bg="black")
                                        GameOver.place(x=0, y=0)

                        def moverBala(event):
                            shipCoords = canvasJuego.bbox(myship)
                            balitas = canvasJuego.create_image(shipCoords[2], (shipCoords[1] + shipCoords[3]) // 2,
                                                               image=balasReFin)

                            pew(balitas,aliencito)

                        def pew(balitas,alien):
                            canvasJuego.move(balitas, 25, 0)
                            chequea(balitas, objetos_imagenes, 0)
                            root.after(80, pew, balitas,alien)


                        # CONTROL EN EL PARA MOVER LAS BALAS
                        canvasJuego.bind_all("<space>", moverBala)
                        colisionConNave(alienCoords, aliencito)

                # COLISION CON LA NAVE
                def colisionConNave(alienCoords, aliencito):
                        global lives
                        shipCoords = canvasJuego.bbox(myship)
                        coordY = random.randint(50, 550)
                        if ((shipCoords[2] > alienCoords[0] > shipCoords[0]) and shipCoords[1] < alienCoords[3] <
                                shipCoords[3]):
                                canvasJuego.coords(aliencito, 1000, coordY)
                                lives = lives
                                livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                                if lives < 1:
                                        livesLabel.configure(text="Se murio", bg="red", fg="white")
                                        GameOver = Canvas(canvasJuego, width=1000, height=750, bg="black")
                                        GameOver.place(x=0, y=0)

                        # BALAS
                        # MOVER BALAS
                def chequea(balitas,objetos_imagenes,i):
                        if i < len(objetos_imagenes):
                                colisiona(balitas, objetos_imagenes, i)
                                chequea(balitas, objetos_imagenes, i + 1)


                def colisiona(balitas,objetos_imagenes,i):
                        balitaCoords = canvasJuego.bbox(balitas)
                        print(balitaCoords)
                        coordY = random.randint(50, 550)
                        alienCoords = canvasJuego.bbox(objetos_imagenes[i])
                        if ((alienCoords[2] > balitaCoords[0] > alienCoords[0]) and alienCoords[1] < balitaCoords[3] <
                                        alienCoords[3]):
                                canvasJuego.coords(objetos_imagenes[i], 1015, coordY)
                                canvasJuego.coords(balitas, 1100, 1000)







                # FUNCION QUE LLAMA A LA FUNCION PARA MOVER UNA IMAGEN PARA QUE RECURSIVAMENTE MUEVA VARIAS IMAGENES
                def mover_varias_imagenes(canvas, objetos_imagenes, i):
                        if i < len(objetos_imagenes):
                                # LLamada a funcion mover una imagen
                                mover_imagen(canvas, objetos_imagenes[i])
                                # LLamada recursiva
                                mover_varias_imagenes(canvas, objetos_imagenes, i + 1)

                # FUNCION PARA ANIMAR A LAS IMAGENES
                def animar():
                        mover_varias_imagenes(canvasJuego, objetos_imagenes, 0)

                        # LLAMADA RECURSIVA
                        root.after(1000, animar)

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
                        if shipCoords[3] > 550:
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

                # DEFINE LOS CONTROLES DE LA NAVE
                # FLECHAS
                canvasJuego.bind_all("<Up>", moverArriba)
                canvasJuego.bind_all("<Down>", moverAbajo)
                canvasJuego.bind_all("<Right>", moverDerecha)
                canvasJuego.bind_all("<Left>", moverIzquierda)

                # TECLADO
                canvasJuego.bind_all("<w>", moverArriba)
                canvasJuego.bind_all("<s>", moverAbajo)
                canvasJuego.bind_all("<d>", moverDerecha)
                canvasJuego.bind_all("<a>", moverIzquierda)

                # REGRESAR AL MENU DE INICIO
                def regresa():
                        # MUSIQUITA VENTANA INICIAL
                        pygame.mixer.init()
                        pygame.mixer_music.load("Fondo.mp3")
                        pygame.mixer_music.play(-1)
                        canvasJuego.destroy()
                        top.destroy()
                        canvasNiveles.destroy()

                btnRegresa = Button(top, text="Menu Inicial", font=("Britannic Bold", 16), width=10, height=1,
                                    fg="black",
                                    command=regresa)
                btnRegresa.place(x=850, y=8)
                myship.lift(AboveThis=btnRegresa)

        #BOTON QUE ABRE EL NIVEL 1
        btnNivel1 = Button(canvasNiveles, text="ATACAR", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=juego1)
        btnNivel1.place(x=125, y=475)

        def juego2():
                # Musicquita
                pygame.mixer.init()
                pygame.mixer_music.load("Morado.mp3")
                pygame.mixer_music.play(-1)
                # CANVAS DEL JUEGO
                canvasJuego = Canvas(framePrin, width=1000, height=550, bg="green")
                canvasJuego.place(relx=0.5, rely=0.54, anchor=CENTER)
                fondoPlanetaMorado = Image.open("MoradoPlaneta.jpg")
                fondoPlanetaMoradoRe = fondoPlanetaMorado.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaMoradoFin = ImageTk.PhotoImage(fondoPlanetaMoradoRe, master=canvasPrin)
                canvasJuego.create_image(500, 280, image=fondoPlanetaMoradoFin)

                balas = Image.open("bala.png")
                balasRe = balas.resize((20, 10), Image.ANTIALIAS)
                balasReFin = ImageTk.PhotoImage(balasRe, master=canvasJuego)

                # CANVAS DISPLAY (MUESTRA EL SCORE Y LAS VIDAS)
                top = Canvas(framePrin, width=1000, height=50, bg="black")
                top.place(relx=0, rely=0)
                # PUNTAJE
                global score
                score = 0
                scoreLabel = Label(top, text="Score: " + str(score), bg="green", fg="white", font=(50))
                scoreLabel.place(x=50, y=15)
                # VIDAS
                global lives
                lives = 3
                livesLabel = Label(top, text="Vidas Extra: " + str(lives), bg="red", fg="white", font=(50))
                livesLabel.place(x=450, y=15)
                # CREACION NAVE
                ship = Image.open("nave.png")
                shipRe = ship.resize((75, 75), Image.ANTIALIAS)
                shipReFin = ImageTk.PhotoImage(shipRe, master=canvasJuego)
                myship = canvasJuego.create_image(100, 100, image=shipReFin)

                # ALIENS
                # LISTA PARA ALMACENAR TRES TIPOS DE ALIENS
                imagenes = []

                # FUNCION ALMACENA ALIENS EN LA LISTA
                def cargar_imagenes(i=1):
                        if i <= 3:
                                alien1 = Image.open(f"alien{i}.png")
                                alien1Re = alien1.resize((50, 50), Image.ANTIALIAS)
                                imagen = ImageTk.PhotoImage(alien1Re, master=canvasJuego)
                                imagenes.append(imagen)
                                cargar_imagenes(i + 1)

                cargar_imagenes()

                # CREA IMAGENES EN EL CANVAS Y LAS ALMACENA EN UNA LISTA
                objetos_imagenes = []

                def crear_imagenes(i=0, y=50):
                        # DEFINE LA CANTIDAD DE IMAGENES QUE SE CREAN
                        if i < 5:
                                x = random.randint(800, 1000)
                                imagen_objeto = canvasJuego.create_image(x, y, image=random.choice(imagenes))
                                objetos_imagenes.append(imagen_objeto)
                                crear_imagenes(i + 1, y + 50)

                crear_imagenes()

                # FUNCION QUE MUEVE LAS IMAGENES
                def mover_imagen(canvas, aliencito):
                        # NAVE LLEGA AL BORDE IZQUIERDO
                        global lives
                        myX = random.randint(-35, 0)
                        coordY = random.randint(30, 720)
                        canvas.move(aliencito, myX, 0)
                        alienCoords = canvas.bbox(aliencito)
                        if alienCoords[0] < 0:
                                canvasJuego.coords(aliencito, 1000, coordY)
                                lives = lives
                                livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                                if lives < 1:
                                        livesLabel.configure(text="Se murio", bg="red", fg="white")
                                        GameOver = Canvas(canvas, width=1000, height=750, bg="black")
                                        GameOver.place(x=0, y=0)

                        def moverBala(event):
                                shipCoords = canvasJuego.bbox(myship)
                                balitas = canvasJuego.create_image(shipCoords[2], (shipCoords[1] + shipCoords[3]) // 2,
                                                                   image=balasReFin)
                                pew(balitas, aliencito)

                        def pew(balitas, alien):
                                canvasJuego.move(balitas, 25, 0)
                                chequea(balitas, objetos_imagenes, 0)
                                root.after(80, pew, balitas, alien)

                        # CONTROL EN EL PARA MOVER LAS BALAS
                        canvasJuego.bind_all("<space>", moverBala)
                        colisionConNave(alienCoords, aliencito)

                # COLISION CON LA NAVE
                def colisionConNave(alienCoords, aliencito):
                        global lives
                        shipCoords = canvasJuego.bbox(myship)
                        coordY = random.randint(50, 550)
                        if ((shipCoords[2] > alienCoords[0] > shipCoords[0]) and shipCoords[1] < alienCoords[3] <
                                shipCoords[3]):
                                canvasJuego.coords(aliencito, 1000, coordY)
                                lives = lives
                                livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                                if lives < 1:
                                        livesLabel.configure(text="Se murio", bg="red", fg="white")
                                        GameOver = Canvas(canvasJuego, width=1000, height=750, bg="black")
                                        GameOver.place(x=0, y=0)

                        # BALAS
                        # MOVER BALAS

                def chequea(balitas, objetos_imagenes, i):
                        if i < len(objetos_imagenes):
                                colisiona(balitas, objetos_imagenes, i)
                                return chequea(balitas, objetos_imagenes, i + 1)

                def colisiona(balitas, objetos_imagenes, i):
                        balitaCoords = canvasJuego.bbox(balitas)
                        print(balitaCoords)
                        coordY = random.randint(50, 550)
                        alienCoords = canvasJuego.bbox(objetos_imagenes[i])
                        if ((alienCoords[2] > balitaCoords[0] > alienCoords[0]) and alienCoords[1] < balitaCoords[3] <
                                alienCoords[3]):
                                canvasJuego.coords(objetos_imagenes[i], 1000, coordY)
                                canvasJuego.coords(balitas, 1000, 1000)

                # FUNCION QUE LLAMA A LA FUNCION PARA MOVER UNA IMAGEN PARA QUE RECURSIVAMENTE MUEVA VARIAS IMAGENES
                def mover_varias_imagenes(canvas, objetos_imagenes, i):
                        if i < len(objetos_imagenes):
                                # LLamada a funcion mover una imagen
                                mover_imagen(canvas, objetos_imagenes[i])
                                # LLamada recursiva
                                mover_varias_imagenes(canvas, objetos_imagenes, i + 1)

                # FUNCION PARA ANIMAR A LAS IMAGENES
                def animar():
                        mover_varias_imagenes(canvasJuego, objetos_imagenes, 0)

                        # LLAMADA RECURSIVA
                        root.after(1000, animar)

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
                        if shipCoords[3] > 550:
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

                # DEFINE LOS CONTROLES DE LA NAVE
                # FLECHAS
                canvasJuego.bind_all("<Up>", moverArriba)
                canvasJuego.bind_all("<Down>", moverAbajo)
                canvasJuego.bind_all("<Right>", moverDerecha)
                canvasJuego.bind_all("<Left>", moverIzquierda)

                # TECLADO
                canvasJuego.bind_all("<w>", moverArriba)
                canvasJuego.bind_all("<s>", moverAbajo)
                canvasJuego.bind_all("<d>", moverDerecha)
                canvasJuego.bind_all("<a>", moverIzquierda)

                # REGRESAR AL MENU DE INICIO
                def regresa():
                        # MUSIQUITA VENTANA INICIAL
                        pygame.mixer.init()
                        pygame.mixer_music.load("Fondo.mp3")
                        pygame.mixer_music.play(-1)
                        canvasJuego.destroy()
                        top.destroy()
                        canvasNiveles.destroy()

                btnRegresa = Button(top, text="Menu Inicial", font=("Britannic Bold", 16), width=10, height=1,
                                    fg="black",
                                    command=regresa)
                btnRegresa.place(x=850, y=8)
                myship.lift(AboveThis=btnRegresa)

        # BOTON QUE ABRE EL NIVEL 2
        btnNivel2 = Button(canvasNiveles, text="ATACAR", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=juego2)
        btnNivel2.place(x=450, y=475)

        def juego3():
                # Musicquita
                pygame.mixer.init()
                pygame.mixer_music.load("Verde.mp3")
                pygame.mixer_music.play(-1)
                # CANVAS DEL JUEGO
                canvasJuego = Canvas(framePrin, width=1000, height=550, bg="green")
                canvasJuego.place(relx=0.5, rely=0.54, anchor=CENTER)
                fondoPlanetaMorado = Image.open("VerdePlaneta.jpg")
                fondoPlanetaMoradoRe = fondoPlanetaMorado.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaMoradoFin = ImageTk.PhotoImage(fondoPlanetaMoradoRe, master=canvasPrin)
                canvasJuego.create_image(500, 280, image=fondoPlanetaMoradoFin)

                balas = Image.open("bala.png")
                balasRe = balas.resize((20, 10), Image.ANTIALIAS)
                balasReFin = ImageTk.PhotoImage(balasRe, master=canvasJuego)

                # CANVAS DISPLAY (MUESTRA EL SCORE Y LAS VIDAS)
                top = Canvas(framePrin, width=1000, height=50, bg="black")
                top.place(relx=0, rely=0)
                # PUNTAJE
                global score
                score = 0
                scoreLabel = Label(top, text="Score: " + str(score), bg="green", fg="white", font=(50))
                scoreLabel.place(x=50, y=15)
                # VIDAS
                global lives
                lives = 3
                livesLabel = Label(top, text="Vidas Extra: " + str(lives), bg="red", fg="white", font=(50))
                livesLabel.place(x=450, y=15)
                # CREACION NAVE
                ship = Image.open("nave.png")
                shipRe = ship.resize((75, 75), Image.ANTIALIAS)
                shipReFin = ImageTk.PhotoImage(shipRe, master=canvasJuego)
                myship = canvasJuego.create_image(100, 100, image=shipReFin)

                # ALIENS
                # LISTA PARA ALMACENAR TRES TIPOS DE ALIENS
                imagenes = []

                # FUNCION ALMACENA ALIENS EN LA LISTA
                def cargar_imagenes(i=1):
                        if i <= 3:
                                alien1 = Image.open(f"alien{i}.png")
                                alien1Re = alien1.resize((50, 50), Image.ANTIALIAS)
                                imagen = ImageTk.PhotoImage(alien1Re, master=canvasJuego)
                                imagenes.append(imagen)
                                cargar_imagenes(i + 1)

                cargar_imagenes()

                # CREA IMAGENES EN EL CANVAS Y LAS ALMACENA EN UNA LISTA
                objetos_imagenes = []

                def crear_imagenes(i=0, y=50):
                        # DEFINE LA CANTIDAD DE IMAGENES QUE SE CREAN
                        if i < 5:
                                x = random.randint(800, 1000)
                                imagen_objeto = canvasJuego.create_image(x, y, image=random.choice(imagenes))
                                objetos_imagenes.append(imagen_objeto)
                                crear_imagenes(i + 1, y + 50)

                crear_imagenes()

                # FUNCION QUE MUEVE LAS IMAGENES
                def mover_imagen(canvas, aliencito):
                        # NAVE LLEGA AL BORDE IZQUIERDO
                        global lives
                        myX = random.randint(-35, 0)
                        coordY = random.randint(30, 720)
                        canvas.move(aliencito, myX, 0)
                        alienCoords = canvas.bbox(aliencito)
                        if alienCoords[0] < 0:
                                canvasJuego.coords(aliencito, 1000, coordY)
                                lives = lives
                                livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                                if lives < 1:
                                        livesLabel.configure(text="Se murio", bg="red", fg="white")
                                        GameOver = Canvas(canvas, width=1000, height=750, bg="black")
                                        GameOver.place(x=0, y=0)

                        def moverBala(event):
                                shipCoords = canvasJuego.bbox(myship)
                                balitas = canvasJuego.create_image(shipCoords[2], (shipCoords[1] + shipCoords[3]) // 2,
                                                                   image=balasReFin)
                                pew(balitas, aliencito)

                        def pew(balitas, alien):
                                canvasJuego.move(balitas, 25, 0)
                                chequea(balitas, objetos_imagenes, 0)
                                root.after(80, pew, balitas, alien)

                        # CONTROL EN EL PARA MOVER LAS BALAS
                        canvasJuego.bind_all("<space>", moverBala)
                        colisionConNave(alienCoords, aliencito)

                # COLISION CON LA NAVE
                def colisionConNave(alienCoords, aliencito):
                        global lives
                        shipCoords = canvasJuego.bbox(myship)
                        coordY = random.randint(50, 550)
                        if ((shipCoords[2] > alienCoords[0] > shipCoords[0]) and shipCoords[1] < alienCoords[3] <
                                shipCoords[3]):
                                canvasJuego.coords(aliencito, 1000, coordY)
                                lives = lives
                                livesLabel.configure(text="Vidas Extra: " + str(lives), bg="red", fg="white")
                                if lives < 1:
                                        livesLabel.configure(text="Se murio", bg="red", fg="white")
                                        GameOver = Canvas(canvasJuego, width=1000, height=750, bg="black")
                                        GameOver.place(x=0, y=0)

                        # BALAS
                        # MOVER BALAS

                def chequea(balitas, objetos_imagenes, i):
                        if i < len(objetos_imagenes):
                                colisiona(balitas, objetos_imagenes, i)
                                return chequea(balitas, objetos_imagenes, i + 1)

                def colisiona(balitas, objetos_imagenes, i):
                        balitaCoords = canvasJuego.bbox(balitas)
                        print(balitaCoords)
                        coordY = random.randint(50, 550)
                        alienCoords = canvasJuego.bbox(objetos_imagenes[i])
                        if ((alienCoords[2] > balitaCoords[0] > alienCoords[0]) and alienCoords[1] < balitaCoords[3] <
                                alienCoords[3]):
                                canvasJuego.coords(objetos_imagenes[i], 1000, coordY)
                                canvasJuego.coords(balitas, 1000, 1000)

                # FUNCION QUE LLAMA A LA FUNCION PARA MOVER UNA IMAGEN PARA QUE RECURSIVAMENTE MUEVA VARIAS IMAGENES
                def mover_varias_imagenes(canvas, objetos_imagenes, i):
                        if i < len(objetos_imagenes):
                                # LLamada a funcion mover una imagen
                                mover_imagen(canvas, objetos_imagenes[i])
                                # LLamada recursiva
                                mover_varias_imagenes(canvas, objetos_imagenes, i + 1)

                # FUNCION PARA ANIMAR A LAS IMAGENES
                def animar():
                        mover_varias_imagenes(canvasJuego, objetos_imagenes, 0)

                        # LLAMADA RECURSIVA
                        root.after(1000, animar)

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
                        if shipCoords[3] > 550:
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

                # DEFINE LOS CONTROLES DE LA NAVE
                # FLECHAS
                canvasJuego.bind_all("<Up>", moverArriba)
                canvasJuego.bind_all("<Down>", moverAbajo)
                canvasJuego.bind_all("<Right>", moverDerecha)
                canvasJuego.bind_all("<Left>", moverIzquierda)

                # TECLADO
                canvasJuego.bind_all("<w>", moverArriba)
                canvasJuego.bind_all("<s>", moverAbajo)
                canvasJuego.bind_all("<d>", moverDerecha)
                canvasJuego.bind_all("<a>", moverIzquierda)

                # REGRESAR AL MENU DE INICIO
                def regresa():
                        # MUSIQUITA VENTANA INICIAL
                        pygame.mixer.init()
                        pygame.mixer_music.load("Fondo.mp3")
                        pygame.mixer_music.play(-1)
                        canvasJuego.destroy()
                        top.destroy()
                        canvasNiveles.destroy()

                btnRegresa = Button(top, text="Menu Inicial", font=("Britannic Bold", 16), width=10, height=1,
                                    fg="black",
                                    command=regresa)
                btnRegresa.place(x=850, y=8)
                myship.lift(AboveThis=btnRegresa)

        # BOTON QUE ABRE EL NIVEL 3
        btnNivel3 = Button(canvasNiveles, text="ATACAR", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=juego3)
        btnNivel3.place(x=775, y=475)

        def regresa():
                canvasNiveles.destroy()

        btnRegresa = Button(canvasNiveles, text="REGRESA", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=regresa)
        btnRegresa.place(x=850, y=650)
        canvasNiveles.lift()


btnA = Button(canvasPrin, text="Juego", font=("Britannic Bold", 16) ,fg="black", bg= "white", width= 20,height= 1, anchor="center",command=niveles)
btnA.place(x=400, y=540)
root.mainloop()
