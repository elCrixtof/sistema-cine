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
                self.registro_menu()
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
                self.venta_boletos()
            elif o == '6':
                self.view.end()
            elif o == '7':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    
    def main_menu_usuario(self):
        o = '0'
        while o != '3':
            self.view.main2_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                # self.inicio_sesion()
                print('prueba')
            elif o == '2':
                # self.registro_menu()
                print('prueba')
            elif o == '3':
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

    def registro_menu(self):
        pass






    
    """
    ************************************
    *  Controlador para salar          *
    ************************************
    """
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

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


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
                self.actualzar_usuario()
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
    
    def actualzar_usuario(self):
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
        fields, vals = self.update_lists(['u_pnombre','u_apellido','u_email','u_password','u_admin'], whole_vals)
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

    def funciones_menu(self):
        pass

    def venta_boletos(self):
        pass

