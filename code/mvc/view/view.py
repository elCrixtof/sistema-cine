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

    def inicio_menu(self):
        print('*************************')
        print('* -- Menu principal --  *')
        print('*************************')
        print('1. Inicio de sesion')
        print('2. Registrarse')
        print('3. Salir')

    def main_menu(self):
        print('*****************************')
        print('* -- Menu Administrador --  *')
        print('*****************************')
        print('1. Salas')
        print('2. Peliculas')          
        print('3. Usuarios')
        print('4. Funciones')
        print('5. Asientos')
        print('6. Compras')
        print('7. Salir')

    def main2_menu(self):
        print('*************************')
        print('* -- Menu Usuario --  *')
        print('*************************')
        print('1. Ver todas peliculas')
        print('2. Ver todas Funciones')
        print('3. Ver todas Funciones por dia')
        print('4. Ver todas Funciones por pelicula y dia')
        print('5. Ver asientos de una funcion')
        print('6. Comprar Boletos')
        print('7. Actualizar Cuenta')
        print('8. Salir') 

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

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def peliculas_menu(self):
        print('*************************')
        print('* -- Submenu peliculas  --  *')
        print('*************************')
        print('1. Agregar peliculas')
        print('2. Mostrar peliculas')          
        print('3. Mostrar todos las peliculas')
        print('4. Actualizar peliculas')
        print('5. Borrar peliculas') 
        print('6. Regresar')
    
    def mostrar_pelicula(self, record):
        print('ID:', record[0])
        print('Titulo:', record[1])
        print('Genero:', record[2])
        print('Descripcion:', record[3])
    
    def mostrar_pelicula_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_pelicula_midder(self):
        print('-'*48)
    
    def mostrar_pelicula_footer(self):
        print('*'*48)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def funciones_menu(self):
        print('*************************')
        print('* -- Submenu funciones  --  *')
        print('*************************')
        print('1. Agregar funciones')
        print('2. Mostrar funciones')          
        print('3. Mostrar todos las funciones')
        print('4. Actualizar funciones')
        print('5. Borrar funciones') 
        print('6. Leer todas Funciones por dia') 
        print('7. Leer todas Funciones por dia y por pelicula') 
        print('8. Regresar')

    def mostrar_funcion(self, record):
        print(f'{record[0]:<12}|{record[1]}|{record[2]:<12}|{record[3]:<12}|{record[4]:<12}')
     
    def mostrar_funcion_header(self, header):
        print(header.center(45,'*'))
        print('ID Funcion'.ljust(12)+'|'+'Fecha y Hora'.ljust(19)+'|'+'Precio'.ljust(12)+'|'+'ID Pelicula'.ljust(12)+'|'+'ID Sala'.ljust(12))
        print('-'*45)

    def mostrar_funcion_midder(self):
        print('-'*45)
     
    def mostrar_funcion_footer(self):
        print('*'*45)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def asientos_menu(self):
        print('*************************')
        print('* -- Submenu asientos  --  *')
        print('*************************')
        print('1. Agregar asiento')
        print('2. Mostrar asiento')          
        print('3. Mostrar todos los asientos')
        print('4. Mostrar todos los asientos por funcion')
        print('5. Crear asientos automaticamente por funcion')
        print('6. Actualizar asiento')
        print('7. Borrar asiento') 
        print('8. Regresar')

    def mostrar_asiento(self, record):
        if (record[2] == 1):
            estado = 'Ocupado'
        else:
            estado = 'Libre'
        print(f'{record[0]:<10}|{record[1]:<10}|{estado:<10}')
     
    def mostrar_asiento_header(self, header):
        print(header.center(22,'*'))
        print('ID asiento'.ljust(10)+'|'+'ID funcion'.ljust(10)+'|'+'Estado'.ljust(10))
        print('-'*22)

    def mostrar_asiento_midder(self):
        print('-'*22)
     
    def mostrar_asiento_footer(self):
        print('*'*22)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # id_compra
    # c_total_compra
    # id_usuario

    def compras_menu(self):
        print('*************************')
        print('* -- Submenu compras  --  *')
        print('*************************')
        print('1. Agregar compra')
        print('2. Mostrar compra')          
        print('3. Mostrar todas las compras')
        print('4. Actualizar Compra')
        print('5. Eliminar compra')
        print('6. Agregar boletos a compra')
        print('7. Quitar boletos a compra')
        print('8. Regresar')
    
    def compras_menu_usuario(self):
        print('*************************')
        print('* -- Submenu compras  --  *')
        print('*************************')
        print('1. Agregar compra')
        print('2. Mostrar compra')          
        print('3. Mostrar todas las compras')
        print('4. Agregar boletos a compra')
        print('5. Regresar')

    def mostrar_compra(self, record):
        print('ID:', record[0])
        print('Total de la compra:', record[1])
        print('ID Usuario:', record[2])
    
    def mostrar_compra_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def mostrar_compra_midder(self):
        print('-'*48)
    
    def mostrar_compra_footer(self):
        print('*'*48)




    def mostrar_boleto(self, record):
        print(f'{record[0]:<15}|{record[1]}|{record[2]:<6}|{record[3]:<15}|{record[4]:<15}')
     
    def mostrar_boleto_header(self):
        print('-'*70)
        print('ID Asiento'.ljust(15)+'|'+'Fecha_hora'.ljust(19)+'|'+'Precio'.ljust(6)+'|'+'Funcion'.ljust(15)+'|'+'ID Funcion'.ljust(15))
        print('-'*70)
     
    def mostrar_boleto_footer(self):
        print('-'*70)








