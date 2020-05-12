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
        self.main_menu()
    
    """
    ************************************
    *  Controladores generales          *
    ************************************
    """
    def inicio_menu(self):
        o = '0'
        while o != '2':
            self.view.main_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.salas_menu()
            else:
                self.view.not_valid_option()
        return

    def main_menu(self):
        o = '0'
        while o != '7':
            self.view.main_menu()
            self.view.option('6')
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
        return [asientos, filas, tipo]
    
    def crear_sala(self):
        asientos, filas, tipo = self.ask_sala()
        id_sala = self.model.crear_sala(asientos, filas, tipo)
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
        pass
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

