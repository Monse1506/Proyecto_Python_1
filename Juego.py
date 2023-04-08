from tkinter import *
from PIL import ImageTk, Image

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
        canvasSobre = Canvas(framePrin, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="green")
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





root.mainloop()
