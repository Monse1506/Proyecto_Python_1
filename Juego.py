from tkinter import *
import time
import random
from PIL import ImageTk, Image
import pygame


# ----------------------------------------------------------------- CREACION DE VENTANA ---------------------------------------------------------------
root = Tk()
root.geometry('1000x600')
root.resizable(width=False, height=False)
root.title('SPACE IMPACT')

# --------------------------------------------------------------- MUSIQUITA VENTANA INICIAL -----------------------------------------------------------
pygame.mixer.init()
pygame.mixer_music.load("Fondo.mp3")
pygame.mixer_music.play(-1)

# --------------------------------------------------------------- CREACION DE FRAME -------------------------------------------------------------------
framePrin = Frame(root, bg= "white")
framePrin.pack(side=TOP)
framePrin.configure(width=1000,height=600)

# ------------------------------------------------------------ CREACION DE CANVAS PARA PONER IMAGEN ---------------------------------------------------
canvasPrin = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="black")
canvasPrin.place(relx=0.5, rely=0.5, anchor=CENTER)

# ----------------------------------------------------IMAGEN DEFAULT DEL CANVAS AKA. FONDO PRINCIPAL DEL MENU ------------------------------------------
fondoMenu = Image.open("fondoPrincipal.jpg")
fondoMenuRe = fondoMenu.resize((1000, 600), Image.ANTIALIAS)
fondoMenuReFin = ImageTk.PhotoImage(fondoMenuRe, master = canvasPrin)
canvasPrin.create_image(500,400, image=fondoMenuReFin)
# -----------------------------------------------------FUNCION PARA ABRIR LA PANTALLA DE ACERCA DE------------------------------------------------------
def cambiar():
        # CANVAS E IMAGEN DE FONDO DE LA VENTANA ACERCA DE
        canvasSobre = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="white")
        canvasSobre.place(relx=0.5, rely=0.5, anchor=CENTER)
        fondoSobre = Image.open("fondoAcerca.png")
        fondoSobreRe = fondoSobre.resize((1000, 600), Image.ANTIALIAS)
        fondoSobreReFin = ImageTk.PhotoImage(fondoSobreRe, master=canvasSobre)
        canvasSobre.create_image(500,400, image=fondoSobreReFin)
        # FUNCION QUE REGRESA A LA VENTANA PRINCIPAL
        def regresa():
                canvasSobre.destroy()
        btnRegresa = Button(canvasSobre, text="REGRESA", font=("Britannic Bold", 16) , width= 10,height= 1, fg="black", command=regresa)
        btnRegresa.place(x=850, y=650)
        canvasSobre.lift()

# BOTON QUE ABRE LA VENTANA DE ACERCA DE
btnA = Button(canvasPrin, text="Acerca de", font=("Britannic Bold", 16) ,fg="black", bg= "white", width= 20,height= 1, anchor="center",command=cambiar)
btnA.place(x=175, y=475)

# ---------------------------------------------FUNCION PARA ABRIR LAS INSTRUCCIONES DEL JUEGO----------------------------------------------
def instrucciones():
        # CANVAS E IMAGEN DE FONDO DE LA VENTANA INSTRUCCIONES
        canvasIns = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="white")
        canvasIns.place(relx=0.5, rely=0.5, anchor=CENTER)
        fondoIns = Image.open("Instruccion.jpg")
        fondoInsRe = fondoIns.resize((1000, 600), Image.ANTIALIAS)
        fondoInsReFin = ImageTk.PhotoImage(fondoInsRe, master=canvasIns)
        canvasIns.create_image(500, 400, image=fondoInsReFin)
        # FUNCION QUE REGRESA A LA VENTANA PRINCIPAL
        def regresa():
                canvasIns.destroy()

        btnRegresa = Button(canvasIns, text="REGRESA", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=regresa)
        btnRegresa.place(x=850, y=650)
        canvasIns.lift()
# BOTON QUE ABRE LA VENTANA DE INSTRUCCIONES
btnIns = Button(canvasPrin, text="Instrucciones", font=("Britannic Bold", 16) ,fg="black", bg= "white", width= 20,height= 1, anchor="center",command=instrucciones)
btnIns.place(x=600, y=475)

# ---------------------------------------------FUNCION PARA ABRIR LA PANTALLA DE NIVELES ----------------------------------------------
def niveles():
        # CANVAS E IMAGEN DE FONDO DE LA VENTANA NIVELES
        canvasNiveles = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="white")
        canvasNiveles.place(relx=0.5, rely=0.5, anchor=CENTER)
        fondoNiveles = Image.open("2.jpg")
        fondoNivelesRe = fondoNiveles.resize((1000, 600), Image.ANTIALIAS)
        fondoNivelesReFin = ImageTk.PhotoImage(fondoNivelesRe, master=canvasPrin)
        canvasNiveles.create_image(500, 400, image=fondoNivelesReFin)
        # VARIABLE QUE HACE QUE LAS IMAGENES DEJEN DE MOVERSE, SI A = FALSE NO SE MUEVEN LOS ALIENS
        global a
        a = True
        # Variable que hace que el score solo se sume una vez
        global uno
        uno = True

        # ------------------------------- FUNCION PARA ABRIR LA PANTALLA QUE LE SOLICITA EL NOMRE AL JUGADOR ----------------------------------------------
        def jugador():
                # CANVAS E IMAGEN DE FONDO DE LA VENTANA NIVELES
                canvasNombre = Canvas(framePrin, width=500, height=250, bg="black")
                canvasNombre.place(relx=0.5, rely=0.54, anchor=CENTER)
                tituloLabel = Label(canvasNombre, text="Hola! Por favor ingresa tu nombre", bg="black", fg="white", font=("Playbill", 30))
                tituloLabel.place(x=80, y=25)
                # INPUT DONDE EL JUGADOR PONE EL NOMBRE
                entrada = Entry(canvasNombre)
                entrada.place(x=190, y=150)

                #FUNCION QUE GUARDA EL NOMBRE DEL JUGADOR EN UNA VARIABLE Y DEVUELVE AL CANVAS NIVELES
                def nombreJugador():
                        global nombre
                        nombre = entrada.get()
                        canvasNombre.destroy()

                # BOTON QUE GUARDA EL NOMBRE DEL JUGADOR EN UNA VARIABLE Y DEVUELVE AL CANVAS NIVELES
                btnJugador = Button( canvasNombre, text="Listo", font=("century", 10),
                                         command=nombreJugador)
                btnJugador.place(x=225, y=200)
        jugador()

        def juego1():
                # --------------------------------------------MUSICA DEL NIEVEL ------------------------------------------------------------------------------------------
                pygame.mixer.init()
                pygame.mixer_music.load("Naranja.mp3")
                pygame.mixer_music.play(-1)
                # ---------------------------------------------------------CANVAS DEL NIVEL ------------------------------------------------------------------------------
                canvasJuego = Canvas(framePrin, width=1000, height=550, bg="green")
                canvasJuego.place(relx=0.5, rely=0.54, anchor=CENTER)
                # -------------------------------------------------  FONDO DEL NIVEL -------------------------------------------------------------------------
                fondoPlaneta = Image.open("NaranjaPlaneta1.jpg")
                fondoPlanetaRe = fondoPlaneta.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaFin1 = ImageTk.PhotoImage(fondoPlanetaRe, master=canvasPrin)
                planeta1 = canvasJuego.create_image(500, 276, image=fondoPlanetaFin1)
                fondoPlaneta = Image.open("NaranjaPlaneta2.jpg")
                fondoPlanetaRe = fondoPlaneta.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaFin2 = ImageTk.PhotoImage(fondoPlanetaRe, master=canvasJuego)
                planeta2 = canvasJuego.create_image(1500, 276, image=fondoPlanetaFin2)
                planeta3 = canvasJuego.create_image(2500, 276, image=fondoPlanetaFin1)
                planeta4 = canvasJuego.create_image(3500, 276, image=fondoPlanetaFin2)
                def moverFondo():
                        global a
                        planeta1coords = canvasJuego.bbox(planeta1)
                        if planeta1coords[2] >= 0:
                                canvasJuego.move(planeta1, -10, 0)
                        elif planeta1coords[2] < 0:
                                canvasJuego.coords(planeta1, 3475, 276)
                        planeta2coords = canvasJuego.bbox(planeta2)
                        if planeta2coords[2] >= 0:
                                canvasJuego.move(planeta2, -10, 0)
                        elif planeta2coords[2] < 0:
                                canvasJuego.coords(planeta2, 3475, 276)
                        planeta3coords = canvasJuego.bbox(planeta3)
                        if planeta3coords[2] >= 0:
                                canvasJuego.move(planeta3, -10, 0)
                        elif planeta3coords[2] < 0:
                                canvasJuego.coords(planeta3, 3475, 276)
                        planeta4coords = canvasJuego.bbox(planeta4)
                        if planeta4coords[2] >= 0:
                                canvasJuego.move(planeta4, -10, 0)
                        elif planeta4coords[2] < 0:
                                canvasJuego.coords(planeta4, 3475, 276)
                        if a:
                           root.after(50, moverFondo)

                moverFondo()


                #IMAGEN DE BALA
                balas = Image.open("balaNaveS.png")
                balasRe = balas.resize((20, 10), Image.ANTIALIAS)
                balasReFin = ImageTk.PhotoImage(balasRe, master=canvasJuego)
                #----------------------------------------------------- CANVAS TOP (MUESTRA EL SCORE Y LAS VIDAS)---------------------------------------------------------
                top = Canvas(framePrin, width=1000, height=50, bg="black")
                top.place(relx=0, rely=0)
                global fin
                fin = True
                # ---------------------------------- PUNTAJE -----------------------------------------------------
                global score
                score = 0
                scoreLabel = Label(top, text=str(score) + " pts" , bg="black", fg="white", font=("Playbill", 30))
                scoreLabel.place(x=250, y=5)
                # ----------------------------- VIDAS -------------------------------------------------------------
                global lives
                lives = 3
                vida = Image.open("vidas.png")
                vida1Re = vida.resize((35, 35), Image.ANTIALIAS)
                vidaReFin1 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida1 = Label(image=vidaReFin1, bg="black")
                vida1.place(x=33, y=10)
                vidaReFin2 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida2 = Label(image=vidaReFin2, bg="black")
                vida2.place(x=80, y=10)
                vidaReFin3 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida3 = Label(image=vidaReFin3, bg="black")
                vida3.place(x=127,y=10)
                # ----------------------- NOMBRE DEL PLANETA ------------------------------------------------------
                planetaLabel = Label(top, text="SOLARIS", bg="black", fg="white", font=("Playbill", 30))
                planetaLabel.place(x=473, y=5)
                # --------------------------------------- TIEMPO --------------------------------------------------
                # counter : variable utilizada para guardar el tiempo de cuando empieza
                # menu : variable utilizada para guardar el tiempo de cuando se abre el menu
                # total: variable utilizada para guardar la cantidad de tiempo que ha transcurrido
                global counter, menu,total
                menu = 0
                counter = time.time()
                total = 0
                # Label que muestra el tiempo del jugador en la pantalla
                tiempoLabel = Label(top, text=str(counter) + " segundos", bg="black", fg="white", font=("Playbill", 30))
                tiempoLabel.place(x=650, y=5)
                # --------------------------------NOMBRE DEL JUGADOR ------------------------------------------
                # variable que almacena el nombre del jugador
                global nombre
                # Label que muestra el nombre del jugador en la pantalla
                nombreLabel = Label(top, text=nombre, bg="black", fg="white", font=("Playbill", 30))
                nombreLabel.place(x=850, y=5)
                # ------------------------ MENU ---------------------------------------------
                # Imagen del boton menu
                imagenMenu = Image.open("Menu.png")
                imagenMenuRe = imagenMenu.resize((40, 40), Image.ANTIALIAS)
                imagenMenuReFin = ImageTk.PhotoImage(imagenMenuRe, master=canvasPrin)

                # --------------- FUNCION QUE ABRE EL MENU DEL JUEGO --------------------------------------------
                def menuOpciones():
                        # a = variable que para las animaciones de los aliens en la pantalla
                        # menu = variable que toma el tiempo que se tarda en el menu y se lo resta al tiempo que ha pasado para que siempre de el tiempo en pantalla
                        global a, menu
                        menu = time.time()
                        a = False

                        # canvas de la pantalla menu y label
                        canvasMenu = Canvas(framePrin, width=500, height=250, bg="black")
                        canvasMenu.place(relx=0.5, rely=0.54, anchor=CENTER)
                        tituloLabel = Label(canvasMenu, text="Space Impact", bg="black", fg="white", font=("Playbill", 80))
                        tituloLabel.place(x=80, y=25)

                        # FUNCION QUE PARA LA MUSICA
                        def pararMusica():
                                pygame.mixer_music.stop()

                        # BOTON QUE ACTIVA LA FUNCION QUE PARA LA MUSICA
                        btnPara = Button(canvasMenu, text="Parar música", font=("century", 10), height=5, width=11,
                                         command=pararMusica)
                        btnPara.place(x=20, y=150)

                        # FUNCION QUE PONE LA MUSICA
                        def ponerMusica():
                                pygame.mixer.init()
                                pygame.mixer_music.load("Morado.mp3")
                                pygame.mixer_music.play(-1)

                        # BOTON QUE ACTIVA LA FUNCION QUE PONE LA MUSICA
                        btnPone = Button(canvasMenu, text="Poner música", font=("century", 10), height=5,
                                                 width=11,
                                                 command=ponerMusica)
                        btnPone.place(x=145, y=150)

                        # FUNCION QUE REGRESA A LA PANTALLA DE JUEGO
                        def regresa():
                                # a = variable que para las animaciones de los aliens en la pantalla
                                # menu = variable que toma el tiempo que se tarda en el menu y se lo resta al tiempo que ha pasado para que siempre de el tiempo en pantalla
                                canvasMenu.destroy()
                                global a, menu
                                menu = (time.time() - menu)//1
                                a = True
                                moverFondo()

                        # BOTON QUE REGRESA A LA PANTALLA DE JUEGO
                        btnRegresa = Button(canvasMenu, text="Volver al Juego", font=("century", 10), height=5,
                                         width=11,
                                         command=regresa)
                        btnRegresa.place(x=260, y=150)

                        # FUNCION QUE REGRESA A LA PANTALLA DE INCIO
                        def regresaInicio():
                                canvasMenu.destroy()
                                vida1.destroy()
                                vida2.destroy()
                                vida3.destroy()
                                canvasNiveles.destroy()
                                canvasJuego.destroy()
                                top.destroy()
                                global a
                                a = True

                        # FUNCION QUE REGRESA A LA PANTALLA DE INICIO
                        btnRegresa = Button(canvasMenu, text="Volver al Menu", font=("century", 10), height=5,
                                         width=11,
                                         command=regresaInicio)

                        btnRegresa.place(x=375, y=150)

                # BOTON QUE ABRE EL MENU
                btnMenu = Button(top,bg="black", image= imagenMenuReFin,
                                    command=menuOpciones)
                btnMenu.place(x=950, y=5)

                # ---------------------------------------------------------- CREACION NAVE ------------------------------------------
                ship = Image.open("nave.png")
                shipRe = ship.resize((75, 75), Image.ANTIALIAS)
                shipReFin = ImageTk.PhotoImage(shipRe, master=canvasJuego)
                myship = canvasJuego.create_image(100, 100, image=shipReFin)
                # ------------------------------------------------------------- ALIENS ----------------------------------------------------
                # LISTA PARA ALMACENAR TRES TIPOS DE ALIENS
                imagenes = []
                # FUNCION ALMACENA ALIENS EN LA LISTA
                def cargar_imagenes(i=1):
                        """
                        E: un indice
                        S: una lista con la cantidad de imagenes que se especifican en la restriccion
                        """
                        if i <= 3:
                                alien1 = Image.open(f"alien{i}.png")
                                alien1Re = alien1.resize((50, 50), Image.ANTIALIAS)
                                imagen = ImageTk.PhotoImage(alien1Re, master=canvasJuego)
                                imagenes.append(imagen)
                                # Llamada recursiva para cargar las imagenes de los aliens
                                cargar_imagenes(i + 1)

                cargar_imagenes()

                # CREA IMAGENES EN EL CANVAS Y LAS ALMACENA EN UNA LISTA
                objetos_imagenes = []
                def crear_imagenes(i=0, y=50):
                        """
                        :param i: Contador
                        :param y: Posicion incial donde se va a poner al alien
                        :return: Las imagenes en pantalla
                        """
                        # DEFINE LA CANTIDAD DE IMAGENES QUE SE CREAN
                        if i < 5:
                                # x: posicion en el eje X donde se crea el alien
                                # y : posicion en el eje y donde se crea el alien
                                x = random.randint(800, 1000)
                                imagen_objeto = canvasJuego.create_image(x, y, image=random.choice(imagenes))
                                objetos_imagenes.append(imagen_objeto)
                                # Llamada recursiva para crear aliens
                                crear_imagenes(i + 1, y + 100)
                # Llama a la funcion que crea los aliens en pantalla
                crear_imagenes()

                # Funcion que muestra la pantalla final una vez que se pierde o se gana en el juego
                def final():
                        # lives: vidas del jugador
                        # score: el puntaje del jugador
                        global lives,score,uno
                        # canvas de la pantalla final
                        GameOver = Canvas(canvasNiveles, width=1000, height=750, bg="black")
                        GameOver.place(x=0, y=0)
                        if lives < 0 :
                                # LABEL EN PANTALLA CUANDO SE PIERDEN TODAS LAS VIDAS
                                gameLabel = Label(GameOver, text="GAME OVER", bg="black",
                                          fg="white", font=("Playbill", 100))
                                gameLabel.place(x=300, y=150)
                        else:
                                # LABEL EN PANTALLA CUANDO SE GANA EL JUEGO
                                gameLabel = Label(GameOver, text="HAS CONQUISTADO SOLARIS", bg="black",
                                                  fg="white", font=("Playbill", 100))
                                gameLabel.place(x=25, y=150)

                                # Funcion que hace que el bonus se aplique solo una vez
                                if uno == True:
                                        score += 250
                                        uno = False

                                bonusLabel = Label(GameOver, text="Recibes un bonus de 250 pts !", bg="black",
                                             fg="white", font=("Playbill", 25))
                                bonusLabel.place(x=400, y=350)
                                puntajeLabel = Label(GameOver, text="Tu puntaje fue de " + str(score) + " pts", bg="black",
                                             fg="white", font=("Playbill", 25))
                                puntajeLabel.place(x=400, y=450)


                        # Variable que solo permite acceder al archivo txt una vez
                        global fin
                        if fin:
                                # Archivo de TXT
                                archivo = open('puntajeSolaris.txt', 'a')
                                # Guarda el puntaje y el nombre de la persona en el archivo txt
                                archivo.write(str(score) + "," + str(nombre) + "\n")
                                archivo.close()
                                # modifica la variable para que no se vuelva a acceder al archivo
                                fin = False

                        # FUNCION QUE HACE QUE VUELVA A LA PANTALLA PRINCIPAL
                        def regresaInicio():
                                GameOver.destroy()
                                vida1.destroy()
                                vida2.destroy()
                                vida3.destroy()
                                canvasNiveles.destroy()
                                canvasJuego.destroy()
                                top.destroy()

                        # BOTON QUE HACE QUE VUELVA A LA PANTALLA PRINCIPAL
                        btnRegresa = Button(GameOver, text="Volver a Jugar", font=("century", 10),
                                            command=regresaInicio)
                        btnRegresa.place(x=250, y=500)
                        canvasJuego.destroy()
                        btnMenu.destroy()
                        # ----------------------------------------------------- PUNTAJES -------------------------------------------
                        # FUNCION QUE GUARDA LOS MEJORES PUNTAJES
                        def mejoresPuntajes():
                                # CANVAS PUNTAJES
                                puntaje = Canvas(GameOver, width=500, height=250, bg="blue")
                                puntaje.place(x=245, y=300)
                                #FONDO DEL CANVAS
                                fondoPuntajes = Image.open("MejoresPuntajes.jpg")
                                fondoPuntajesRe = fondoPuntajes.resize((500, 250),
                                                                       Image.ANTIALIAS)
                                fondoPuntajesFin = ImageTk.PhotoImage(fondoPuntajesRe,
                                                                      master=puntaje)
                                puntaje.create_image(252, 127, image=fondoPuntajesFin)

                                # LABELS QUE MUESTRAN LOS TRES MEJORES PUNTAJES
                                puntaje1 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje1.place(x=60, y=100)
                                puntaje2 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje2.place(x=225, y=100)
                                puntaje3 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje3.place(x=385, y=100)
                                puntajeExito = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntajeExito.place(x=45, y=175)

                                # GUARDA EL TXT EN UNA VARIABLE
                                puntos = open("puntajeSolaris.txt", 'r')

                                # cant: contador que verifica la cantidad de lineas que hay en el documento txt
                                # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                # lineas: cantidad de lineas que tiene el documento txt
                                global cant, puntajes, lineas
                                lineas = puntos.readlines()
                                puntos.close()
                                cant = 0
                                puntajes = []

                                # pts: lista que almacena los 3 mejores puntajes
                                # i: contador que solo saca los tres primeros puntajes
                                global pts, i
                                pts = []
                                i = 0

                                # Modifica la lista puntajes poniendo como elementos cada una de las lineas del archivo txt
                                def punto():
                                        # cant: contador que verifica la cantidad de lineas que hay en el documento txt
                                        # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                        # lineas: cantidad de lineas que tiene el documento txt
                                        global cant, puntajes
                                        if cant < len(lineas):
                                                puntajes = [[int(lineas[cant].split(",")[0]),
                                                             lineas[cant].split(",")[1]]] + puntajes
                                                cant += 1
                                                # Llamada recursiva que hace que se repita la funcion hasta que cant sea = a la cantidad de elementos en lineas
                                                punto()

                                punto()

                                # FUNCION QUE SACA LOS TRES MEJORES PUNTAJES
                                def tres():
                                        # i: contador que solo saca los tres primeros puntajes
                                        # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                        global i, puntajes
                                        if i < 3:
                                                # FUNCION QUE ELIMINA DE LA LISTA EL ELEMENTO INGRESADO
                                                def nuevalista(a, lista, puntajesN):
                                                        global puntajes
                                                        """
                                                           :param a: elemento de la lista puntajes
                                                           :param lista: lista puntajes sin el primer elemento
                                                           :param puntajesN: lista que se crea a partir de la lista puntajes sin el elemento ingresado
                                                           :return: nueva lista que se crea a partir de la lista puntajes sin el elemento ingresado
                                                        """
                                                        if lista == []:
                                                                puntajes = puntajesN
                                                                return puntajesN
                                                        elif lista[0] == a:
                                                                return nuevalista(a, lista[1:], puntajesN)
                                                        else:
                                                                return nuevalista(a, lista[1:], [lista[0]] + puntajesN)

                                                # FUNCION SACA EL MEJOR PUNTAJE DE LA LISTA
                                                def mejores_puntajes(puntaje, lista):
                                                        """
                                                         :param puntaje: elemento de puntaje en la posicion 0
                                                        :param lista: lista puntaje sin el primer elemento
                                                        :return: modifica la lista pts y llama a la funcion nuevalista
                                                        """
                                                        # pts: lista que almacena los 3 mejores puntajes
                                                        global pts
                                                        if len(lista) == 0:
                                                                pts = [puntaje] + pts
                                                                return nuevalista(puntaje, puntajes, [])
                                                        elif puntaje[0] < lista[0][0]:
                                                                return mejores_puntajes(lista[0], lista[1:])
                                                        else:
                                                                return mejores_puntajes(puntaje, lista[1:])

                                                # llama a la funcion
                                                mejores_puntajes(puntajes[0], puntajes)
                                                # cambia el contador
                                                i += 1
                                                # llamada recursicva
                                                tres()
                                        else:
                                                # FUNCION QUE CHEQUEA SI EL PUNTAJE DEL JUGADOR ACTUAL ESTA EN EL TOP 3
                                                def esta(listap,nom,pun):
                                                        if listap == []:
                                                                return False
                                                        elif [pun,nom+"\n"] == listap[0]:
                                                                return True
                                                        else:
                                                                return esta(listap[1:],nom, pun)

                                                # MODIFICA LOS LABELS DE PUNTAJES
                                                puntaje3.configure(text=str(pts[0][1]) + str(
                                                                pts[0][0]) + " pts")
                                                puntaje2.configure(text=str(pts[1][1]) + str(
                                                              pts[1][0]) + " pts")
                                                puntaje1.configure(text=str(pts[2][1]) + str(
                                                                pts[2][0]) + " pts")
                                                if esta(pts,nombre,score):
                                                        puntajeExito.configure(text= "FELICIDADES ESTAS ENTRE LOS PRIMEROS TRES PUNTAJES !")
                                                else:
                                                        puntajeExito.configure(
                                                                text="NO TE ENCUENTRAS ENTRE LOS PRIMEROS TRES PUNTAJES :(")

                                tres()
                                # FUNCION QUE VUELVE A LA PANTALLA DE FIN DEL JUEGO
                                def regresa():
                                        puntaje.destroy()

                                # BOTON QUE VUELVE A LA PANTALLA DE FIN DEL JUEGO
                                btnPun = Button(puntaje, text="Regresar", font=("century", 10),
                                                command=regresa)
                                btnPun.place(x=410, y=210)

                                #LLAMADA QUE HACE QUE SE EJECUTE LA FUNCION QUE SACA LOS 3 MEJORES PUNTAJES
                                tres()
                                puntaje.lift()
                        # BOTON QUE ABRE LA PANTALLA DE MEJORES PUNTAJES
                        btnmejoresPun = Button(GameOver, text="Puntajes", font=("century", 10),
                                               command=mejoresPuntajes)
                        btnmejoresPun.place(x=650, y=500)

                # FUNCION QUE MUEVE LAS IMAGENES
                def mover_imagen(canvas, aliencito):
                        """
                        :param canvas: canvas donde esta el alien
                        :param aliencito: una de las imagenes de la lista que contiene a todos los aliens
                        :return: los aliens moviendose en el canvas
                        """
                        # total: tiempo transcurrido en la pantalla del juego
                        # a: variable que controla si se mueven o no los aliens
                        global total
                        if total < 100:
                           if a == True:
                                   # FUNCION QUE MODIFICA LA VARIABLE Y EL LABEL DEL TIEMPO
                                def tiempo():
                                        # counter : variable utilizada para guardar el tiempo de cuando empieza
                                        # menu : variable utilizada para guardar el tiempo de cuando se abre el menu
                                        # total: variable utilizada para guardar la cantidad de tiempo que ha transcurrido
                                           global counter, total, menu
                                           total = (time.time()- menu - counter)//1  # Modifica la variable total segundo a segundo
                                           tiempoLabel.config(text=str(total) + " segundos") # Modifica el label de tiempo para que este se muestre en pantalla

                                # Llamada a la funcion que modifica el tiempo
                                tiempo()
                               # NAVE DEL ALIEN LLEGA AL BORDE IZQUIERDO --------------------------------------------------------------------------------------------------
                                # lives: vidas del jugador
                                global lives
                                #myX: Velocidad de los aliens
                                myX = random.randint(-35, 0)
                                # Coordenada donde reaparece el alien
                                coordY = random.randint(30, 700)
                                # Hace que el alien se mueva en pantalla
                                canvas.move(aliencito, myX, 0)
                                alienCoords = canvas.bbox(aliencito)
                                # Chequea si el alien se sali[o de la pantalla y baja una vida si lo hizo
                                if alienCoords[0] < 0:
                                        canvasJuego.coords(aliencito, 1000, coordY)
                                        if lives == 3:
                                                lives = lives - 1
                                                vida3.destroy()
                                        elif lives == 2:
                                                lives = lives - 1
                                                vida2.destroy()
                                        elif lives == 1:
                                                lives = lives - 1
                                                vida1.destroy()
                                        else:
                                                lives = lives - 1
                                                # si ya no quedan vidas se va a la pantalla de fin del juego
                                                final()

                                # FUNCION CREA LAS BALAS Y LAS MUEVE ----------------------------------------------------------------------------
                                def moverBala(event):
                                        """
                                        :param event: Se preciona la barra espaciadora
                                        :return: lanza una bala
                                        """
                                        # variable que pone el juego en pausa
                                        if a == True:
                                          shipCoords = canvasJuego.bbox(myship)
                                          # crea la bala donde esta la nave del jugador
                                          balitas = canvasJuego.create_image(shipCoords[2], (shipCoords[1] + shipCoords[3]) // 2,
                                                               image=balasReFin)
                                          # llama a la funcion pew que mueve la bala
                                          pew(balitas)

                                # FUNCION QUE MUEVE LA BALA
                                def pew(balitas):
                                          """
                                          :param balitas: bala que se creo en la funcion moverBala
                                          :return: bala moviendose si no se sale de pantalla, elimina bala si se sale de pantalla
                                          """
                                          balitaCoords = canvasJuego.bbox(balitas)
                                          # mueve la bala
                                          canvasJuego.move(balitas, 25, 0)
                                          # chequea si la bala colisiono contra un alien
                                          chequea(balitas, objetos_imagenes, 0)
                                          # Repite la funcion mover cada 80 milisegundos
                                          if balitaCoords[2] < 1000:
                                                  root.after(80, pew, balitas)
                                          else:
                                                  canvasJuego.delete(balitas)



                                # CONTROL PARA DISPARAR BALAS
                                canvasJuego.bind_all("<space>", moverBala)
                                # FUNCION QUE CHEQUEA SI COLISIONA UN ALIEN CON LA NAVE
                                colisionConNave(alienCoords, aliencito)
                        else:
                                  # LLAMA A FUNCION QUE MUESTRA PANTALLA FINAL
                                   final()

                # FUNCION QUE CHEQUEA COLISION CON LA NAVE
                def colisionConNave(alienCoords, aliencito):
                        """
                        :param alienCoords: Coordenadas del alien
                        :param aliencito: alien al que pertenecen esas coordenadas
                        :return: chequea si la nave impacta con un alien
                        """
                        # lives: vidas del jugador
                        global lives
                        shipCoords = canvasJuego.bbox(myship)
                        coordY = random.randint(50, 550)
                        if ((shipCoords[2] > alienCoords[0] > shipCoords[0]) and shipCoords[1] < alienCoords[3] <
                                shipCoords[3]):
                                canvasJuego.coords(aliencito, 1000, coordY)
                                global lives
                                if lives == 3:
                                        lives = lives - 1
                                        vida3.destroy()
                                elif lives == 2:
                                        lives = lives - 1
                                        vida2.destroy()
                                elif lives == 1:
                                        lives = lives - 1
                                        vida1.destroy()
                                else:
                                        lives = lives - 1
                                        # muestra la pantalla final
                                        final()
                                        canvasJuego.destroy()
                                        btnMenu.destroy()

                # FUNCION QUE CHEQUEA SI LAS BALAS COLISIONARON CON UN ALIEN
                def chequea(balitas,objetos_imagenes,i):
                        """
                        :param balitas: bala que se va a chequear
                        :param objetos_imagenes: la lista que contiene las imagenes
                        :param i: parametro que se asegura que se chequen todas las imagenes
                        """
                        if i < len(objetos_imagenes):
                                # FUNCION QUE VERIFICA SI LAS BALAS CHOCAN CON UN ALIEN
                                colisiona(balitas, objetos_imagenes, i)
                                # LLAMADA RECURSIVA CAMBIANDOLE EL INDICE
                                chequea(balitas, objetos_imagenes, i + 1)

                # VERIFICA SI LAS BALAS CHOCAN CON UN ALIEN
                def colisiona(balitas,objetos_imagenes,i):
                        """
                        :param balitas: bala que se va a chequear
                        :param objetos_imagenes: lista que contiene a todos los aliens
                        :param i: indica el indice de la lista que se va a chequear
                        """
                        # score: contiene el puntaje de la persona
                        global score
                        balitaCoords = canvasJuego.bbox(balitas)
                        coordY = random.randint(50, 500)
                        alienCoords = canvasJuego.bbox(objetos_imagenes[i])
                        if ((alienCoords[2] > balitaCoords[0] > alienCoords[0]) and alienCoords[1] < balitaCoords[3] <
                                        alienCoords[3]):
                                score = score + 2 ** len(objetos_imagenes)
                                scoreLabel.configure(text=str(score) + " pts")
                                canvasJuego.coords(objetos_imagenes[i], 1005, coordY)
                                canvasJuego.coords(balitas, 1100, 1000)

                # FUNCION QUE LLAMA A LA FUNCION PARA MOVER UNA IMAGEN PARA QUE RECURSIVAMENTE MUEVA VARIAS IMAGENES
                def mover_varias_imagenes(canvas, objetos_imagenes, i):
                        """
                        :param canvas: indica el canvas donde va a aparecer las imagenes
                        :param objetos_imagenes: lista donde estan almacenados todos los aliens en pantalla
                        :param i: contador que verifica que no se salga la funcion de la cantidad de elementos en la lista
                        """
                        if i < len(objetos_imagenes):
                                # LLamada a funcion mover una imagen, le envia el canvas y una de las imagenes de los aliens en la lista
                                mover_imagen(canvas, objetos_imagenes[i])
                                # LLamada recursiva, se acaba cuando se recorran todas las imagenes de la lista
                                mover_varias_imagenes(canvas, objetos_imagenes, i + 1)

                # FUNCION PARA ANIMAR A LAS IMAGENES
                def animar():
                        # total: variable que almacena el tiempo
                        # llamada a la funcion mover vairias imagenes
                        mover_varias_imagenes(canvasJuego, objetos_imagenes, 0)
                        if total < 100:
                          # LLAMADA RECURSIVA
                          root.after(400, animar)

                # ACTIVA LA FUNCION QUE ANIMA LAS IMAGENES
                animar()

                # MOVIMIENTOS NAVE, VERIFICAN QUE NO SE SALGA LA NAVE DE LA PANTALLA
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

                myship.lift()

        #BOTON QUE ABRE EL NIVEL 1
        btnNivel1 = Button(canvasNiveles, text="ATACAR", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=juego1)
        btnNivel1.place(x=125, y=475)
        global tiempoenMenu
        tiempoenMenu = 0
        def juego2():
                # --------------------------------------------MUSICA DEL NIEVEL ------------------------------------------------------------------------------------------
                pygame.mixer.init()
                pygame.mixer_music.load("Morado.mp3")
                pygame.mixer_music.play(-1)
                # ---------------------------------------------------------CANVAS DEL NIVEL ------------------------------------------------------------------------------
                canvasJuego = Canvas(framePrin, width=1000, height=550, bg="green")
                canvasJuego.place(relx=0.5, rely=0.54, anchor=CENTER)
                # -------------------------------------------------  FONDO DEL NIVEL -------------------------------------------------------------------------
                fondoPlaneta = Image.open("MoradoPlaneta1.jpg")
                fondoPlanetaRe = fondoPlaneta.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaFin1 = ImageTk.PhotoImage(fondoPlanetaRe, master=canvasPrin)
                planeta1 = canvasJuego.create_image(500, 276, image=fondoPlanetaFin1)
                fondoPlaneta = Image.open("MoradoPlaneta2.jpg")
                fondoPlanetaRe = fondoPlaneta.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaFin2 = ImageTk.PhotoImage(fondoPlanetaRe, master=canvasJuego)
                planeta2 = canvasJuego.create_image(1500, 276, image=fondoPlanetaFin2)
                planeta3 = canvasJuego.create_image(2500, 276, image=fondoPlanetaFin1)
                planeta4 = canvasJuego.create_image(3500, 276, image=fondoPlanetaFin2)

                def moverFondo():
                        global a
                        planeta1coords = canvasJuego.bbox(planeta1)
                        if planeta1coords[2] >= 0:
                                canvasJuego.move(planeta1, -10, 0)
                        elif planeta1coords[2] < 0:
                                canvasJuego.coords(planeta1, 3475, 276)
                        planeta2coords = canvasJuego.bbox(planeta2)
                        if planeta2coords[2] >= 0:
                                canvasJuego.move(planeta2, -10, 0)
                        elif planeta2coords[2] < 0:
                                canvasJuego.coords(planeta2, 3475, 276)
                        planeta3coords = canvasJuego.bbox(planeta3)
                        if planeta3coords[2] >= 0:
                                canvasJuego.move(planeta3, -10, 0)
                        elif planeta3coords[2] < 0:
                                canvasJuego.coords(planeta3, 3475, 276)
                        planeta4coords = canvasJuego.bbox(planeta4)
                        if planeta4coords[2] >= 0:
                                canvasJuego.move(planeta4, -10, 0)
                        elif planeta4coords[2] < 0:
                                canvasJuego.coords(planeta4, 3475, 276)
                        if a:
                                root.after(50, moverFondo)

                moverFondo()
                # IMAGEN DE BALA --------------------------------------------------------------------------------------------------------------------------------------------
                balas = Image.open("balaNave.png")
                balasRe = balas.resize((20, 20), Image.ANTIALIAS)
                balasReFin = ImageTk.PhotoImage(balasRe, master=canvasJuego)
                # ----------------------------------------------------- CANVAS TOP (MUESTRA EL SCORE Y LAS VIDAS)---------------------------------------------------------
                top = Canvas(framePrin, width=1000, height=50, bg="black")
                top.place(relx=0, rely=0)
                global fin
                fin = True
                # ---------------------------------- PUNTAJE -----------------------------------------------------
                global score
                score = 0
                scoreLabel = Label(top, text=str(score) + " pts", bg="black", fg="white", font=("Playbill", 30))
                scoreLabel.place(x=250, y=5)
                # ----------------------------- VIDAS -------------------------------------------------------------
                global lives
                lives = 3
                vida = Image.open("vidas.png")
                vida1Re = vida.resize((35, 35), Image.ANTIALIAS)
                vidaReFin1 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida1 = Label(image=vidaReFin1, bg="black")
                vida1.place(x=33, y=10)
                vidaReFin2 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida2 = Label(image=vidaReFin2, bg="black")
                vida2.place(x=80, y=10)
                vidaReFin3 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida3 = Label(image=vidaReFin3, bg="black")
                vida3.place(x=127, y=10)
                # ----------------------- NOMBRE DEL PLANETA ------------------------------------------------------
                planetaLabel = Label(top, text="AXTURIAS", bg="black", fg="white", font=("Playbill", 30))
                planetaLabel.place(x=473, y=5)
                # --------------------------------------- TIEMPO --------------------------------------------------
                # counter : variable utilizada para guardar el tiempo de cuando empieza
                # menu : variable utilizada para guardar el tiempo de cuando se abre el menu
                # total: variable utilizada para guardar la cantidad de tiempo que ha transcurrido
                global counter, menu, total
                menu = 0
                counter = time.time()
                total = 0
                # Label que muestra el tiempo del jugador en la pantalla
                tiempoLabel = Label(top, text=str(counter) + " segundos", bg="black", fg="white", font=("Playbill", 30))
                tiempoLabel.place(x=650, y=5)
                # --------------------------------NOMBRE DEL JUGADOR ------------------------------------------
                # variable que almacena el nombre del jugador
                global nombre
                # Label que muestra el nombre del jugador en la pantalla
                nombreLabel = Label(top, text=nombre, bg="black", fg="white", font=("Playbill", 30))
                nombreLabel.place(x=850, y=5)
                # ------------------------ MENU ---------------------------------------------
                # Imagen del boton menu
                imagenMenu = Image.open("Menu.png")
                imagenMenuRe = imagenMenu.resize((40, 40), Image.ANTIALIAS)
                imagenMenuReFin = ImageTk.PhotoImage(imagenMenuRe, master=canvasPrin)

                # --------------- FUNCION QUE ABRE EL MENU DEL JUEGO --------------------------------------------
                def menuOpciones():
                        # a = variable que para las animaciones de los aliens en la pantalla
                        # menu = variable que toma el tiempo que se tarda en el menu y se lo resta al tiempo que ha pasado para que siempre de el tiempo en pantalla
                        global a, menu
                        menu = time.time()
                        a = False

                        # canvas de la pantalla menu y label
                        canvasMenu = Canvas(framePrin, width=500, height=250, bg="black")
                        canvasMenu.place(relx=0.5, rely=0.54, anchor=CENTER)
                        tituloLabel = Label(canvasMenu, text="Space Impact", bg="black", fg="white",
                                            font=("Playbill", 80))
                        tituloLabel.place(x=80, y=25)

                        # FUNCION QUE PARA LA MUSICA
                        def pararMusica():
                                pygame.mixer_music.stop()

                        # BOTON QUE ACTIVA LA FUNCION QUE PARA LA MUSICA
                        btnPara = Button(canvasMenu, text="Parar música", font=("century", 10), height=5, width=11,
                                         command=pararMusica)
                        btnPara.place(x=20, y=150)

                        # FUNCION QUE PONE LA MUSICA
                        def ponerMusica():
                                pygame.mixer.init()
                                pygame.mixer_music.load("Morado.mp3")
                                pygame.mixer_music.play(-1)

                        # BOTON QUE ACTIVA LA FUNCION QUE PONE LA MUSICA
                        btnPone = Button(canvasMenu, text="Poner música", font=("century", 10), height=5,
                                         width=11,
                                         command=ponerMusica)
                        btnPone.place(x=145, y=150)

                        # FUNCION QUE REGRESA A LA PANTALLA DE JUEGO
                        def regresa():
                                # a = variable que para las animaciones de los aliens en la pantalla
                                # menu = variable que toma el tiempo que se tarda en el menu y se lo resta al tiempo que ha pasado para que siempre de el tiempo en pantalla
                                canvasMenu.destroy()
                                global a, menu
                                menu = (time.time() - menu) // 1
                                a = True
                                moverFondo()

                        # BOTON QUE REGRESA A LA PANTALLA DE JUEGO
                        btnRegresa = Button(canvasMenu, text="Volver al Juego", font=("century", 10), height=5,
                                            width=11,
                                            command=regresa)
                        btnRegresa.place(x=260, y=150)

                        # FUNCION QUE REGRESA A LA PANTALLA DE INCIO
                        def regresaInicio():
                                canvasMenu.destroy()
                                vida1.destroy()
                                vida2.destroy()
                                vida3.destroy()
                                canvasNiveles.destroy()
                                canvasJuego.destroy()
                                top.destroy()
                                global a
                                a = True

                        # FUNCION QUE REGRESA A LA PANTALLA DE INICIO
                        btnRegresa = Button(canvasMenu, text="Volver al Menu", font=("century", 10), height=5,
                                            width=11,
                                            command=regresaInicio)

                        btnRegresa.place(x=375, y=150)

                # BOTON QUE ABRE EL MENU
                btnMenu = Button(top, bg="black", image=imagenMenuReFin,
                                 command=menuOpciones)
                btnMenu.place(x=950, y=5)

                # ---------------------------------------------------------- CREACION NAVE ------------------------------------------
                ship = Image.open("nave.png")
                shipRe = ship.resize((75, 75), Image.ANTIALIAS)
                shipReFin = ImageTk.PhotoImage(shipRe, master=canvasJuego)
                myship = canvasJuego.create_image(100, 100, image=shipReFin)
                # ------------------------------------------------------------- ALIENS ----------------------------------------------------
                # LISTA PARA ALMACENAR TRES TIPOS DE ALIENS
                imagenes = []

                # FUNCION ALMACENA ALIENS EN LA LISTA
                def cargar_imagenes(i=1):
                        """
                        E: un indice
                        S: una lista con la cantidad de imagenes que se especifican en la restriccion
                        """
                        if i <= 3:
                                alien1 = Image.open(f"alien{i}.png")
                                alien1Re = alien1.resize((50, 50), Image.ANTIALIAS)
                                imagen = ImageTk.PhotoImage(alien1Re, master=canvasJuego)
                                imagenes.append(imagen)
                                # Llamada recursiva para cargar las imagenes de los aliens
                                cargar_imagenes(i + 1)

                cargar_imagenes()

                # CREA IMAGENES EN EL CANVAS Y LAS ALMACENA EN UNA LISTA
                objetos_imagenes = []

                def crear_imagenes(i=0, y=50):
                        """
                        :param i: Contador
                        :param y: Posicion incial donde se va a poner al alien
                        :return: Las imagenes en pantalla
                        """
                        # DEFINE LA CANTIDAD DE IMAGENES QUE SE CREAN
                        if i < 10:
                                # x: posicion en el eje X donde se crea el alien
                                # y : posicion en el eje y donde se crea el alien
                                x = random.randint(800, 1000)
                                imagen_objeto = canvasJuego.create_image(x, y, image=random.choice(imagenes))
                                objetos_imagenes.append(imagen_objeto)
                                # Llamada recursiva para crear aliens
                                crear_imagenes(i + 1, y + 50)

                # Llama a la funcion que crea los aliens en pantalla
                crear_imagenes()

                # Funcion que muestra la pantalla final una vez que se pierde o se gana en el juego
                def final():
                        # lives: vidas del jugador
                        # score: el puntaje del jugador
                        global lives, score, uno
                        # canvas de la pantalla final
                        GameOver = Canvas(canvasNiveles, width=1000, height=750, bg="black")
                        GameOver.place(x=0, y=0)
                        if lives < 0:
                                # LABEL EN PANTALLA CUANDO SE PIERDEN TODAS LAS VIDAS
                                gameLabel = Label(GameOver, text="GAME OVER", bg="black",
                                                  fg="white", font=("Playbill", 100))
                                gameLabel.place(x=300, y=150)
                        else:
                                # LABEL EN PANTALLA CUANDO SE GANA EL JUEGO
                                gameLabel = Label(GameOver, text="HAS CONQUISTADO AXTURIAS", bg="black",
                                                  fg="white", font=("Playbill", 100))
                                gameLabel.place(x=25, y=150)

                                # Funcion que hace que el bonus se aplique solo una vez
                                if uno == True:
                                        score += 250
                                        uno = False

                                bonusLabel = Label(GameOver, text="Recibes un bonus de 250 pts !", bg="black",
                                                   fg="white", font=("Playbill", 25))
                                bonusLabel.place(x=400, y=350)
                                puntajeLabel = Label(GameOver, text="Tu puntaje fue de " + str(score) + " pts",
                                                     bg="black",
                                                     fg="white", font=("Playbill", 25))
                                puntajeLabel.place(x=400, y=450)

                        # Variable que solo permite acceder al archivo txt una vez
                        global fin
                        if fin:
                                # Archivo de TXT
                                archivo = open('puntajeAxtorias.txt', 'a')
                                # Guarda el puntaje y el nombre de la persona en el archivo txt
                                archivo.write(str(score) + "," + str(nombre) + "\n")
                                archivo.close()
                                # modifica la variable para que no se vuelva a acceder al archivo
                                fin = False

                        # FUNCION QUE HACE QUE VUELVA A LA PANTALLA PRINCIPAL
                        def regresaInicio():
                                GameOver.destroy()
                                vida1.destroy()
                                vida2.destroy()
                                vida3.destroy()
                                canvasNiveles.destroy()
                                canvasJuego.destroy()
                                top.destroy()

                        # BOTON QUE HACE QUE VUELVA A LA PANTALLA PRINCIPAL
                        btnRegresa = Button(GameOver, text="Volver a Jugar", font=("century", 10),
                                            command=regresaInicio)
                        btnRegresa.place(x=250, y=500)
                        canvasJuego.destroy()
                        btnMenu.destroy()

                        # ----------------------------------------------------- PUNTAJES -------------------------------------------
                        # FUNCION QUE GUARDA LOS MEJORES PUNTAJES
                        def mejoresPuntajes():
                                # CANVAS PUNTAJES
                                puntaje = Canvas(GameOver, width=500, height=250, bg="blue")
                                puntaje.place(x=245, y=300)
                                # FONDO DEL CANVAS
                                fondoPuntajes = Image.open("MejoresPuntajes.jpg")
                                fondoPuntajesRe = fondoPuntajes.resize((500, 250),
                                                                       Image.ANTIALIAS)
                                fondoPuntajesFin = ImageTk.PhotoImage(fondoPuntajesRe,
                                                                      master=puntaje)
                                puntaje.create_image(252, 127, image=fondoPuntajesFin)

                                # LABELS QUE MUESTRAN LOS TRES MEJORES PUNTAJES
                                puntaje1 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje1.place(x=60, y=100)
                                puntaje2 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje2.place(x=225, y=100)
                                puntaje3 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje3.place(x=385, y=100)
                                puntajeExito = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntajeExito.place(x=40, y=175)

                                # GUARDA EL TXT EN UNA VARIABLE
                                puntos = open("puntajeAxtorias.txt", 'r')

                                # cant: contador que verifica la cantidad de lineas que hay en el documento txt
                                # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                # lineas: cantidad de lineas que tiene el documento txt
                                global cant, puntajes, lineas
                                lineas = puntos.readlines()
                                puntos.close()
                                cant = 0
                                puntajes = []

                                # pts: lista que almacena los 3 mejores puntajes
                                # i: contador que solo saca los tres primeros puntajes
                                global pts, i
                                pts = []
                                i = 0

                                # Modifica la lista puntajes poniendo como elementos cada una de las lineas del archivo txt
                                def punto():
                                        # cant: contador que verifica la cantidad de lineas que hay en el documento txt
                                        # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                        # lineas: cantidad de lineas que tiene el documento txt
                                        global cant, puntajes
                                        if cant < len(lineas):
                                                puntajes = [[int(lineas[cant].split(",")[0]),
                                                             lineas[cant].split(",")[1]]] + puntajes
                                                cant += 1
                                                # Llamada recursiva que hace que se repita la funcion hasta que cant sea = a la cantidad de elementos en lineas
                                                punto()

                                punto()

                                # FUNCION QUE SACA LOS TRES MEJORES PUNTAJES
                                def tres():
                                        # i: contador que solo saca los tres primeros puntajes
                                        # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                        global i, puntajes
                                        if i < 3:
                                                # FUNCION QUE ELIMINA DE LA LISTA EL ELEMENTO INGRESADO
                                                def nuevalista(a, lista, puntajesN):
                                                        global puntajes
                                                        """
                                                           :param a: elemento de la lista puntajes
                                                           :param lista: lista puntajes sin el primer elemento
                                                           :param puntajesN: lista que se crea a partir de la lista puntajes sin el elemento ingresado
                                                           :return: nueva lista que se crea a partir de la lista puntajes sin el elemento ingresado
                                                        """
                                                        if lista == []:
                                                                puntajes = puntajesN
                                                                return puntajesN
                                                        elif lista[0] == a:
                                                                return nuevalista(a, lista[1:], puntajesN)
                                                        else:
                                                                return nuevalista(a, lista[1:], [lista[0]] + puntajesN)

                                                # FUNCION SACA EL MEJOR PUNTAJE DE LA LISTA
                                                def mejores_puntajes(puntaje, lista):
                                                        """
                                                         :param puntaje: elemento de puntaje en la posicion 0
                                                        :param lista: lista puntaje sin el primer elemento
                                                        :return: modifica la lista pts y llama a la funcion nuevalista
                                                        """
                                                        # pts: lista que almacena los 3 mejores puntajes
                                                        global pts
                                                        if len(lista) == 0:
                                                                pts = [puntaje] + pts
                                                                return nuevalista(puntaje, puntajes, [])
                                                        elif puntaje[0] < lista[0][0]:
                                                                return mejores_puntajes(lista[0], lista[1:])
                                                        else:
                                                                return mejores_puntajes(puntaje, lista[1:])

                                                # llama a la funcion
                                                mejores_puntajes(puntajes[0], puntajes)
                                                # cambia el contador
                                                i += 1
                                                # llamada recursicva
                                                tres()
                                        else:
                                                # FUNCION QUE CHEQUEA SI EL PUNTAJE DEL JUGADOR ACTUAL ESTA EN EL TOP 3
                                                def esta(listap, nom, pun):
                                                        if listap == []:
                                                                return False
                                                        elif [pun, nom + "\n"] == listap[0]:
                                                                return True
                                                        else:
                                                                return esta(listap[1:], nom, pun)

                                                # MODIFICA LOS LABELS DE PUNTAJES
                                                puntaje3.configure(text=str(pts[0][1]) + str(
                                                        pts[0][0]) + " pts")
                                                puntaje2.configure(text=str(pts[1][1]) + str(
                                                        pts[1][0]) + " pts")
                                                puntaje1.configure(text=str(pts[2][1]) + str(
                                                        pts[2][0]) + " pts")
                                                if esta(pts, nombre, score):
                                                        puntajeExito.configure(
                                                                text="FELICIDADES ESTAS ENTRE LOS PRIMEROS TRES PUNTAJES !")
                                                else:
                                                        puntajeExito.configure(
                                                                text="NO TE ENCUENTRAS ENTRE LOS PRIMEROS TRES PUNTAJES :(")

                                tres()

                                # FUNCION QUE VUELVE A LA PANTALLA DE FIN DEL JUEGO
                                def regresa():
                                        puntaje.destroy()

                                # BOTON QUE VUELVE A LA PANTALLA DE FIN DEL JUEGO
                                btnPun = Button(puntaje, text="Regresar", font=("century", 10),
                                                command=regresa)
                                btnPun.place(x=410, y=210)

                                # LLAMADA QUE HACE QUE SE EJECUTE LA FUNCION QUE SACA LOS 3 MEJORES PUNTAJES
                                tres()
                                puntaje.lift()

                        # BOTON QUE ABRE LA PANTALLA DE MEJORES PUNTAJES
                        btnmejoresPun = Button(GameOver, text="Puntajes", font=("century", 10),
                                               command=mejoresPuntajes)
                        btnmejoresPun.place(x=650, y=500)

                # FUNCION QUE MUEVE LAS IMAGENES
                def mover_imagen(canvas, aliencito):
                        """
                        :param canvas: canvas donde esta el alien
                        :param aliencito: una de las imagenes de la lista que contiene a todos los aliens
                        :return: los aliens moviendose en el canvas
                        """
                        # total: tiempo transcurrido en la pantalla del juego
                        # a: variable que controla si se mueven o no los aliens
                        global total
                        if total < 100:
                                if a == True:
                                        # FUNCION QUE MODIFICA LA VARIABLE Y EL LABEL DEL TIEMPO
                                        def tiempo():
                                                # counter : variable utilizada para guardar el tiempo de cuando empieza
                                                # menu : variable utilizada para guardar el tiempo de cuando se abre el menu
                                                # total: variable utilizada para guardar la cantidad de tiempo que ha transcurrido
                                                global counter, total, menu
                                                total = (
                                                                        time.time() - menu - counter) // 1  # Modifica la variable total segundo a segundo
                                                tiempoLabel.config(text=str(
                                                        total) + " segundos")  # Modifica el label de tiempo para que este se muestre en pantalla

                                        # Llamada a la funcion que modifica el tiempo
                                        tiempo()
                                        # NAVE DEL ALIEN LLEGA AL BORDE IZQUIERDO --------------------------------------------------------------------------------------------------
                                        # lives: vidas del jugador
                                        global lives
                                        # myX: Velocidad de los aliens
                                        myX = random.randint(-35, 0)
                                        # Coordenada donde reaparece el alien
                                        coordY = random.randint(30, 700)
                                        # Hace que el alien se mueva en pantalla
                                        canvas.move(aliencito, myX, 0)
                                        alienCoords = canvas.bbox(aliencito)
                                        # Chequea si el alien se sali[o de la pantalla y baja una vida si lo hizo
                                        if alienCoords[0] < 0:
                                                canvasJuego.coords(aliencito, 1000, coordY)
                                                if lives == 3:
                                                        lives = lives - 1
                                                        vida3.destroy()
                                                elif lives == 2:
                                                        lives = lives - 1
                                                        vida2.destroy()
                                                elif lives == 1:
                                                        lives = lives - 1
                                                        vida1.destroy()
                                                else:
                                                        lives = lives - 1
                                                        # si ya no quedan vidas se va a la pantalla de fin del juego
                                                        final()

                                        # FUNCION CREA LAS BALAS Y LAS MUEVE ----------------------------------------------------------------------------
                                        def moverBala(event):
                                                """
                                                :param event: Se preciona la barra espaciadora
                                                :return: lanza una bala
                                                """
                                                # variable que pone el juego en pausa
                                                if a == True:
                                                        shipCoords = canvasJuego.bbox(myship)
                                                        # crea la bala donde esta la nave del jugador
                                                        balitas = canvasJuego.create_image(shipCoords[2], (
                                                                        shipCoords[1] + shipCoords[3]) // 2,
                                                                                           image=balasReFin)
                                                        # llama a la funcion pew que mueve la bala
                                                        pew(balitas)

                                        # FUNCION QUE MUEVE LA BALA
                                        def pew(balitas):
                                                """
                                                :param balitas: bala que se creo en la funcion moverBala
                                                :return: bala moviendose si no se sale de pantalla, elimina bala si se sale de pantalla
                                                """
                                                balitaCoords = canvasJuego.bbox(balitas)
                                                # mueve la bala
                                                canvasJuego.move(balitas, 25, 0)
                                                # chequea si la bala colisiono contra un alien
                                                chequea(balitas, objetos_imagenes, 0)
                                                # Repite la funcion mover cada 80 milisegundos
                                                if balitaCoords[2] < 1000:
                                                        root.after(80, pew, balitas)
                                                else:
                                                        canvasJuego.delete(balitas)

                                        # CONTROL PARA DISPARAR BALAS
                                        canvasJuego.bind_all("<space>", moverBala)
                                        # FUNCION QUE CHEQUEA SI COLISIONA UN ALIEN CON LA NAVE
                                        colisionConNave(alienCoords, aliencito)
                        else:
                                # LLAMA A FUNCION QUE MUESTRA PANTALLA FINAL
                                final()

                # FUNCION QUE CHEQUEA COLISION CON LA NAVE
                def colisionConNave(alienCoords, aliencito):
                        """
                        :param alienCoords: Coordenadas del alien
                        :param aliencito: alien al que pertenecen esas coordenadas
                        :return: chequea si la nave impacta con un alien
                        """
                        # lives: vidas del jugador
                        global lives
                        shipCoords = canvasJuego.bbox(myship)
                        coordY = random.randint(50, 550)
                        if ((shipCoords[2] > alienCoords[0] > shipCoords[0]) and shipCoords[1] < alienCoords[3] <
                                shipCoords[3]):
                                canvasJuego.coords(aliencito, 1000, coordY)
                                global lives
                                if lives == 3:
                                        lives = lives - 1
                                        vida3.destroy()
                                elif lives == 2:
                                        lives = lives - 1
                                        vida2.destroy()
                                elif lives == 1:
                                        lives = lives - 1
                                        vida1.destroy()
                                else:
                                        lives = lives - 1
                                        # muestra la pantalla final
                                        final()
                                        canvasJuego.destroy()
                                        btnMenu.destroy()

                # FUNCION QUE CHEQUEA SI LAS BALAS COLISIONARON CON UN ALIEN
                def chequea(balitas, objetos_imagenes, i):
                        """
                        :param balitas: bala que se va a chequear
                        :param objetos_imagenes: la lista que contiene las imagenes
                        :param i: parametro que se asegura que se chequen todas las imagenes
                        """
                        if i < len(objetos_imagenes):
                                # FUNCION QUE VERIFICA SI LAS BALAS CHOCAN CON UN ALIEN
                                colisiona(balitas, objetos_imagenes, i)
                                # LLAMADA RECURSIVA CAMBIANDOLE EL INDICE
                                chequea(balitas, objetos_imagenes, i + 1)

                # VERIFICA SI LAS BALAS CHOCAN CON UN ALIEN
                def colisiona(balitas, objetos_imagenes, i):
                        """
                        :param balitas: bala que se va a chequear
                        :param objetos_imagenes: lista que contiene a todos los aliens
                        :param i: indica el indice de la lista que se va a chequear
                        """
                        # score: contiene el puntaje de la persona
                        global score
                        balitaCoords = canvasJuego.bbox(balitas)
                        coordY = random.randint(50, 500)
                        alienCoords = canvasJuego.bbox(objetos_imagenes[i])
                        if ((alienCoords[2] > balitaCoords[0] > alienCoords[0]) and alienCoords[1] < balitaCoords[3] <
                                alienCoords[3]):
                                score = score + 2 ** len(objetos_imagenes)
                                scoreLabel.configure(text=str(score) + " pts")
                                canvasJuego.coords(objetos_imagenes[i], 1005, coordY)
                                canvasJuego.coords(balitas, 1100, 1000)

                # FUNCION QUE LLAMA A LA FUNCION PARA MOVER UNA IMAGEN PARA QUE RECURSIVAMENTE MUEVA VARIAS IMAGENES
                def mover_varias_imagenes(canvas, objetos_imagenes, i):
                        """
                        :param canvas: indica el canvas donde va a aparecer las imagenes
                        :param objetos_imagenes: lista donde estan almacenados todos los aliens en pantalla
                        :param i: contador que verifica que no se salga la funcion de la cantidad de elementos en la lista
                        """
                        if i < len(objetos_imagenes):
                                # LLamada a funcion mover una imagen, le envia el canvas y una de las imagenes de los aliens en la lista
                                mover_imagen(canvas, objetos_imagenes[i])
                                # LLamada recursiva, se acaba cuando se recorran todas las imagenes de la lista
                                mover_varias_imagenes(canvas, objetos_imagenes, i + 1)

                # FUNCION PARA ANIMAR A LAS IMAGENES
                def animar():
                        # total: variable que almacena el tiempo
                        # llamada a la funcion mover vairias imagenes
                        mover_varias_imagenes(canvasJuego, objetos_imagenes, 0)
                        if total < 100:
                                # LLAMADA RECURSIVA
                                root.after(300, animar)

                # ACTIVA LA FUNCION QUE ANIMA LAS IMAGENES
                animar()

                # MOVIMIENTOS NAVE, VERIFICAN QUE NO SE SALGA LA NAVE DE LA PANTALLA
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

                myship.lift()

        # BOTON QUE ABRE EL NIVEL 2
        btnNivel2 = Button(canvasNiveles, text="ATACAR", font=("Britannic Bold", 16), width=10, height=1, fg="black",
                            command=juego2)
        btnNivel2.place(x=450, y=475)

        def juego3():
                # --------------------------------------------MUSICA DEL NIEVEL ------------------------------------------------------------------------------------------
                pygame.mixer.init()
                pygame.mixer_music.load("Verde.mp3")
                pygame.mixer_music.play(-1)
                # ---------------------------------------------------------CANVAS DEL NIVEL ------------------------------------------------------------------------------
                canvasJuego = Canvas(framePrin, width=1000, height=550, bg="green")
                canvasJuego.place(relx=0.5, rely=0.54, anchor=CENTER)
                # -------------------------------------------------  FONDO DEL NIVEL -------------------------------------------------------------------------
                fondoPlaneta = Image.open("VerdePlaneta1.jpg")
                fondoPlanetaRe = fondoPlaneta.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaFin1 = ImageTk.PhotoImage(fondoPlanetaRe, master=canvasPrin)
                planeta1 = canvasJuego.create_image(500, 276, image=fondoPlanetaFin1)
                fondoPlaneta = Image.open("VerdePlaneta2.jpg")
                fondoPlanetaRe = fondoPlaneta.resize((1010, 550), Image.ANTIALIAS)
                fondoPlanetaFin2 = ImageTk.PhotoImage(fondoPlanetaRe, master=canvasJuego)
                planeta2 = canvasJuego.create_image(1500, 276, image=fondoPlanetaFin2)
                planeta3 = canvasJuego.create_image(2500, 276, image=fondoPlanetaFin1)
                planeta4 = canvasJuego.create_image(3500, 276, image=fondoPlanetaFin2)

                def moverFondo():
                        global a
                        planeta1coords = canvasJuego.bbox(planeta1)
                        if planeta1coords[2] >= 0:
                                canvasJuego.move(planeta1, -10, 0)
                        elif planeta1coords[2] < 0:
                                canvasJuego.coords(planeta1, 3475, 276)
                        planeta2coords = canvasJuego.bbox(planeta2)
                        if planeta2coords[2] >= 0:
                                canvasJuego.move(planeta2, -10, 0)
                        elif planeta2coords[2] < 0:
                                canvasJuego.coords(planeta2, 3475, 276)
                        planeta3coords = canvasJuego.bbox(planeta3)
                        if planeta3coords[2] >= 0:
                                canvasJuego.move(planeta3, -10, 0)
                        elif planeta3coords[2] < 0:
                                canvasJuego.coords(planeta3, 3475, 276)
                        planeta4coords = canvasJuego.bbox(planeta4)
                        if planeta4coords[2] >= 0:
                                canvasJuego.move(planeta4, -10, 0)
                        elif planeta4coords[2] < 0:
                                canvasJuego.coords(planeta4, 3475, 276)
                        if a:
                                root.after(50, moverFondo)

                moverFondo()
                # IMAGEN DE BALA ---------------------------------------------------------------------------------------------------------------
                balas = Image.open("balaNave.png")
                balasRe = balas.resize((20, 20), Image.ANTIALIAS)
                balasReNave = ImageTk.PhotoImage(balasRe, master=canvasJuego)

                balasA = Image.open("balaAlien.png")
                balasReA = balasA.resize((30, 30), Image.ANTIALIAS)
                balasReAlien = ImageTk.PhotoImage(balasReA, master=canvasJuego)

                global listaBalaA
                listaBalaA = []
                # ----------------------------------------------------- CANVAS TOP (MUESTRA EL SCORE Y LAS VIDAS)---------------------------------------------------------
                top = Canvas(framePrin, width=1000, height=50, bg="black")
                top.place(relx=0, rely=0)
                global fin
                fin = True
                # ---------------------------------- PUNTAJE -----------------------------------------------------
                global score
                score = 0
                scoreLabel = Label(top, text=str(score) + " pts", bg="black", fg="white", font=("Playbill", 30))
                scoreLabel.place(x=250, y=5)
                # ----------------------------- VIDAS -------------------------------------------------------------
                global lives
                lives = 3
                vida = Image.open("vidas.png")
                vida1Re = vida.resize((35, 35), Image.ANTIALIAS)
                vidaReFin1 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida1 = Label(image=vidaReFin1, bg="black")
                vida1.place(x=33, y=10)
                vidaReFin2 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida2 = Label(image=vidaReFin2, bg="black")
                vida2.place(x=80, y=10)
                vidaReFin3 = ImageTk.PhotoImage(vida1Re, master=canvasPrin)
                vida3 = Label(image=vidaReFin3, bg="black")
                vida3.place(x=127, y=10)
                # ----------------------- NOMBRE DEL PLANETA ------------------------------------------------------
                planetaLabel = Label(top, text="CYBERTRON", bg="black", fg="white", font=("Playbill", 30))
                planetaLabel.place(x=473, y=5)
                # --------------------------------------- TIEMPO --------------------------------------------------
                # counter : variable utilizada para guardar el tiempo de cuando empieza
                # menu : variable utilizada para guardar el tiempo de cuando se abre el menu
                # total: variable utilizada para guardar la cantidad de tiempo que ha transcurrido
                global counter, menu, total
                menu = 0
                counter = time.time()
                total = 0
                # Label que muestra el tiempo del jugador en la pantalla
                tiempoLabel = Label(top, text=str(counter) + " segundos", bg="black", fg="white", font=("Playbill", 30))
                tiempoLabel.place(x=650, y=5)
                # --------------------------------NOMBRE DEL JUGADOR ------------------------------------------
                # variable que almacena el nombre del jugador
                global nombre
                # Label que muestra el nombre del jugador en la pantalla
                nombreLabel = Label(top, text=nombre, bg="black", fg="white", font=("Playbill", 30))
                nombreLabel.place(x=850, y=5)
                # ------------------------ MENU ---------------------------------------------
                # Imagen del boton menu
                imagenMenu = Image.open("Menu.png")
                imagenMenuRe = imagenMenu.resize((40, 40), Image.ANTIALIAS)
                imagenMenuReFin = ImageTk.PhotoImage(imagenMenuRe, master=canvasPrin)

                # --------------- FUNCION QUE ABRE EL MENU DEL JUEGO --------------------------------------------
                def menuOpciones():
                        # a = variable que para las animaciones de los aliens en la pantalla
                        # menu = variable que toma el tiempo que se tarda en el menu y se lo resta al tiempo que ha pasado para que siempre de el tiempo en pantalla
                        global a, menu
                        menu = time.time()
                        a = False

                        # canvas de la pantalla menu y label
                        canvasMenu = Canvas(framePrin, width=500, height=250, bg="black")
                        canvasMenu.place(relx=0.5, rely=0.54, anchor=CENTER)
                        tituloLabel = Label(canvasMenu, text="Space Impact", bg="black", fg="white",
                                            font=("Playbill", 80))
                        tituloLabel.place(x=80, y=25)

                        # FUNCION QUE PARA LA MUSICA
                        def pararMusica():
                                pygame.mixer_music.stop()

                        # BOTON QUE ACTIVA LA FUNCION QUE PARA LA MUSICA
                        btnPara = Button(canvasMenu, text="Parar música", font=("century", 10), height=5, width=11,
                                         command=pararMusica)
                        btnPara.place(x=20, y=150)

                        # FUNCION QUE PONE LA MUSICA
                        def ponerMusica():
                                pygame.mixer.init()
                                pygame.mixer_music.load("Morado.mp3")
                                pygame.mixer_music.play(-1)

                        # BOTON QUE ACTIVA LA FUNCION QUE PONE LA MUSICA
                        btnPone = Button(canvasMenu, text="Poner música", font=("century", 10), height=5,
                                         width=11,
                                         command=ponerMusica)
                        btnPone.place(x=145, y=150)

                        # FUNCION QUE REGRESA A LA PANTALLA DE JUEGO
                        def regresa():
                                # a = variable que para las animaciones de los aliens en la pantalla
                                # menu = variable que toma el tiempo que se tarda en el menu y se lo resta al tiempo que ha pasado para que siempre de el tiempo en pantalla
                                canvasMenu.destroy()
                                global a, menu
                                menu = (time.time() - menu) // 1
                                a = True
                                moverFondo()

                        # BOTON QUE REGRESA A LA PANTALLA DE JUEGO
                        btnRegresa = Button(canvasMenu, text="Volver al Juego", font=("century", 10), height=5,
                                            width=11,
                                            command=regresa)
                        btnRegresa.place(x=260, y=150)

                        # FUNCION QUE REGRESA A LA PANTALLA DE INCIO
                        def regresaInicio():
                                canvasMenu.destroy()
                                vida1.destroy()
                                vida2.destroy()
                                vida3.destroy()
                                canvasNiveles.destroy()
                                canvasJuego.destroy()
                                top.destroy()
                                global a
                                a = True

                        # FUNCION QUE REGRESA A LA PANTALLA DE INICIO
                        btnRegresa = Button(canvasMenu, text="Volver al Menu", font=("century", 10), height=5,
                                            width=11,
                                            command=regresaInicio)

                        btnRegresa.place(x=375, y=150)

                # BOTON QUE ABRE EL MENU
                btnMenu = Button(top, bg="black", image=imagenMenuReFin,
                                 command=menuOpciones)
                btnMenu.place(x=950, y=5)

                # ---------------------------------------------------------- CREACION NAVE ------------------------------------------
                ship = Image.open("nave.png")
                shipRe = ship.resize((75, 75), Image.ANTIALIAS)
                shipReFin = ImageTk.PhotoImage(shipRe, master=canvasJuego)
                myship = canvasJuego.create_image(100, 100, image=shipReFin)
                # ------------------------------------------------------------- ALIENS ----------------------------------------------------
                # LISTA PARA ALMACENAR TRES TIPOS DE ALIENS
                imagenes = []

                # FUNCION ALMACENA ALIENS EN LA LISTA
                def cargar_imagenes(i=1):
                        """
                        E: un indice
                        S: una lista con la cantidad de imagenes que se especifican en la restriccion
                        """
                        if i <= 3:
                                alien1 = Image.open(f"alien{i}.png")
                                alien1Re = alien1.resize((50, 50), Image.ANTIALIAS)
                                imagen = ImageTk.PhotoImage(alien1Re, master=canvasJuego)
                                imagenes.append(imagen)
                                # Llamada recursiva para cargar las imagenes de los aliens
                                cargar_imagenes(i + 1)

                cargar_imagenes()

                # CREA IMAGENES EN EL CANVAS Y LAS ALMACENA EN UNA LISTA
                objetos_imagenes = []

                def crear_imagenes(i=0, y=50):
                        """
                        :param i: Contador
                        :param y: Posicion incial donde se va a poner al alien
                        :return: Las imagenes en pantalla
                        """
                        # DEFINE LA CANTIDAD DE IMAGENES QUE SE CREAN
                        if i < 5:
                                # x: posicion en el eje X donde se crea el alien
                                # y : posicion en el eje y donde se crea el alien
                                x = random.randint(800, 1000)
                                imagen_objeto = canvasJuego.create_image(x, y, image=random.choice(imagenes))
                                objetos_imagenes.append(imagen_objeto)
                                # Llamada recursiva para crear aliens
                                crear_imagenes(i + 1, y + 100)

                # Llama a la funcion que crea los aliens en pantalla
                crear_imagenes()

                # Funcion que muestra la pantalla final una vez que se pierde o se gana en el juego
                def final():
                        # lives: vidas del jugador
                        # score: el puntaje del jugador
                        global lives, score, uno
                        # canvas de la pantalla final
                        GameOver = Canvas(canvasNiveles, width=1000, height=750, bg="black")
                        GameOver.place(x=0, y=0)
                        if lives < 0:
                                # LABEL EN PANTALLA CUANDO SE PIERDEN TODAS LAS VIDAS
                                gameLabel = Label(GameOver, text="GAME OVER", bg="black",
                                                  fg="white", font=("Playbill", 100))
                                gameLabel.place(x=300, y=150)
                        else:
                                # LABEL EN PANTALLA CUANDO SE GANA EL JUEGO
                                gameLabel = Label(GameOver, text="HAS CONQUISTADO CYBERTRON", bg="black",
                                                  fg="white", font=("Playbill", 80))
                                gameLabel.place(x=50, y=150)

                                # Funcion que hace que el bonus se aplique solo una vez
                                if uno == True:
                                        score += 250
                                        uno = False

                                bonusLabel = Label(GameOver, text="Recibes un bonus de 250 pts !", bg="black",
                                                   fg="white", font=("Playbill", 25))
                                bonusLabel.place(x=400, y=350)
                                puntajeLabel = Label(GameOver, text="Tu puntaje fue de " + str(score) + " pts",
                                                     bg="black",
                                                     fg="white", font=("Playbill", 25))
                                puntajeLabel.place(x=400, y=450)

                        # Variable que solo permite acceder al archivo txt una vez
                        global fin
                        if fin:
                                # Archivo de TXT
                                archivo = open('PuntajeCybertron.txt', 'a')
                                # Guarda el puntaje y el nombre de la persona en el archivo txt
                                archivo.write(str(score) + "," + str(nombre) + "\n")
                                archivo.close()
                                # modifica la variable para que no se vuelva a acceder al archivo
                                fin = False

                        # FUNCION QUE HACE QUE VUELVA A LA PANTALLA PRINCIPAL
                        def regresaInicio():
                                GameOver.destroy()
                                vida1.destroy()
                                vida2.destroy()
                                vida3.destroy()
                                canvasNiveles.destroy()
                                canvasJuego.destroy()
                                top.destroy()

                        # BOTON QUE HACE QUE VUELVA A LA PANTALLA PRINCIPAL
                        btnRegresa = Button(GameOver, text="Volver a Jugar", font=("century", 10),
                                            command=regresaInicio)
                        btnRegresa.place(x=250, y=500)
                        canvasJuego.destroy()
                        btnMenu.destroy()

                        # ----------------------------------------------------- PUNTAJES -------------------------------------------
                        # FUNCION QUE GUARDA LOS MEJORES PUNTAJES
                        def mejoresPuntajes():
                                # CANVAS PUNTAJES
                                puntaje = Canvas(GameOver, width=500, height=250, bg="blue")
                                puntaje.place(x=245, y=300)
                                # FONDO DEL CANVAS
                                fondoPuntajes = Image.open("MejoresPuntajes.jpg")
                                fondoPuntajesRe = fondoPuntajes.resize((500, 250),
                                                                       Image.ANTIALIAS)
                                fondoPuntajesFin = ImageTk.PhotoImage(fondoPuntajesRe,
                                                                      master=puntaje)
                                puntaje.create_image(252, 127, image=fondoPuntajesFin)

                                # LABELS QUE MUESTRAN LOS TRES MEJORES PUNTAJES
                                puntaje1 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje1.place(x=60, y=100)
                                puntaje2 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje2.place(x=225, y=100)
                                puntaje3 = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntaje3.place(x=385, y=100)
                                puntajeExito = Label(puntaje, text="", bg="white", fg="black", font=("century", 10))
                                puntajeExito.place(x=40, y=175)

                                # GUARDA EL TXT EN UNA VARIABLE
                                puntos = open("PuntajeCybertron.txt", 'r')

                                # cant: contador que verifica la cantidad de lineas que hay en el documento txt
                                # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                # lineas: cantidad de lineas que tiene el documento txt
                                global cant, puntajes, lineas
                                lineas = puntos.readlines()
                                puntos.close()
                                cant = 0
                                puntajes = []

                                # pts: lista que almacena los 3 mejores puntajes
                                # i: contador que solo saca los tres primeros puntajes
                                global pts, i
                                pts = []
                                i = 0

                                # Modifica la lista puntajes poniendo como elementos cada una de las lineas del archivo txt
                                def punto():
                                        # cant: contador que verifica la cantidad de lineas que hay en el documento txt
                                        # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                        # lineas: cantidad de lineas que tiene el documento txt
                                        global cant, puntajes
                                        if cant < len(lineas):
                                                puntajes = [[int(lineas[cant].split(",")[0]),
                                                             lineas[cant].split(",")[1]]] + puntajes
                                                cant += 1
                                                # Llamada recursiva que hace que se repita la funcion hasta que cant sea = a la cantidad de elementos en lineas
                                                punto()

                                punto()

                                # FUNCION QUE SACA LOS TRES MEJORES PUNTAJES
                                def tres():
                                        # i: contador que solo saca los tres primeros puntajes
                                        # puntajes: lista que se va creando al modificar la lista inicial quitandole los mejores puntajes
                                        global i, puntajes
                                        if i < 3:
                                                # FUNCION QUE ELIMINA DE LA LISTA EL ELEMENTO INGRESADO
                                                def nuevalista(a, lista, puntajesN):
                                                        global puntajes
                                                        """
                                                           :param a: elemento de la lista puntajes
                                                           :param lista: lista puntajes sin el primer elemento
                                                           :param puntajesN: lista que se crea a partir de la lista puntajes sin el elemento ingresado
                                                           :return: nueva lista que se crea a partir de la lista puntajes sin el elemento ingresado
                                                        """
                                                        if lista == []:
                                                                puntajes = puntajesN
                                                                return puntajesN
                                                        elif lista[0] == a:
                                                                return nuevalista(a, lista[1:], puntajesN)
                                                        else:
                                                                return nuevalista(a, lista[1:], [lista[0]] + puntajesN)

                                                # FUNCION SACA EL MEJOR PUNTAJE DE LA LISTA
                                                def mejores_puntajes(puntaje, lista):
                                                        """
                                                         :param puntaje: elemento de puntaje en la posicion 0
                                                        :param lista: lista puntaje sin el primer elemento
                                                        :return: modifica la lista pts y llama a la funcion nuevalista
                                                        """
                                                        # pts: lista que almacena los 3 mejores puntajes
                                                        global pts
                                                        if len(lista) == 0:
                                                                pts = [puntaje] + pts
                                                                return nuevalista(puntaje, puntajes, [])
                                                        elif puntaje[0] < lista[0][0]:
                                                                return mejores_puntajes(lista[0], lista[1:])
                                                        else:
                                                                return mejores_puntajes(puntaje, lista[1:])

                                                # llama a la funcion
                                                mejores_puntajes(puntajes[0], puntajes)
                                                # cambia el contador
                                                i += 1
                                                # llamada recursicva
                                                tres()
                                        else:
                                                # FUNCION QUE CHEQUEA SI EL PUNTAJE DEL JUGADOR ACTUAL ESTA EN EL TOP 3
                                                def esta(listap, nom, pun):
                                                        if listap == []:
                                                                return False
                                                        elif [pun, nom + "\n"] == listap[0]:
                                                                return True
                                                        else:
                                                                return esta(listap[1:], nom, pun)

                                                # MODIFICA LOS LABELS DE PUNTAJES
                                                puntaje3.configure(text=str(pts[0][1]) + str(
                                                        pts[0][0]) + " pts")
                                                puntaje2.configure(text=str(pts[1][1]) + str(
                                                        pts[1][0]) + " pts")
                                                puntaje1.configure(text=str(pts[2][1]) + str(
                                                        pts[2][0]) + " pts")
                                                if esta(pts, nombre, score):
                                                        puntajeExito.configure(
                                                                text="FELICIDADES ESTAS ENTRE LOS PRIMEROS TRES PUNTAJES !")
                                                else:
                                                        puntajeExito.configure(
                                                                text="NO TE ENCUENTRAS ENTRE LOS PRIMEROS TRES PUNTAJES :(")

                                tres()

                                # FUNCION QUE VUELVE A LA PANTALLA DE FIN DEL JUEGO
                                def regresa():
                                        puntaje.destroy()

                                # BOTON QUE VUELVE A LA PANTALLA DE FIN DEL JUEGO
                                btnPun = Button(puntaje, text="Regresar", font=("century", 10),
                                                command=regresa)
                                btnPun.place(x=410, y=210)

                                # LLAMADA QUE HACE QUE SE EJECUTE LA FUNCION QUE SACA LOS 3 MEJORES PUNTAJES
                                tres()
                                puntaje.lift()

                        # BOTON QUE ABRE LA PANTALLA DE MEJORES PUNTAJES
                        btnmejoresPun = Button(GameOver, text="Puntajes", font=("century", 10),
                                               command=mejoresPuntajes)
                        btnmejoresPun.place(x=650, y=500)

                # FUNCION QUE MUEVE LAS IMAGENES
                def mover_imagen(canvas, aliencito):
                        """
                        :param canvas: canvas donde esta el alien
                        :param aliencito: una de las imagenes de la lista que contiene a todos los aliens
                        :return: los aliens moviendose en el canvas
                        """
                        # total: tiempo transcurrido en la pantalla del juego
                        # a: variable que controla si se mueven o no los aliens
                        global total
                        if total < 100:
                                if a == True:
                                        # FUNCION QUE MODIFICA LA VARIABLE Y EL LABEL DEL TIEMPO
                                        def tiempo():
                                                # counter : variable utilizada para guardar el tiempo de cuando empieza
                                                # menu : variable utilizada para guardar el tiempo de cuando se abre el menu
                                                # total: variable utilizada para guardar la cantidad de tiempo que ha transcurrido
                                                global counter, total, menu
                                                total = (time.time() - menu - counter) // 1  # Modifica la variable total segundo a segundo
                                                tiempoLabel.config(text=str(
                                                        total) + " segundos")  # Modifica el label de tiempo para que este se muestre en pantalla

                                        # Llamada a la funcion que modifica el tiempo
                                        tiempo()
                                        # NAVE DEL ALIEN LLEGA AL BORDE IZQUIERDO --------------------------------------------------------------------------------------------------
                                        # lives: vidas del jugador
                                        global lives
                                        # myX: Velocidad de los aliens
                                        myX = random.randint(-35, 0)
                                        balaA = random.randint(0,30)
                                        # Coordenada donde reaparece el alien
                                        coordY = random.randint(30, 700)
                                        # Hace que el alien se mueva en pantalla
                                        canvas.move(aliencito, myX, 0)
                                        alienCoords = canvas.bbox(aliencito)

                                        def colisionConNaveBalaAlien(balita, balitaCoords):
                                                """
                                                :param alienCoords: Coordenadas del alien
                                                :param aliencito: alien al que pertenecen esas coordenadas
                                                :return: chequea si la nave impacta con un alien
                                                """
                                                # lives: vidas del jugador
                                                global lives
                                                shipCoords = canvasJuego.bbox(myship)
                                                if ((shipCoords[2] > balitaCoords[0] > shipCoords[0]) and shipCoords[1] <
                                                        balitaCoords[3] <  shipCoords[3]):
                                                        canvasJuego.coords(balita, -1, -1)
                                                        global lives
                                                        if lives == 3:
                                                                lives = lives - 1
                                                                vida3.destroy()
                                                        elif lives == 2:
                                                                lives = lives - 1
                                                                vida2.destroy()
                                                        elif lives == 1:
                                                                lives = lives - 1
                                                                vida1.destroy()
                                                        else:
                                                                lives = lives - 1
                                                                # muestra la pantalla final
                                                                final()
                                                                canvasJuego.destroy()
                                                                btnMenu.destroy()

                                        def pewAlien(balitas):
                                                """
                                                :param balitas: bala que se creo
                                                :return: bala moviendose si no se sale de pantalla, elimina bala si se sale de pantalla
                                                """
                                                global listaBalaA
                                                balitaCoords = canvasJuego.bbox(balitas)
                                                # mueve la bala
                                                canvasJuego.move(balitas, -10, 0)
                                                # chequea si colisiona con la nave del jugador
                                                colisionConNaveBalaAlien(balitas, balitaCoords)
                                                # Repite la funcion mover cada 80 milisegundos
                                                root.after(150, pewAlien, balitas)

                                        if balaA < 1:
                                                global listaBalaA
                                                # crea la bala donde esta el alien
                                                balitasA = canvasJuego.create_image(alienCoords[0], (
                                                        alienCoords[1] + alienCoords[3]) // 2,
                                                                                   image=balasReAlien)
                                                listaBalaA += [balitasA]
                                                # llama a la funcion pew que mueve la bala
                                                pewAlien(balitasA)



                                        # Chequea si el alien se sali[o de la pantalla y baja una vida si lo hizo
                                        if alienCoords[0] < 0:
                                                canvasJuego.coords(aliencito, 1000, coordY)
                                                if lives == 3:
                                                        lives = lives - 1
                                                        vida3.destroy()
                                                elif lives == 2:
                                                        lives = lives - 1
                                                        vida2.destroy()
                                                elif lives == 1:
                                                        lives = lives - 1
                                                        vida1.destroy()
                                                else:
                                                        lives = lives - 1
                                                        # si ya no quedan vidas se va a la pantalla de fin del juego
                                                        final()

                                        # FUNCION CREA LAS BALAS Y LAS MUEVE ----------------------------------------------------------------------------
                                        def moverBala(event):
                                                """
                                                :param event: Se preciona la barra espaciadora
                                                :return: lanza una bala
                                                """

                                                # variable que pone el juego en pausa
                                                if a == True:
                                                        shipCoords = canvasJuego.bbox(myship)
                                                        # crea la bala donde esta la nave del jugador
                                                        balitas = canvasJuego.create_image(shipCoords[2], (
                                                                        shipCoords[1] + shipCoords[3]) // 2,
                                                                                           image=balasReNave)
                                                        # llama a la funcion pew que mueve la bala
                                                        pew(balitas)

                                        # FUNCION QUE MUEVE LA BALA
                                        def pew(balitas):
                                                global listaBalaA
                                                """
                                                :param balitas: bala que se creo en la funcion moverBala
                                                :return: bala moviendose si no se sale de pantalla, elimina bala si se sale de pantalla
                                                """
                                                balitaCoords = canvasJuego.bbox(balitas)
                                                # mueve la bala
                                                canvasJuego.move(balitas, 25, 0)
                                                # chequea si la bala colisiono contra un alien
                                                chequea(balitas, objetos_imagenes, 0)
                                                # Repite la funcion mover cada 80 milisegundos
                                                if balitaCoords[2] < 1000:
                                                        # chequea si la bala colisiono contra la bala del alien
                                                        chequeaA(balitas, listaBalaA, 0)
                                                        root.after(80, pew, balitas)
                                                else:
                                                        canvasJuego.delete(balitas)

                                        # CONTROL PARA DISPARAR BALAS
                                        canvasJuego.bind_all("<space>", moverBala)
                                        # FUNCION QUE CHEQUEA SI COLISIONA UN ALIEN CON LA NAVE
                                        colisionConNave(alienCoords, aliencito)
                        else:
                                # LLAMA A FUNCION QUE MUESTRA PANTALLA FINAL
                                final()

                # FUNCION QUE CHEQUEA COLISION CON LA NAVE
                def colisionConNave(alienCoords, aliencito):
                        """
                        :param alienCoords: Coordenadas del alien
                        :param aliencito: alien al que pertenecen esas coordenadas
                        :return: chequea si la nave impacta con un alien
                        """
                        # lives: vidas del jugador
                        global lives
                        shipCoords = canvasJuego.bbox(myship)
                        coordY = random.randint(50, 550)
                        if ((shipCoords[2] > alienCoords[0] > shipCoords[0]) and shipCoords[1] < alienCoords[3] <
                                shipCoords[3]):
                                canvasJuego.coords(aliencito, 1000, coordY)
                                global lives
                                if lives == 3:
                                        lives = lives - 1
                                        vida3.destroy()
                                elif lives == 2:
                                        lives = lives - 1
                                        vida2.destroy()
                                elif lives == 1:
                                        lives = lives - 1
                                        vida1.destroy()
                                else:
                                        lives = lives - 1
                                        # muestra la pantalla final
                                        final()
                                        canvasJuego.destroy()
                                        btnMenu.destroy()

                def chequeaA(balitas,listaBalaA,i):
                        """
                                                :param balitas: bala que se va a chequear
                                                :param listaBalaA: la lista que contiene las imagenes
                                                :param i: parametro que se asegura que se chequen todas las imagenes
                                                """

                        if i < len(listaBalaA):
                                        # FUNCION QUE VERIFICA SI LAS BALAS CHOCAN CON UN ALIEN
                                        colisionaBalayBala(balitas, listaBalaA, i)
                                        # LLAMADA RECURSIVA CAMBIANDOLE EL INDICE
                                        chequeaA(balitas, listaBalaA, i + 1)

                def colisionaBalayBala(balitas, listaBalaA, i):
                        """
                        :param balitas: bala que se va a chequear
                        :param listaBalaA: lista que contiene a todos los balas lanzadas por la nave
                        :param i: indica el indice de la lista que se va a chequear
                        """
                        balitaNaveCoords = canvasJuego.bbox(balitas)
                        coordY = random.randint(50, 500)
                        balitaAlienCoords = canvasJuego.bbox(listaBalaA[i])
                        print(balitaNaveCoords)
                        if ((balitaAlienCoords[2] > balitaNaveCoords[0] > balitaAlienCoords[0]) and balitaAlienCoords[1] < balitaNaveCoords[3] <
                                balitaAlienCoords[3]):
                                canvasJuego.coords(listaBalaA[i], 1005, coordY)
                                canvasJuego.coords(balitas, 1100, 1000)

                # FUNCION QUE CHEQUEA SI LAS BALAS COLISIONARON CON UN ALIEN
                def chequea(balitas, objetos_imagenes, i):
                        """
                        :param balitas: bala que se va a chequear
                        :param objetos_imagenes: la lista que contiene las imagenes
                        :param i: parametro que se asegura que se chequen todas las imagenes
                        """
                        if i < len(objetos_imagenes):
                                # FUNCION QUE VERIFICA SI LAS BALAS CHOCAN CON UN ALIEN
                                colisiona(balitas, objetos_imagenes, i)
                                # LLAMADA RECURSIVA CAMBIANDOLE EL INDICE
                                chequea(balitas, objetos_imagenes, i + 1)


                # VERIFICA SI LAS BALAS CHOCAN CON UN ALIEN
                def colisiona(balitas, objetos_imagenes, i):
                        """
                        :param balitas: bala que se va a chequear
                        :param objetos_imagenes: lista que contiene a todos los aliens
                        :param i: indica el indice de la lista que se va a chequear
                        """
                        # score: contiene el puntaje de la persona
                        global score
                        balitaCoords = canvasJuego.bbox(balitas)
                        coordY = random.randint(50, 500)
                        alienCoords = canvasJuego.bbox(objetos_imagenes[i])
                        if ((alienCoords[2] > balitaCoords[0] > alienCoords[0]) and alienCoords[1] < balitaCoords[3] <
                                alienCoords[3]):
                                score = score + 2 ** len(objetos_imagenes)
                                scoreLabel.configure(text=str(score) + " pts")
                                canvasJuego.coords(objetos_imagenes[i], 1005, coordY)
                                canvasJuego.coords(balitas, 1100, 1000)

                # FUNCION QUE LLAMA A LA FUNCION PARA MOVER UNA IMAGEN PARA QUE RECURSIVAMENTE MUEVA VARIAS IMAGENES
                def mover_varias_imagenes(canvas, objetos_imagenes, i):
                        """
                        :param canvas: indica el canvas donde va a aparecer las imagenes
                        :param objetos_imagenes: lista donde estan almacenados todos los aliens en pantalla
                        :param i: contador que verifica que no se salga la funcion de la cantidad de elementos en la lista
                        """
                        if i < len(objetos_imagenes):
                                # LLamada a funcion mover una imagen, le envia el canvas y una de las imagenes de los aliens en la lista
                                mover_imagen(canvas, objetos_imagenes[i])
                                # LLamada recursiva, se acaba cuando se recorran todas las imagenes de la lista
                                mover_varias_imagenes(canvas, objetos_imagenes, i + 1)

                # FUNCION PARA ANIMAR A LAS IMAGENES
                def animar():
                        # total: variable que almacena el tiempo
                        # llamada a la funcion mover vairias imagenes
                        mover_varias_imagenes(canvasJuego, objetos_imagenes, 0)
                        if total < 100:
                                # LLAMADA RECURSIVA
                                root.after(400, animar)

                # ACTIVA LA FUNCION QUE ANIMA LAS IMAGENES
                animar()

                # MOVIMIENTOS NAVE, VERIFICAN QUE NO SE SALGA LA NAVE DE LA PANTALLA
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

                myship.lift()

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
