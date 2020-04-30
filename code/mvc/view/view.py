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
        print('2. Comprar Boletos')          
        print('3. Funciones')
        print('4. Peliculas')
        print('5. Registrarse')
        print('6. Salir')

     
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
        print(f'{record[0]:<6}|{record[1]:<25}|{record[2]:<35}')
     
    def mostrar_sala_header(self, header):
        print(header.center(68,'*'))
        print('ID'.ljust(6)+'|'+'Num. Asientos'.ljust(25)+'|'+'Tipo de sala'.ljust(35))
        print('-'*68)

    def mostrar_sala_midder(self):
        print('-'*68)
     
    def mostrar_sala_footer(self):
        print('*'*68)