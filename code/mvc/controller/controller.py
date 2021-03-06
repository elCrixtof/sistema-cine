from model.model import Model
from view.view import View
from datetime import date 

class Controller:
    """
    ************************************
    *  Controlador para cine Db        *
    ************************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.id = 0
     
    def start(self):
        self.view.start()
        self.inicio_menu()
    
    """
    ************************************
    *  Controladores generales          *
    ************************************
    """
    def inicio_menu(self):
        o = '0'
        while o != '3':
            self.view.inicio_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.inicio_sesion()
            elif o == '2':
                self.crear_usuario()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def main_menu_admin(self):
        o = '0'
        while o != '7':
            self.view.main_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.salas_menu()
            elif o == '2':
                self.peliculas_menu()
            elif o == '3':
                self.usuarios_menu()
            elif o == '4':
                self.funciones_menu()
            elif o == '5':
                self.asientos_menu()
            elif o == '6':
                self.compras_menu_admin()
            elif o == '7':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def main_menu_usuario(self):
        o = '0'
        while o != '8':
            self.view.main2_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.leer_todas_peliculas()
            elif o == '2':
                self.leer_todas_funciones()
            elif o == '3':
                self.leer_funciones_dia()
            elif o == '4':
                self.leer_funciones_dia_pelicula()
            elif o == '5':
                self.leer_asientos_funcion()
            elif o == '6':
                self.compras_menu_usuario()
            elif o == '7':
                self.actualzar_usuario_usuario()
            elif o == '8':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f, v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals
    
    """
    ************************************
    *  Inicio sesion  y registro       *
    ************************************
    """

    def ask_inicio(self):
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Password: ')
        password = input()
        return [email, password]

    def inicio_sesion(self):
        email, password = self.ask_inicio()
        usuario = self.model.leer_usuario_email_password(email, password)
        if type(usuario) == tuple:
            self.id = usuario[0]
            self.view.mostrar_usuario_header('Datos de tu usuario')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            if usuario == None:
                self.view.error('El EMAIL O EL PASSWORD SON INCORRECTOS')
            else: 
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
            return
        if usuario[5] == True:
            self.main_menu_admin()
        else:
            self.main_menu_usuario()
        return usuario

    """
    ************************************
    *  Controlador para salas          *
    ************************************
    """
    def salas_menu(self):
        o = '0'
        while o != '6':
            self.view.salas_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_sala()
            elif o == '2':
                self.leer_una_sala()
            elif o == '3':
                self.leer_todas_salas()
            elif o == '4':
                self.actualzar_sala()
            elif o == '5':
                self.eliminar_sala()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_sala(self):
        self.view.ask('Asientos por fila: ')
        asientos = input()
        self.view.ask('Numero de filas: ')
        filas = input()
        self.view.ask('Tipo: ')
        tipo = input()
        return [filas, asientos, tipo]
    
    def crear_sala(self):
        asientos, filas, tipo = self.ask_sala()
        id_sala = self.model.crear_sala(filas, asientos, tipo)
        if type(id_sala) == int:
            self.view.ok(id_sala, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA SALA. REVISA.')
        return

    def leer_una_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        sala = self.model.leer_una_sala(id_sala)
        if type(sala) == tuple:
            self.view.mostrar_sala_header('Datos de la sala'+id_sala+' ')
            self.view.mostrar_sala(sala)
            self.view.mostrar_sala_midder()
            self.view.mostrar_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
        return

    def leer_todas_salas(self):
        salas = self.model.leer_todas_salas()
        if type(salas) == list:
            self.view.mostrar_sala_header(' Datos de todas las salas ')
            for sala in salas:
                self.view.mostrar_sala(sala)
                self.view.mostrar_sala_midder()
            self.view.mostrar_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA.')
        return

    def actualzar_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        sala = self.model.leer_una_sala(id_sala)
        if type(sala) == tuple:
            self.view.mostrar_sala_header('Datos de la sala'+id_sala+' ')
            self.view.mostrar_sala(sala)
            self.view.mostrar_sala_midder()
            self.view.mostrar_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['s_num_filas', 's_num_asientosf','s_tipo'], whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.actualizar_sala(fields, vals)
        if out == True:
             self.view.ok(id_sala, 'actualizo')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISA.')
        return

    def eliminar_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        count = self.model.eliminar_sala(id_sala)
        if count != 0:
               self.view.ok(id_sala, 'borro')
        else: 
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA. REVISA.')
        return

    """
    ************************************
    *  Controlador para peliculas      *
    ************************************
    """

    def peliculas_menu(self):
        o = '0'
        while o != '6':
            self.view.peliculas_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_pelicula()
            elif o == '2':
                self.leer_una_pelicula()
            elif o == '3':
                self.leer_todas_peliculas()
            elif o == '4':
                self.actualzar_pelicula()
            elif o == '5':
                self.eliminar_pelicula()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_pelicula(self):
        self.view.ask('Titulo: ')
        titulo = input()
        self.view.ask('Genero: ')
        genero = input ()
        self.view.ask('Descripcion: ')
        descripcion = input()
        return [titulo, genero, descripcion]

    def crear_pelicula(self):
        titulo, genero, descripcion = self.ask_pelicula()
        id_pelicula = self.model.crear_pelicula(titulo, genero, descripcion)
        if type(id_pelicula) == int:
            self.view.ok(id_pelicula, 'se agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA.')
        return

    def leer_una_pelicula(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        pelicula = self.model.leer_una_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.mostrar_pelicula_header('Datos de la pelicula'+id_pelicula+' ')
            self.view.mostrar_pelicula(pelicula)
            self.view.mostrar_pelicula_midder()
            self.view.mostrar_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
        return    

    def leer_todas_peliculas(self):
        peliculas = self.model.leer_todas_peliculas()
        if type(peliculas) == list:
            self.view.mostrar_pelicula_header(' Datos de todas las peliculas ')
            for pelicula in peliculas:
                self.view.mostrar_pelicula(pelicula)
                self.view.mostrar_pelicula_midder()
            self.view.mostrar_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
        return

    def actualzar_pelicula(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        pelicula = self.model.leer_una_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.mostrar_pelicula_header('Datos de la pelicula'+id_pelicula+' ')
            self.view.mostrar_pelicula(pelicula)
            self.view.mostrar_pelicula_midder()
            self.view.mostrar_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
            return  
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['p_titulo','p_genero','p_descripcion'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.actualizar_pelicula(fields, vals)
        if out == True:
             self.view.ok(id_pelicula, 'actualizo')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA.')
        return

    def eliminar_pelicula(self):
        self.view.ask('ID plicula: ')
        id_pelicula = input()
        count = self.model.eliminar_pelicula(id_pelicula)
        if count != 0:
               self.view.ok(id_pelicula, 'borro')
        else: 
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA.')
        return

    """
    ************************************
    *  Controlador para usuarios      *
    ************************************
    """
    
    def usuarios_menu(self):
        o = '0'
        while o != '6':
            self.view.usuarios_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_usuario()
            elif o == '2':
                self.leer_un_usuario()
            elif o == '3':
                self.leer_todos_usuarios()
            elif o == '4':
                self.actualzar_usuario_admin()
            elif o == '5':
                self.eliminar_usuario()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_usuario(self):
        self.view.ask('Nombre: ')
        nombre = input ()
        self.view.ask('Apellido: ')
        apellido = input ()
        self.view.ask('email: ')
        email = input ()
        self.view.ask('Password: ')
        password = input()
        return [nombre, apellido, email, password]

    def crear_usuario(self):
        nombre, apellido, email, password = self.ask_usuario()
        admin = False
        id_usuario = self.model.crear_usuario(nombre, apellido, email, password, admin)
        if type(id_usuario) == int:
            self.view.ok(id_usuario, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL USUARIO. REVISA.')
        return

    def leer_un_usuario(self):
        self.view.ask('ID usuario: ')
        id_usuario = input()
        usuario = self.model.leer_un_usuario(id_usuario)
        if type(usuario) == tuple:
            self.view.mostrar_usuario_header('Datos del usuario'+id_usuario+' ')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            if usuario == None:
                self.view.error('EL USUARIO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return

    def leer_todos_usuarios(self):
        usuarios = self.model.leer_todos_usuarios()
        if type(usuarios) == list:
            self.view.mostrar_usuario_header(' Datos de todos los usuarios ')
            for usuario in usuarios:
                self.view.mostrar_usuario(usuario)
                self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return
    
    def actualzar_usuario_admin(self):
        self.view.ask('ID usuario: ')
        id_usuario = input()
        usuario = self.model.leer_un_usuario(id_usuario)
        if type(usuario) == tuple:
            self.view.mostrar_usuario_header('Datos del usuario'+id_usuario+' ')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            if usuario == None:
                self.view.error('EL USUARIO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_usuario()
        self.view.ask('Tipo(Admin:1 Mortal:0): ')
        u_admin = input()
        whole_vals.append(u_admin)
        fields, vals = self.update_lists(['u_pnombre','u_apellido','u_email','u_password','u_admin'], whole_vals)
        vals.append(id_usuario)
        vals = tuple(vals)
        out = self.model.actualizar_usuario(fields, vals)
        if out == True:
             self.view.ok(id_usuario, 'actualizo')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA.')
        return
    
    def actualzar_usuario_usuario(self):
        id_usuario = self.id
        usuario = self.model.leer_un_usuario(id_usuario)
        if type(usuario) == tuple:
            self.view.mostrar_usuario_header('Datos del usuario'+id_usuario+' ')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            if usuario == None:
                self.view.error('EL USUARIO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_usuario()
        fields, vals = self.update_lists(['u_pnombre','u_apellido','u_email','u_password'], whole_vals)
        vals.append(id_usuario)
        vals = tuple(vals)
        out = self.model.actualizar_usuario(fields, vals)
        if out == True:
             self.view.ok(id_usuario, 'actualizo')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA.')
        return

    def eliminar_usuario(self):
        self.view.ask('ID usuario: ')
        id_usuario = input()
        count = self.model.eliminar_usuario(id_usuario)
        if count != 0:
               self.view.ok(id_usuario, 'borro')
        else: 
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL USUARIO. REVISA.')
        return

    """
    ************************************
    *  Controladores FUNCIONES          *
    ************************************
    """

    def funciones_menu(self):
        o = '0'
        while o != '8':
            self.view.funciones_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.crear_funcion()
            elif o == '2':
                self.leer_una_funcion()
            elif o == '3':
                self.leer_todas_funciones()
            elif o == '4':
                self.actualizar_funcion()
            elif o == '5':
                self.eliminar_funcion()
            elif o == '6':
                self.leer_funciones_dia()
            elif o == '7':
                self.leer_funciones_dia_pelicula()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_funcion(self):
        self.view.ask('Fecha y Hora (AA-MM-DD HH:MM:SS):')
        f_fecha_hora = input()
        self.view.ask('Precio:')
        f_precio = input()
        self.view.ask('ID Pelicula:')
        id_pelicula = input()
        self.view.ask('ID Sala:')
        id_sala = input() 
        return [f_fecha_hora,f_precio,id_pelicula,id_sala]

    def crear_funcion(self):
        fecha_hora, precio, id_pelicula, id_sala = self.ask_funcion()
        id_funcion = self.model.crear_funcion(fecha_hora, precio, id_pelicula, id_sala )
        if type(id_funcion) == int:
            self.view.ok(id_funcion, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISA.')
        return

    def leer_una_funcion(self):
        self.view.ask('ID funcion: ')
        id_funcion = input()
        funcion = self.model.leer_una_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.mostrar_funcion_header('Datos del funcion'+id_funcion+' ')
            self.view.mostrar_funcion(funcion)
            self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
        return
    
    def leer_todas_funciones(self):
        funciones = self.model.leer_todas_funciones()
        if type(funciones) == list:
            self.view.mostrar_funcion_header(' Datos de todas las funciones ')
            for funcion in funciones:
                self.view.mostrar_funcion(funcion)
                self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
        return

    def leer_funciones_dia(self):
        self.view.ask('Dia(AAAA-MM-DD): ')
        dia = input()
        inicio = dia + ' 00:00:00'
        fin = dia + ' 23:59:59' 
        funciones = self.model.leer_funciones_horario(inicio, fin)
        if type(funciones) == list:
            self.view.mostrar_funcion_header(' Datos de todas las funciones del dia ' + dia)
            for funcion in funciones:
                self.view.mostrar_funcion(funcion)
                self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
        return

    def leer_funciones_dia_pelicula(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        self.view.ask('Dia(AAAA-MM-DD): ')
        dia = input()
        self.view.ask('Pelicula')
        inicio = dia + ' 00:00:00'
        fin = dia + ' 23:59:59' 
        funciones = self.model.leer_funciones_horario_pelicula(inicio, fin, id_pelicula)
        if type(funciones) == list:
            self.view.mostrar_funcion_header(' Datos de todas las funciones del dia ' + dia)
            for funcion in funciones:
                self.view.mostrar_funcion(funcion)
                self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
        return

    def actualizar_funcion(self):
        self.view.ask('ID funcion: ')
        id_funcion = input()
        funcion = self.model.leer_una_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.mostrar_funcion_header('Datos del funcion'+id_funcion+' ')
            self.view.mostrar_funcion(funcion)
            self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_funcion()
        fields, vals = self.update_lists(['f_fecha_hora','f_precio','id_pelicula','id_sala'], whole_vals)
        vals.append(id_funcion)
        vals = tuple(vals)
        out = self.model.actualizar_funcion(fields, vals)
        if out == True:
             self.view.ok(id_funcion, 'actualizo')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR LA FUNCION. REVISA.')
        return

    def eliminar_funcion(self):
        self.view.ask('ID funcion: ')
        id_funcion = input()
        count = self.model.eliminar_funcion(id_funcion)
        if count != 0:
               self.view.ok(id_funcion, 'borro')
        else: 
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA FUNCION. REVISA.')
        return

    """
    ************************************
    *  Controladores Asientos          *
    ************************************
    """

    def asientos_menu(self):
        o = '0'
        while o != '8':
            self.view.asientos_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.crear_asiento()
            elif o == '2':
                self.leer_un_asiento()
            elif o == '3':
                self.leer_todos_asientos()
            elif o == '4':
                self.leer_asientos_funcion()
            elif o == '5':
                self.crear_asientos_funcion()
            elif o == '6':
                self.actualizar_asiento()
            elif o == '7':
                self.eliminar_asiento()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_asiento(self):
        self.view.ask('ID Asiento(A1,B2,etc.): ')
        id_asiento = input()
        self.view.ask('ID Funcion: ')
        id_funcion = input()
        self.view.ask('Estado(Ocupado:1, Libre:0): ')
        a_estado = input()
        return [id_asiento, id_funcion, a_estado]

    def crear_asiento(self):
        id_asiento, id_funcion, a_estado = self.ask_asiento()
        id_asiento = self.model.crear_asiento(id_asiento, id_funcion, a_estado)
        if type(id_asiento) == int:
            self.view.ok(id_asiento, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
        return
    
    def crear_asientos_funcion(self):
        self.view.ask('ID funcion: ')
        id_funcion = input()
        funcion = self.model.leer_una_funcion(id_funcion)
        if type(funcion) == tuple:
            id_sala = funcion[4]
            sala = self.model.leer_una_sala(id_sala)
            n_filas = sala[1]
            n_asientosf = sala[2]
            fila = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            for i in range(n_filas):
                for k in range(n_asientosf):
                    id_asiento = fila[i] + str(k)
                    id_asiento = self.model.crear_asiento(id_asiento, id_funcion, 0)
                    if type(id_asiento) == int:
                        self.view.ok(id_asiento, 'agrego')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
                        continue
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
        return

    def leer_un_asiento(self):
        self.view.ask('ID asiento: ')
        id_asiento = input()
        self.view.ask('ID funcion: ')
        id_funcion = input()
        asiento = self.model.leer_un_asiento(id_asiento, id_funcion)
        if type(asiento) == tuple:
            self.view.mostrar_asiento_header('Datos del asiento'+id_asiento+' ')
            self.view.mostrar_asiento(asiento)
            self.view.mostrar_asiento_midder()
            self.view.mostrar_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
        return
    
    def leer_todos_asientos(self):
        asientos = self.model.leer_todos_asientos()
        if type(asientos) == list:
            self.view.mostrar_asiento_header(' Datos de todos los asientos ')
            for asiento in asientos:
                self.view.mostrar_asiento(asiento)
                self.view.mostrar_asiento_midder()
            self.view.mostrar_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
        return

    def leer_asientos_funcion(self):
          self.view.ask('ID funcion: ')
          id_funcion = input()
          asientos = self.model.leer_todos_asientos_funcion(id_funcion)
          if type(asientos) == list:
               self.view.mostrar_asiento_header(' Asientos para la funcion '+id_funcion+' ')
               for asiento in asientos:
                    self.view.mostrar_asiento(asiento)
                    self.view.mostrar_asiento_midder()
               self.view.mostrar_asiento_footer()
          else: 
               self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA.')
          return

    def actualizar_asiento(self):
        self.view.ask('ID funcion: ')
        id_funcion = input()
        self.view.ask('ID asiento: ')
        id_asiento = input()
        asiento = self.model.leer_un_asiento(id_asiento, id_funcion)
        if type(asiento) == tuple:
            self.view.mostrar_asiento_header('Datos del asiento'+id_asiento+' ')
            self.view.mostrar_asiento(asiento)
            self.view.mostrar_asiento_midder()
            self.view.mostrar_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        self.view.ask('Estado(Ocupado:1 Libre:0): ')
        estado = input()
        fields, whole_vals = self.update_lists(['a_estado'], [estado])
        whole_vals.append(id_asiento)
        whole_vals.append(id_funcion)
        out = self.model.actualizar_asiento(fields, whole_vals)
        if out == True:
             self.view.ok(id_asiento, 'actualizo')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR LA FUNCION. REVISA.')
        return
    
    def actualizar_asiento_automatico(self, id_asiento, id_funcion, ocupado):
        asiento = self.model.leer_un_asiento(id_asiento, id_funcion)
        if type(asiento) == tuple:
            self.view.mostrar_asiento_header('Datos del asiento'+id_asiento+' ')
            self.view.mostrar_asiento(asiento)
            self.view.mostrar_asiento_midder()
            self.view.mostrar_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
            return
        estado = str(ocupado)
        fields, whole_vals = self.update_lists(['a_estado'], [estado])
        whole_vals.append(id_asiento)
        whole_vals.append(id_funcion)
        out = self.model.actualizar_asiento(fields, whole_vals)
        if out == True:
             self.view.ok(id_asiento, 'actualizo')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR LA FUNCION. REVISA.')
        return

    def eliminar_asiento(self):
        self.view.ask('ID asiento(A1,B2,etc): ')
        id_asiento = input()
        self.view.ask('ID funcion: ')
        id_funcion = input()
        count = self.model.eliminar_asiento(id_asiento, id_funcion)
        if count != 0:
               self.view.ok(id_asiento, 'borro')
        else: 
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO. REVISA.')
        return

    """
    ************************************
    *  Controladores Compras           *
    ************************************
    """

    def compras_menu(self):
        pass

    def compras_menu_usuario(self):
        o = '0'
        while o != '5':
            self.view.compras_menu_usuario()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_compra_usuario()
            elif o == '2':
                self.leer_una_compra_usuario()
            elif o == '3':
                self.leer_todas_compras_usuario()
            elif o == '4':
                self.sumar_boletos_compra_usuario()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return
    
    def compras_menu_admin(self):
        o = '0'
        while o != '8':
            self.view.compras_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.crear_compra()
            elif o == '2':
                self.leer_una_compra()
            elif o == '3':
                self.leer_todas_compras()
            elif o == '4':
                self.actualizar_compra()
            elif o == '5':
                self.eliminar_compra()
            elif o == '6':
                self.sumar_boletos_compra()
            elif o == '7':
                self.eliminar_boletos_compra()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def crear_compra(self):
        self.view.ask('ID Usuario: ')
        id_usuario = input()
        c_total_compra = 0.0
        id_compra = self.model.crear_compra(c_total_compra ,id_usuario)

        if type(id_compra) == int:
            id_asiento = ' '
            while id_asiento != '':
                self.view.msg('---- Agrega asientos a la compra (deja vacio el id del asiento para salir) ---')
                self.view.ask('ID Asiento: ')
                id_asiento = input()
                self.view.ask('ID Funcion: ')
                id_funcion = input()
                precio = self.crear_boleto(id_asiento, id_funcion, id_compra)
                c_total_compra += precio
            self.model.actualizar_compra(('c_total_compra = %s',),(c_total_compra,id_compra))
        else:
            self.view.error('NO SE PUDO CREAR LA COMPRA. REVISA')
        return

    def leer_una_compra(self):
          self.view.ask('ID compra: ')
          id_compra = input()
          compra = self.model.leer_una_compra(id_compra)
          if type(compra) == tuple:
               boletos = self.model.leer_todos_boletos(id_compra)
               if type(boletos) != list and boletos != None:
                    self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
               else:
                    self.view.mostrar_compra_header(' Datos de la Compra '+id_compra+' ')
                    self.view.mostrar_compra(compra)
                    self.view.mostrar_boleto_header()
                    for boleto in boletos:
                         self.view.mostrar_boleto(boleto)
                    self.view.mostrar_boleto_header()
                    self.view.mostrar_compra_footer()
                    return compra
          else:
               if compra == None:
                    self.view.error('LA COMPRA NO EXISTE')
               else:
                    self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
          return  

    def leer_todas_compras(self):
        compras = self.model.leer_todas_compras()
        if type(compras) == list:
            self.view.mostrar_compra_header(' Todas las compras ')
            for compra in compras:
                id_compra = compra[0]
                boletos = self.model.leer_todos_boletos(id_compra)
                if type(boletos) != list and boletos != None:
                        self.view.error('PROBLEMA AL LEER BOLETOS. REVISA.')
                else:
                        self.view.mostrar_compra(compra)
                        self.view.mostrar_boleto_header()
                        for boleto in boletos:
                            self.view.mostrar_boleto(boleto)
                        self.view.mostrar_boleto_footer()
                        self.view.mostrar_compra_midder()
                self.view.mostrar_compra_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA ORDEN. REVISA.')
        return

    def actualizar_compra(self):
        self.view.ask('ID compra a modificar: ')
        id_compra = input()
        compra = self.model.leer_una_compra(id_compra)
        if type(compra) == tuple:
            self.view.mostrar_compra_header( 'Datos de la compra '+id_compra+' ')
            self.view.mostrar_compra(compra)
            self.view.mostrar_compra_footer()
        else:
            if compra == None:
                self.view.error('LA ORDEN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA ORDEN. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        self.view.ask('ID usuario: ')
        id_usuario = input()
        self.view.ask('Total Compra: ')
        c_total_compra = input()
        whole_vals = [id_usuario, c_total_compra]
        fields, vals = self.update_lists(['id_usuario', 'c_total_compra'], whole_vals)
        vals.append(id_compra)
        vals = tuple(vals)
        out = self.model.actualizar_compra(fields, vals)
        if out == True:
            self.view.ok(id_compra, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA ORDEN. REVISA.')
        return

    def eliminar_compra(self):
          self.view.ask('Id de compra a borrar: ')
          id_compra = input()
          count = self.model.eliminar_compra(id_compra)
          if count != 0:
               self.view.ok(id_compra, 'borro')
          else: 
               if count == 0:
                    self.view.error('LA COMPRA NO EXISTE')
               else:
                    self.view.error('PROBLEMA AL BORRAR LA COMPRA. REVISA')
          return

    # ***************** Compras Usuario ***********************

    def crear_compra_usuario(self):
        id_usuario = self.id
        c_total_compra = 0.0
        id_compra = self.model.crear_compra(c_total_compra ,id_usuario)

        if type(id_compra) == int:
            id_asiento = ' '
            while id_asiento != '':
                self.view.msg('---- Agrega asientos a la compra (deja vacio el id del asiento para salir) ---')
                self.view.ask('ID Asiento: ')
                id_asiento = input()
                self.view.ask('ID Funcion: ')
                id_funcion = input()
                precio = self.crear_boleto(id_asiento, id_funcion, id_compra)
                c_total_compra += precio
            self.model.actualizar_compra(('c_total_compra = %s',),(c_total_compra,id_compra))
        else:
            self.view.error('NO SE PUDO CREAR LA COMPRA. REVISA')
        return

    def leer_una_compra_usuario(self):
        self.view.ask('ID compra: ')
        id_compra = input()
        compra = self.model.leer_una_compra_usuario(id_compra, self.id)
        if type(compra) == tuple:
            boletos = self.model.leer_todos_boletos(id_compra)
            if type(boletos) != list and boletos != None:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
            else:
                self.view.mostrar_compra_header(' Datos de la Compra '+id_compra+' ')
                self.view.mostrar_compra(compra)
                self.view.mostrar_boleto_header()
                for boleto in boletos:
                        self.view.mostrar_boleto(boleto)
                self.view.mostrar_boleto_header()
                self.view.mostrar_compra_footer()
                return compra
        else:
            if compra == None:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
        return 

    def leer_todas_compras_usuario(self):
        compras = self.model.leer_todas_compras_usuario(self.id)
        if type(compras) == list:
            self.view.mostrar_compra_header(' Todas las compras para el usuario ' + str(self.id) +' ')
            for compra in compras:
                id_compra = compra[0]
                boletos = self.model.leer_todos_boletos(id_compra)
                if type(boletos) != list and boletos != None:
                        self.view.error('PROBLEMA AL LEER BOLETOS. REVISA.')
                else:
                        self.view.mostrar_compra(compra)
                        self.view.mostrar_boleto_header()
                        for boleto in boletos:
                            self.view.mostrar_boleto(boleto)
                        self.view.mostrar_boleto_footer()
                        self.view.mostrar_compra_midder()
                self.view.mostrar_compra_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA ORDEN. REVISA.')
        return

    def actualizar_compra_usuario(self):
        self.view.ask('ID compra a modificar: ')
        id_compra = input()
        compra = self.model.leer_una_compra_usuario(id_compra, self.id)
        if type(compra) == tuple:
            self.view.mostrar_compra_header( 'Datos de la compra '+id_compra+' ')
            self.view.mostrar_compra(compra)
            self.view.mostrar_compra_footer()
        else:
            if compra == None:
                self.view.error('LA ORDEN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA ORDEN. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        id_usuario = self.id
        whole_vals = [id_usuario]
        fields, vals = self.update_lists(['id_usuario'], whole_vals)
        vals.append(id_compra)
        vals = tuple(vals)
        out = self.model.actualizar_compra(fields, vals)
        if out == True:
            self.view.ok(id_compra, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA ORDEN. REVISA.')
        return


    """
    ************************************
    *  Controladores Boletos           *
    ************************************
    """


    def crear_boleto(self, id_asiento, id_funcion, id_compra):
        precio = 0.0
        if id_asiento != '' and id_funcion != '' and id_compra != '':
            asiento = self.model.leer_un_asiento(id_asiento, id_funcion)

            if type(asiento) == tuple:
                self.view.mostrar_asiento_header(' Datos del asiento '+id_asiento+' ')
                self.view.mostrar_asiento(asiento)
                self.view.mostrar_asiento_footer()
                funcion = self.model.leer_una_funcion(id_funcion)
                precio = funcion[2]
                out = self.model.crear_boleto(id_asiento, id_funcion, id_compra)
                ocupado = 1
                self.actualizar_asiento_automatico(id_asiento, id_funcion, ocupado)
                if out == True:
                        self.view.ok(asiento[0], 'agrego a la compra')
                else:
                    if out.errno == 1062:
                        self.view.error('EL BOLETO YA ESTA EN LA COMPRA')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL BOLETO. REVISA.')
                    precio = 0.0
            else:
                if asiento == None:
                    self.view.error('EL ASIENTO NO EXISTE.')
                else:
                    self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA')
        return precio
        
    def sumar_boletos_compra(self):
        compra = self.leer_una_compra()
        if type(compra) == tuple:
            id_compra = compra[0]
            c_total_compra = compra[1]
            id_asiento = ' '
            while id_asiento != '':
                self.view.msg('---- Agrega asientos a la compra (deja vacios los IDs para salir ----')
                self.view.ask('ID Asiento: ')
                id_asiento = input()
                self.view.ask('ID Funcion: ')
                id_funcion = input()
                precio = self.crear_boleto(id_asiento, id_funcion, id_compra)
                c_total_compra += precio
            self.model.actualizar_compra(('c_total_compra = %s',),(c_total_compra, id_compra))
        return
    
    def eliminar_boletos_compra(self):
        self.view.ask('ID compra: ')
        id_compra = input()
        compra = self.model.leer_una_compra(id_compra)
        if type(compra) == tuple:
            c_total_compra = compra[1]
            id_asiento = ' '
            while id_asiento != '':
                self.view.msg('---- Borra Boletos de la orden (deja vacios los IDs para salir ----')
                self.view.ask('ID asiento: ')
                id_asiento =  input()
                self.view.ask('ID funcion: ')
                id_funcion = input()
                if id_asiento != '' and id_funcion != '':
                        boleto = self.model.leer_un_boleto(id_compra, id_asiento, id_funcion)
                        count = self.model.eliminar_boleto(id_asiento, int(id_funcion), id_compra)
                        ocupado = 0
                        self.actualizar_asiento_automatico(id_asiento, id_funcion, ocupado)
                        if type(boleto) == tuple and count != 0:
                            funcion = self.model.leer_una_funcion(id_funcion)
                            precio = funcion[2]
                            c_total_compra -= precio
                            self.view.ok(id_asiento, 'borro de la orden')
                        else:
                            if boleto == None:
                                self.view.error('EL BOLETO NO EXISTE EN LA COMPRA')
                            else:
                                self.view.error('PROBLEMA AL BORAR EL BOLETO. REVISA.')
            self.model.actualizar_compra(('c_total_compra = %s',), (c_total_compra, id_compra))
        return

    def sumar_boletos_compra_usuario(self):
        compra = self.leer_una_compra_usuario()
        if type(compra) == tuple:
            id_compra = compra[0]
            c_total_compra = compra[1]
            id_asiento = ' '
            while id_asiento != '':
                self.view.msg('---- Agrega asientos a la compra (deja vacios los IDs para salir ----')
                self.view.ask('ID Asiento: ')
                id_asiento = input()
                self.view.ask('ID Funcion: ')
                id_funcion = input()
                precio = self.crear_boleto(id_asiento, id_funcion, id_compra)
                c_total_compra += precio
            self.model.actualizar_compra(('c_total_compra = %s',),(c_total_compra, id_compra))
        return

