class View:
    """
    ************************************
    *        A view for a store DB             *
    ************************************
    """

    def start (self):
        print('=========================')
        print('= Bienvenido al sistema =')
        print('=========================')
        
    def end (self):
        print('=========================')
        print('= Hasta la vista, baby  =')
        print('=========================')
        
    def main_menu(self):
        print('*************************')
        print('* -- Menu principal --  *')
        print('*************************')
        print('1. Salas')
        print('2. Peliculas')          
        print('3. Usuarios')
        print('4. Funciones')
        print('5. Comprar Boletos')
        print('6. Registrarse')
        print('7. Salir')

     
    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')
     
    def not_valid_option(self):
        print('¡Opcion no valida!/n Intenta de nuevo')
     
    def ask(self, output):
        print(output, end = '')   

    def msg(self, output):
        print(output)     

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +') 
        print('+'*(len(str(id))+len(op)+24))     

    def error(self, err):
        print('!Error¡ '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def salas_menu(self):
        print('*************************')
        print('* -- Submenu Salas  --  *')
        print('*************************')
        print('1. Agregar sala')
        print('2. Mostrar sala')          
        print('3. Mostrar todos las salas')
        print('4. Actualizar sala')
        print('5. Borrar sala')
        print('6. Regresar')

    def mostrar_sala(self, record):
        print(f'{record[0]:<6}|{record[1]:<25}|{record[2]:<25}|{record[3]:<35}')
     
    def mostrar_sala_header(self, header):
        print(header.center(94,'*'))
        print('ID'.ljust(6)+'|'+'Num. Asientos por fila'.ljust(25)+'|'+'Num. filas'.ljust(25)+'|'+'Tipo de sala'.ljust(35))
        print('-'*94)

    def mostrar_sala_midder(self):
        print('-'*94)
     
    def mostrar_sala_footer(self):
        print('*'*94)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def usuarios_menu(self):
        print('*************************')
        print('* -- Submenu Usuarios  --  *')
        print('*************************')
        print('1. Agregar usuario')
        print('2. Mostrar usuario')          
        print('3. Mostrar todos las usuarios')
        print('4. Actualizar usuario')
        print('5. Borrar usuario')
        print('6. Regresar')
    
    def mostrar_usuario(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido:', record[2])
        print('email:', record[3])
        print('admin:', record[5])
    
    def mostrar_usuario_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_usuario_midder(self):
        print('-'*48)
    
    def mostrar_usuario_footer(self):
        print('*'*48)