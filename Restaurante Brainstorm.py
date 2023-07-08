from tkinter import *
import psycopg2
import random
import time
from tkinter import filedialog,messagebox

def salidaPrincipal():
    ventana.destroy()

Title = ("arial black", 25)
Subtitle = ("Cambria", 12)

ventana = Tk()
ventana.geometry("800x700")
ventana.title("RESTAURANTE")
ventana.config(bg="#FF9933")

marcoPrincipal = Frame(ventana, bd="10", relief=RIDGE, bg="#FF9933")
marcoPrincipal.pack(side=TOP)

tituloPrincipal = Label(marcoPrincipal, text="Restaurante BrainStorm", font=Title, fg="#202020", bg="#FF9933")
tituloPrincipal.pack()

subPrincipal = Label(marcoPrincipal, bd=5, text="BIENVENIDOS", font=Subtitle, fg="#202020", bg="#FF9933")
subPrincipal.pack()

#Diesño de ventana primer ventana secundaria
def ventanaReserva():
    ventana_reserva = Toplevel()
    ventana_reserva.title("Datos en PostgreSQL")
    ventana_reserva.geometry("600x600")
    ventana_reserva.config(bg="#202020")
    main_title = Label(ventana_reserva, text="Registro para reserva",
                       font=Subtitle, bg="#FF9933",
                       fg="white")
    main_title.pack()

    def guardar_nueva_reserva(nombre, cantidad, contacto):
        #print(nombre) #print(cantidad) #print(contacto)
        conn = psycopg2.connpect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='postgres')
        cursor = conn.cursor()
        query = '''INSERT INTO reservas(nombre, cantidad, contacto) VALUES (%s, %s, %s)'''
        cursor.execute(query, (nombre, cantidad, contacto))
        print("Datos guardados")
        conn.commit()
        conn.close()
            
        entry_nombre.delete(0, END)
        entry_cantidad.delete(0, END)
        entry_contacto.delete(0, END)
        #mostrar_reservas()


    def mostrar_reservas():
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='postgres')
        cursor = conn.cursor()
        query = '''SELECT * FROM reservas'''
        cursor.execute(query)

        row = cursor.fetchall()

        listbox = Listbox(frame, width=30, height=5)
        listbox.grid(row=12, columnspan=4, sticky=W+E)

        for x in row:
            listbox.insert(END, x)

        print(row)

        conn.commit()
        conn.close()

    def buscar(id):
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='reservaciones')
        cursor = conn.cursor()
        query = '''SELECT * FROM reservas WHERE id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()

        messagebox.showinfo("Informacion", message=row)
        print(row)

        conn.commit()
        conn.close()

        id_buscar.delete(0, END)

    def mostrar():
        mostrar_reservas()

    def eliminar(id):
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='reservaciones')
        cursor = conn.cursor()
        query = '''DELETE FROM reservas WHERE id={} RETURNING *'''.format(id)
        cursor.execute(query, (id))

        var = cursor.fetchone()

        messagebox.showinfo("Informacion", message=var)
        print(var)

        conn.commit()
        conn.close()

        id_eliminar.delete(0, END)
    
##########################################################
#Parte 2 Jimena Mansilla
    frame = Frame(ventana_reserva, bd="2", relief=RIDGE, bg="#FF9933")
    frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    label = Label(frame, width="17",height="1", bg="#FF9933",
                  font=Subtitle, text="AGREGAR REGISTRO")
    label.grid(row=0, column=1)

    label = Label(frame, width="15",height="1", bg="gray", fg="white",
                  font=Subtitle, text="Nombre")
    label.grid(row=1, column=0)

    entry_nombre = Entry(frame)
    entry_nombre.grid(row=1, column=1)

    #
    label = Label(frame, width="15",height="1", bg="gray", fg="white",
                  font=Subtitle, text="Cantidad Personas")
    label.grid(row=3, column=0)

    entry_cantidad = Entry(frame)
    entry_cantidad.grid(row=3, column=1)

    #
    label = Label(frame, width="15",height="1", bg="gray", fg="white",
                  font=Subtitle, text="Contacto")
    label.grid(row=6, column=0)

    entry_contacto = Entry(frame)
    entry_contacto.grid(row=6, column=1)

    button = Button(frame, font=Subtitle, text="Add", bg="#202020", fg="white"
                    ,command=lambda:guardar_nueva_reserva(entry_nombre.get(),
                                                        entry_cantidad.get(),
                                                        entry_contacto.get()))
    button.grid(row=7, column=1, sticky=W+E)

    # Buscar reserva
    label = Label(frame, width="14",height="1", bg="gray", fg="white",
                  font=Subtitle, text="Busqueda")
    label.grid(row=9, column=0)

    id_buscar = Entry(frame)
    id_buscar.grid(row=9, column=1)

    boton = Button(frame, font=Subtitle, text="Buscar",width="10",height="1",
                   bg="#202020", fg="white",
                   command=lambda:buscar(id_buscar.get()))
    boton.grid(row=9, column=2)

    label = Label(frame, width="14",height="1", bg="gray", fg="white",
                  font=Subtitle,text="Busqueda por id")
    label.grid(row=10, column=0)

    id_eliminar = Entry(frame)
    id_eliminar.grid(row=10, column=1)

    boton_eliminar = Button(frame, font=Subtitle, text="Eliminar",width="10",height="1",
                            bg="#202020", fg="white",
                            command=lambda:eliminar(id_eliminar.get()))
    boton_eliminar.grid(row=10, column=2)

    boton_mostrar = Button(frame, font=Subtitle, text="Mostrar reservas",width="16",height="1",
                           bg="#202020", fg="white",
                           command=mostrar)
    boton_mostrar.grid(row=11,column=1)

    #mostrar_reservas()
    # Fin de Reserva

# Boton de ingreso a ventana Reservas
boton_reservas = Button(ventana, font=Subtitle, text="Reservas",command=ventanaReserva,width="20",height="2")
boton_reservas.config(bd=2, bg="#202020", fg="white")
boton_reservas.pack()
boton_reservas.place(x=200, y=200)
##############################
##############################

def menu():
    ventanaMenu = Toplevel()
    ventanaMenu.config(bg="#202020")
    ventanaMenu.title("Menu")
    ventanaMenu.geometry("1260x650")

    def texto():
        textoText.delete(1.0, END)
        x = random.randint(1, 10000)
        noText = "No" + str(x)
        fecha = time.strftime("%d-%m-%y")
        textoText.insert(END, "Ayuda.." + noText + "\t\t\t\t Fecha:" + fecha + "\n")
        textoText.insert(END, "********************************************************\n")
        textoText.insert(END, "Instrucciones \t\t\t Para ordenar usted debe:\n")
        textoText.insert(END, "¡BIENVENIDO! "+ "\n")
        textoText.insert(END, "Haga click sobre el check para desbloquear la funcion y "+"\n" +
                         "digitar las unidades que desea consumir")
        textoText.insert(END, "*******************************************************\n\n")
        textoText.insert(END, "Le deseamos la mejor de las experiencias \t\t\t"+ "\n")

    def guardar():
        url=filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        datos_recibo=textoText.get(1.0, END)
        url.write(datos_recibo)
        url.close()
        messagebox.showinfo("Informacion", message="Instrucciones almacenada con exito")

    def borrar():
        textoText.delete(1.0, END)
        #Variables para textos: Comida
        txtAsado.set("0")
        txtMilanesa.set("0")
        txtPure.set("0")
        txtEnsalada.set("0")
        txtPapas.set("0")
        txtPollo.set("0")
        txtPastas.set("0")
        txtArroz.set("0")
        txtPizza.set("0")

        # Variables para textos: Bebidas
        txtPepsi.set("0")
        txtCoca.set("0")
        txtFanta.set("0")
        txtSprite.set("0")
        txtAguaS.set("0")
        txtAgua.set("0")
        txtAndes.set("0")
        txtQuilmes.set("0")
        txtVino.set("0")

        # Desactivar casillas de textos
        textAsado.config(state=DISABLED)
        textMilanesa.config(state=DISABLED)
        textPure.config(state=DISABLED)
        textEnsalada.config(state=DISABLED)
        textPapas.config(state=DISABLED)
        textPollo.config(state=DISABLED)
        textPastas.config(state=DISABLED)
        textArroz.config(state=DISABLED)
        textPizza.config(state=DISABLED)

        # Bebidas
        textPepsi.config(state=DISABLED)
        textPepsi.config(state=DISABLED)
        textFanta.config(state=DISABLED)
        textSprite.config(state=DISABLED)
        textAguaS.config(state=DISABLED)
        textAgua.config(state=DISABLED)
        textAndes.config(state=DISABLED)
        textQuilmes.config(state=DISABLED)
        textVino.config(state=DISABLED)

        # Variables
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)

        global varcostocomida, varcostobebidas, total
        varcostocomida=0
        varcostobebidas=0
        total=0

        entryCostoComida.config(state=NORMAL)
        entryCostoComida.delete(0, END)
        entryCostoComida.insert(0, varcostocomida)
        entryCostoComida.config(state=DISABLED)

        entryCostoBebidas.config(state=NORMAL)
        entryCostoBebidas.delete(0, END)
        entryCostoBebidas.insert(0, varcostobebidas)
        entryCostoBebidas.config(state=DISABLED)

        entryTotal.config(state=NORMAL)
        entryTotal.delete(0, END)
        entryTotal.insert(0, total)
        entryTotal.config(state=DISABLED)

    def salirMenu():
        ventanaMenu.destroy()

#Funcion
    def totalFinal():
        global varcostocomida, varcostobebidas, total
##########################################################
#Perte 3 Giunta Pilar
# Definimos los Valores de la comida 
        t_asado = int(textAsado.get()) 
        t_milanesa = int(textMilanesa.get())
        t_pure = int(textPure.get())
        t_ensalada = int(textEnsalada.get())
        t_papas = int(textPapas.get())
        t_pollo = int(textPollo.get())
        t_pastas = int(textPastas.get())
        t_arroz = int(textArroz.get())
        t_pizza = int(textPizza.get())
        varcostocomida = (t_asado * 1000) + (t_milanesa * 700) + (t_pure * 500) + (t_ensalada * 750) + (t_papas * 1500) + (t_pollo * 800) + (t_pastas * 1100) + (t_arroz * 600) + (t_pizza * 1500)
        entryCostoComida.config(state=NORMAL)
        entryCostoComida.delete(0, END)
        entryCostoComida.insert(0, varcostocomida)
        entryCostoComida.config(state=DISABLED)

        #Valores: Bebidas
        t_pepsi = int(textPepsi.get())
        t_coca = int(textCocaCola.get())
        t_fanta = int(textFanta.get())
        t_sprite = int(textSprite.get())
        t_aguaS = int(textAguaS.get())
        t_agua = int(textAgua.get())
        t_andes = int(textAndes.get())
        t_quilmes = int(textQuilmes.get())
        t_vino = int(textVino.get())
        varcostobebidas = (t_pepsi * 600) + (t_coca * 600) + (t_fanta * 600) + (t_sprite * 600) + (t_aguaS * 500) + (
                    t_agua * 500) + (t_andes * 800) + (t_quilmes * 800) + (t_vino * 800)
        entryCostoBebidas.config(state=NORMAL)
        entryCostoBebidas.delete(0, END)
        entryCostoBebidas.insert(0, varcostobebidas)
        entryCostoBebidas.config(state=DISABLED)

        total = varcostocomida + varcostobebidas
        entryTotal.config(state=NORMAL)
        entryTotal.delete(0, END)
        entryTotal.insert(0, total)
        entryTotal.config(state=DISABLED)

    #Funcion: activar y desactivar checkbutton
    def asado(): 
        if var1.get() == 1:
            textAsado.config(state=NORMAL)
            textAsado.delete(0, END)
            textAsado.focus()
        else: #desabilitado para escribir
            textAsado.config(state=DISABLED)
            txtAsado.set("0")

    def milanesa():
        if var2.get() == 1:
            textMilanesa.config(state=NORMAL)
            textMilanesa.delete(0, END)
            textMilanesa.focus()
        else:
            textMilanesa.config(state=DISABLED)
            txtMilanesa.set("0")

    def pure():
        if var3.get() == 1:
            textPure.config(state=NORMAL)
            textPure.delete(0, END)
            textPure.focus()
        else:
            textPure.config(state=DISABLED)
            txtPure.set("0")

    def ensalada():
        if var4.get() == 1:
            textEnsalada.config(state=NORMAL)
            textEnsalada.delete(0, END)
            textEnsalada.focus()
        else:
            textEnsalada.config(state=DISABLED)
            txtEnsalada.set("0")

    def papas():
        if var5.get() == 1:
            textPapas.config(state=NORMAL)
            textPapas.delete(0, END)
            textPapas.focus()
        else:
            textPapas.config(state=DISABLED)
            txtPapas.set("0")
#########################################################################
