from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import datetime, timedelta

class app:
    db = 'database.db'

    def __init__(self, ventana):
        # Creación de la ventana
        self.ventana = ventana
        self.ventana.title("Control de Cuentas")
        self.ventana.geometry("1360x679+0+0")
        self.ventana.resizable(False,False)

        # Titulo en ventana
        Label(self.ventana, text="ADMINISTRADOR DE CUENTAS", bd=10, font=("Arial",30,"bold"), fg="black").pack(side=TOP)

        # Variables
        self.IdVar = StringVar()
        self.NombreVar = StringVar()
        self.ApellidoVar = StringVar()
        self.PaisVar = StringVar()
        self.NacimientoVar = StringVar()
        self.EmailVar = StringVar()
        self.ContraUnoVar = StringVar()
        self.TelefonoVar = StringVar()
        self.ContraDosVar = StringVar()
        self.CreacionVar = StringVar()

        # Apartado para el ingreso de datos
        FrameGestion = Frame(self.ventana, bd=4, bg="lavender")
        FrameGestion.place(x=10, y=68, width=520, height=600)

        # Titulo para el apartado de ingreso de datos
        Label(FrameGestion, text="REGISTRAR  NUEVO  USUARIO", bg="lavender", fg="black", font=("Arial",20,"bold")).grid(row=0, columnspan=2, pady=20)

        #---Nombre
        Label(FrameGestion, text="Nombre:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=1, column=0, pady=10, padx=20, sticky="E",)
        NombreTexto = Entry(FrameGestion, textvariable=self.NombreVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        NombreTexto.focus()
        NombreTexto.grid(row=1, column=1, pady=10, sticky="W")
        #---Apellido
        Label(FrameGestion, text="Apellido:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=2, column=0, pady=10, padx=20, sticky="E",)
        ApellidoTexto = Entry(FrameGestion, textvariable=self.ApellidoVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        ApellidoTexto.grid(row=2, column=1, pady=10, sticky="W")
        #---País
        Label(FrameGestion, text="País:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=3, column=0, pady=10, padx=20, sticky="E",)
        PaisTexto = Entry(FrameGestion, textvariable=self.PaisVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        PaisTexto.grid(row=3, column=1, pady=10, sticky="W")
        #---Fecha de nacimiento
        Label(FrameGestion, text="Nacimiento:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=4, column=0, pady=10, padx=20, sticky="E",)
        NacimientoTexto = Entry(FrameGestion, textvariable=self.NacimientoVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        NacimientoTexto.grid(row=4, column=1, pady=10, sticky="W")
        #---Email
        Label(FrameGestion, text="Email:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=5, column=0, pady=10, padx=20, sticky="E",)
        EmailTexto = Entry(FrameGestion, textvariable=self.EmailVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        EmailTexto.grid(row=5, column=1, pady=10, sticky="W")
        #---Contraseña I
        Label(FrameGestion, text="Contraseña I:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=6, column=0, pady=10, padx=20, sticky="E",)
        ContraUnoTexto = Entry(FrameGestion, textvariable=self.ContraUnoVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        ContraUnoTexto.grid(row=6, column=1, pady=10, sticky="W")
        #---Telefono
        Label(FrameGestion, text="Teléfono:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=7, column=0, pady=10, padx=20, sticky="E",)
        TelefonoTexto = Entry(FrameGestion, textvariable=self.TelefonoVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        TelefonoTexto.grid(row=7, column=1, pady=10, sticky="W")
        #---Contraseña II
        Label(FrameGestion, text="Contraseña II:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=8, column=0, pady=10, padx=20, sticky="E",)
        ContraDosTexto = Entry(FrameGestion, textvariable=self.ContraDosVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        ContraDosTexto.grid(row=8, column=1, pady=10, sticky="W")
        #---Fecha de creación
        Label(FrameGestion, text="Creación:", bg="lavender", fg="black", font=("Arial",15,"bold")).grid(row=9, column=0, pady=10, padx=20, sticky="E",)
        CreacionTexto = Entry(FrameGestion, textvariable=self.CreacionVar, font=("Arial",12), bd=5, relief=GROOVE, width=33)
        CreacionTexto.grid(row=9, column=1, pady=10, sticky="W")

        # Botones del apartado para el ingreso de datos
        FrameBoton = Frame(FrameGestion, bd=4, bg="lavender")
        FrameBoton.place(x=68, y=536, width=368)
        #---Boton Agregar
        Button(FrameBoton, text="Agregar", width=10, command=self.agregar_registro).grid(row=0, column=0, pady=10, padx=20)
        #---Boton Actualizar
        Button(FrameBoton, text="Actualizar", width=10, command=self.actualizar_registro).grid(row=0, column=1, pady=10, padx=20)
        #---Boton Borrar
        Button(FrameBoton, text="Borrar", width=10, command=self.eliminar_registro).grid(row=0, column=2, pady=10, padx=20)

        # Apartado para la vista de datos
        FrameDetalle = Frame(self.ventana, bd=4, bg="lavender")
        FrameDetalle.place(x=539, y=68, width=811, height=600)

        # Boton Perfil
        Button(FrameDetalle, text="Perfil", width=10, command=self.ventana_perfil).grid(row=0, column=0, pady=1, padx=20)

        # Mensajes
        self.mensaje = Label(FrameDetalle, text='', bg="lavender", fg="red", font=("Arial",12,"bold"))
        self.mensaje.grid(row=0, column=1, columnspan=2, pady=1, padx=10)

        # Tabla
        FrameTabla = Frame(FrameDetalle, bd=4, relief=RIDGE)
        FrameTabla.place(x=10, y=30, width=783, height=553)

        scrollX = Scrollbar(FrameTabla, orient=HORIZONTAL)
        scrollY = Scrollbar(FrameTabla, orient=VERTICAL)

        self.TablaRegistros = ttk.Treeview(FrameTabla, columns=('#1','#2','#3','#4','#5','#6','#7','#8','#9'), xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.TablaRegistros.xview)
        scrollY.config(command=self.TablaRegistros.yview)
        self.TablaRegistros.column('#0', width=100)
        self.TablaRegistros.heading('#0', text="Id", anchor=CENTER)
        self.TablaRegistros.column('#1', width=150)
        self.TablaRegistros.heading('#1', text="Nombre", anchor=CENTER)
        self.TablaRegistros.column('#2', width=150)
        self.TablaRegistros.heading('#2', text="Apellido", anchor=CENTER)
        self.TablaRegistros.column('#3', width=150)
        self.TablaRegistros.heading('#3', text="País", anchor=CENTER)
        self.TablaRegistros.heading('#4', text="Nacimiento", anchor=CENTER)
        self.TablaRegistros.column('#5', width=300)
        self.TablaRegistros.heading('#5', text="Email", anchor=CENTER)
        self.TablaRegistros.column('#6', width=150)
        self.TablaRegistros.heading('#6', text="Contraseña I", anchor=CENTER)
        self.TablaRegistros.heading('#7', text="Teléfono", anchor=CENTER)
        self.TablaRegistros.column('#8', width=150)
        self.TablaRegistros.heading('#8', text="Contraseña II", anchor=CENTER)
        self.TablaRegistros.heading('#9', text="Creación", anchor=CENTER)
        self.TablaRegistros.pack(fill=BOTH, expand=1)
        self.TablaRegistros.bind("<ButtonRelease-1>", self.obtener_click)
        self.mostrar_registros()

    def validacion(self):
        return len(self.NombreVar.get()) != 0 and len(self.ApellidoVar.get()) != 0 and len(self.PaisVar.get()) != 0 and len(self.NacimientoVar.get()) != 0 and len(
            self.EmailVar.get()) != 0 and len(self.ContraUnoVar.get()) != 0 and len(self.TelefonoVar.get()) != 0 and len(self.ContraDosVar.get()) != 0 and len(self.CreacionVar.get()) != 0

    def ejecutar_query(self, query, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(query, parametros)
            con.commit()
        return resultado

    def mostrar_registros(self):
        registros = self.TablaRegistros.get_children()
        for elemento in registros:
            self.TablaRegistros.delete(elemento)
        query = 'SELECT * FROM CUENTA ORDER BY ID DESC'
        FilasTabla = self.ejecutar_query(query)
        for row in FilasTabla:
            self.TablaRegistros.insert('', 0, text=row[0], values=row[1:])

    def agregar_registro(self):
        if self.validacion():
            query = 'INSERT INTO CUENTA VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            parametros = (self.NombreVar.get(),
            self.ApellidoVar.get(),
            self.PaisVar.get(),
            self.NacimientoVar.get(),
            self.EmailVar.get(),
            self.ContraUnoVar.get(),
            self.TelefonoVar.get(),
            self.ContraDosVar.get(),
            self.CreacionVar.get())
            self.ejecutar_query(query, parametros)
            self.mensaje['text'] = "La identidad {} ha sido ingresada".format(self.NombreVar.get())
            self.mostrar_registros()
            self.limpiar_campos()
        else:
            self.mensaje['text'] = "Datos requeridos"
        self.mostrar_registros()

    def limpiar_campos(self):
        self.IdVar.set("")
        self.NombreVar.set("")
        self.ApellidoVar.set("")
        self.PaisVar.set("")
        self.NacimientoVar.set("")
        self.EmailVar.set("")
        self.ContraUnoVar.set("")
        self.TelefonoVar.set("")
        self.ContraDosVar.set("")
        self.CreacionVar.set("")

    def obtener_click(self, evento):
        CursorFila = self.TablaRegistros.focus()
        contenido = self.TablaRegistros.item(CursorFila)
        row = contenido['values']
        self.NombreVar.set(row[0])
        self.ApellidoVar.set(row[1])
        self.PaisVar.set(row[2])
        self.NacimientoVar.set(row[3])
        self.EmailVar.set(row[4])
        self.ContraUnoVar.set(row[5])
        self.TelefonoVar.set(row[6])
        self.ContraDosVar.set(row[7])
        self.CreacionVar.set(row[8])

    def actualizar_registro(self):
        self.mensaje['text'] = ''
        if self.validacion():
            OldNombre = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][0]
            OldApellido = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][1]
            OldPais = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][2]
            OldNacimiento = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][3]
            OldEmail = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][4]
            OldContraUno = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][5]
            OldTelefono = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][6]
            OldContraDos = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][7]
            OldCreacion = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][8]
            query = 'UPDATE CUENTA SET nombre=?, apellido=?, pais=?, nacimiento=?, email=?, contraUno=?, telefono=?, contraDos=?, creacion=? WHERE nombre= ? AND apellido=? AND pais=? AND nacimiento=? AND email=? AND contraUno=? AND telefono=? AND contraDos=? AND creacion=?'
            parametros = (self.NombreVar.get(),
            self.ApellidoVar.get(),
            self.PaisVar.get(),
            self.NacimientoVar.get(),
            self.EmailVar.get(),
            self.ContraUnoVar.get(),
            self.TelefonoVar.get(),
            self.ContraDosVar.get(),
            self.CreacionVar.get(),
            OldNombre,
            OldApellido,
            OldPais,
            OldNacimiento,
            OldEmail,
            OldContraUno,
            OldTelefono,
            OldContraDos,
            OldCreacion)
            self.ejecutar_query(query, parametros)
            self.mensaje['text'] = "La identidad {} ha sido actualizada".format(self.NombreVar.get())
            self.mostrar_registros()
            self.limpiar_campos()
        else:
            self.mensaje['text'] = "Selecciona un registro"

    def eliminar_registro(self):
        self.mensaje['text'] = ''
        if self.validacion():
            IdRegistro = self.TablaRegistros.item(self.TablaRegistros.selection())['text']
            query = 'DELETE FROM CUENTA WHERE id = ?'
            self.ejecutar_query(query, (IdRegistro, ))
            self.mostrar_registros()
            self.limpiar_campos()
            self.mensaje['text'] = "La identidad {} ha sido eliminada".format(self.NombreVar.get())
        else:
            self.mensaje['text'] = "Selecciona un registro"

    def ventana_perfil(self):
        if self.validacion():
            VerId = self.TablaRegistros.item(self.TablaRegistros.selection())['text']
            VerNombre = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][0]
            VerApellido = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][1]
            VerPais = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][2]
            VerNacimiento = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][3]
            VerEmail = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][4]
            VerContraUno = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][5]
            VerTelefono = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][6]
            VerContraDos = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][7]
            VerCreacion = self.TablaRegistros.item(self.TablaRegistros.selection())['values'][8]

            # Conversion de fecha
            FechaAcutual = datetime.today()
            ConvertirFecha = datetime.strptime(VerCreacion, '%d/%m/%Y')

            # Tiempo transcurrido
            dias = (FechaAcutual - ConvertirFecha).days
            meses = int(dias/30)
            anios = int(meses/365)

            self.limpiar_campos()
            self.PerfilVentana = Toplevel()
            self.PerfilVentana.geometry("937x590+10+10")
            self.PerfilVentana.title("Perfil")
            self.PerfilVentana.resizable(False,False)
        else:
            self.mensaje['text'] = "Selecciona un registro"

        # Titulo de ventana Perfil
        Label(self.PerfilVentana, text="INFORMACIÓN", bd=10, font=("Arial",30,"bold"), fg="black").pack(side=TOP)

        # Apartado para la lectura de datos
        FramePerfil = Frame(self.PerfilVentana, bd=4)
        FramePerfil.place(x=10, y=68, width=917, height=512)

        #---Ver Id
        Label(FramePerfil, text="Id:", fg="black", font=("Arial",15,"bold")).grid(row=1, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerId), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=1, column=1, pady=10, sticky="W")
        #---Ver Nombre
        Label(FramePerfil, text="Nombre:", fg="black", font=("Arial",15,"bold")).grid(row=2, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerNombre), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=2, column=1, pady=10, sticky="W")
        #---Ver Apellido
        Label(FramePerfil, text="Apellido:", fg="black", font=("Arial",15,"bold")).grid(row=3, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerApellido), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=3, column=1, pady=10, sticky="W")
        #---Ver País
        Label(FramePerfil, text="País:", fg="black", font=("Arial",15,"bold")).grid(row=4, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerPais), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=4, column=1, pady=10, sticky="W")
        #---Ver Nacimiento
        Label(FramePerfil, text="Nacimiento:", fg="black", font=("Arial",15,"bold")).grid(row=5, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerNacimiento), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=5, column=1, pady=10, sticky="W")
        #---Ver Email
        Label(FramePerfil, text="Email:", fg="black", font=("Arial",15,"bold")).grid(row=6, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerEmail), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=6, column=1, pady=10, sticky="W")
        #---Ver Contra I
        Label(FramePerfil, text="Contra I:", fg="black", font=("Arial",15,"bold")).grid(row=7, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerContraUno), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=7, column=1, pady=10, sticky="W")
        #---Ver Telefono
        Label(FramePerfil, text="Teléfono:", fg="black", font=("Arial",15,"bold")).grid(row=8, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerTelefono), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=8, column=1, pady=10, sticky="W")
        #---Ver Contra II
        Label(FramePerfil, text="Contra II:", fg="black", font=("Arial",15,"bold")).grid(row=9, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerContraDos), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=9, column=1, pady=10, sticky="W")
        #---Ver Creación
        Label(FramePerfil, text="Creación:", fg="black", font=("Arial",15,"bold")).grid(row=10, column=0, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=VerCreacion), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=10, column=1, pady=10, sticky="W")

        # Apartado para la visualización de tiempo activo
        FrameTiempo = Frame(FramePerfil, bd=4)
        FrameTiempo.place(x=480, y=0, width=440, height=200)

        # Titulo para apartado de tiempo transcurrido
        Label(FrameTiempo, text="TIEMPO ACTIVO", fg="black", font=("Arial",18,"bold")).pack(side=TOP)

        #---Ver Días
        Label(FramePerfil, text="Días:", fg="black", font=("Arial",15,"bold")).grid(row=2, column=2, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=dias), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=2, column=3, pady=10, sticky="W")
        #---Ver Meses
        Label(FramePerfil, text="Meses:", fg="black", font=("Arial",15,"bold")).grid(row=3, column=2, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=meses), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=3, column=3, pady=10, sticky="W")
        #---Ver Años
        Label(FramePerfil, text="Años:", fg="black", font=("Arial",15,"bold")).grid(row=4, column=2, pady=10, padx=20, sticky="E")
        Entry(FramePerfil, textvariable=StringVar(FramePerfil, value=anios), state='readonly', font=("Arial",12), bd=5, relief=GROOVE, width=33).grid(row=4, column=3, pady=10, sticky="W")

ventana = Tk()
aplicacion = app(ventana)
ventana.mainloop()