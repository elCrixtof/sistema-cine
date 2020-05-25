from mysql import connector

class Model:
    """
    ********************************************
    * A data model with mysql for a cine DB *
    ********************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file 
        self.config_db = self.read_config_db() 
        self.connect_to_db() 

    def read_config_db(self):
        d = {}
        with open (self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key]=val
        return d
    
    def connect_to_db(self):
          self.cnx = connector.connect(**self.config_db)
          self.cursor = self.cnx.cursor()
    
    def close_db(self):
          self.cnx.close()
    
    """
    ************************************
    *        Metodos para salas        *
    ************************************
    """

    def crear_sala(self, s_num_filas, s_num_asientosf, s_tipo):
        try:
            sql = 'INSERT INTO salas (`s_num_filas`,`s_num_asientosf`, `s_tipo`) VALUES (%s, %s, %s)'
            vals = (s_num_filas, s_num_asientosf, s_tipo)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_sala = self.cursor.lastrowid
            return id_sala
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    def leer_una_sala(self, id_sala):
        try:
            sql = 'SELECT * FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)   
    
    def leer_todas_salas(self):
        try:
            sql = 'SELECT * FROM salas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err) 
    
    def actualizar_sala(self, fields, vals):
        try:
            sql = 'UPDATE salas SET ' + ','.join(fields)+'WHERE id_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err) 
    
    def eliminar_sala(self, id_sala):
        try:
            sql = 'DELETE FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    """
    ************************************
    *        Metodos para usuarios     *
    ************************************
    """

    def crear_usuario(self, u_pnombre, u_apellido, u_email, u_password, u_admi):
        try:
            sql = 'INSERT INTO usuarios (`u_pnombre`, `u_apellido`, `u_email`, `u_password`, `u_admin`) VALUES (%s, %s, %s, %s, %s)'
            vals = (u_pnombre, u_apellido, u_email, u_password, u_admi)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_sala = self.cursor.lastrowid
            return id_sala
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    def leer_un_usuario(self, id_usuario):
        try:
            sql = 'SELECT * FROM usuarios WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)   
    
    def leer_todos_usuarios(self):
        try:
            sql = 'SELECT * FROM usuarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_usuario(self, fields, vals):
        try:
            sql = 'UPDATE usuarios SET ' + ','.join(fields)+'WHERE id_usuario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_usuario(self, id_usuario):
        try:
            sql = 'DELETE FROM usuarios WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def leer_usuario_email_password(self, u_email, u_password):
        try:
            sql = 'SELECT * FROM usuarios WHERE u_email = %s and u_password = %s'
            vals = (u_email, u_password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    """
    ************************************
    *        Metodos para peliculas        *
    ************************************
    """

    def crear_pelicula(self, p_titulo, p_genero, p_descripcion):
            try:
                sql = 'INSERT INTO peliculas (`p_titulo`, `p_genero`, `p_descripcion`) VALUES (%s, %s, %s)'
                vals = (p_titulo, p_genero, p_descripcion)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                id_pelicula = self.cursor.lastrowid
                return id_pelicula
            except connector.Error as err:
                self.cnx.rollback()
                return(err)

    def leer_una_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_todas_peliculas(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE peliculas SET ' + ','.join(fields)+'WHERE id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_pelicula(self, id_pelicula):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
 
    """
    ************************************
    *        Metodos para funciones        *
    ************************************
    """
    # id_funcion
    # f_fecha_hora
    # f_precio
    # id_pelicula
    # id_sala

    def crear_funcion(self, f_fecha_hora, f_precio, id_pelicula, id_sala):
            try:
                sql = 'INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES (%s, %s, %s, %s)'
                vals = (f_fecha_hora, f_precio, id_pelicula, id_sala)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                id_pelicula = self.cursor.lastrowid
                return id_pelicula
            except connector.Error as err:
                self.cnx.rollback()
                return(err)
    
    def leer_una_funcion(self, id_funcion):
        try:
            sql = 'SELECT * FROM funciones WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)
    
    
    def leer_todas_funciones(self):
        try:
            sql = 'SELECT * FROM funciones'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)
    
    def leer_funciones_horario(self, inicio, fin):
        try:
            sql = 'SELECT * FROM funciones WHERE f_fecha_hora >= %s and f_fecha_hora <= %s'
            vals = (inicio,fin)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)
    
    def leer_funciones_horario_pelicula(self, inicio, fin, pelicula):
        try:
            sql = 'SELECT * FROM funciones WHERE f_fecha_hora >= %s and f_fecha_hora <= %s and id_pelicula = %s'
            vals = (inicio,fin, pelicula)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)
    
    def actualizar_funcion(self, fields, vals):
        try:
            sql = 'UPDATE funciones SET ' + ','.join(fields)+'WHERE id_funcion = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    def eliminar_funcion(self, id_funcion):
        try:
            sql = 'DELETE FROM funciones WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    

    """
    ************************************
    *        Metodos para asientos        *
    ************************************
    """
    #id_asiento
    #id_funcion
    #a_estado
    def crear_asiento(self, id_asiento,id_funcion,a_estado):
            try:
                sql = 'INSERT INTO asientos (`id_asiento`,`id_funcion`,`a_estado`) VALUES (%s, %s, %s)'
                vals = (id_asiento,id_funcion,a_estado)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                id_asiento = self.cursor.lastrowid
                return id_asiento
            except connector.Error as err:
                self.cnx.rollback()
                return(err)

    def leer_un_asiento(self, id_asiento, id_funcion):
        try:
            sql = 'SELECT * FROM asientos WHERE id_asiento = %s and id_funcion = %s' 
            vals = (id_asiento, id_funcion)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)
    
    def leer_todos_asientos(self):
        try:
            sql = 'SELECT * FROM asientos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def leer_todos_asientos_funcion(self, id_funcion):
        try:
            sql = 'SELECT * FROM asientos WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)
    
    def actualizar_asiento(self, fields, vals):
        try:
            sql = 'UPDATE asientos SET ' + ','.join(fields)+'WHERE id_asiento = %s and id_funcion = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    def eliminar_asiento(self,  id_asiento, id_funcion):
        try:
            sql = 'DELETE FROM asientos WHERE id_asiento = %s and id_funcion = %s'
            vals = (id_asiento, id_funcion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    
    """
    ************************************
    *        Metodos para compras        *
    ************************************
    """
    # id_compra
    # c_total_compra
    # id_usuario

    def crear_compra(self, c_total_compra, id_usuario):
            try:
                sql = 'INSERT INTO compras (`c_total_compra`,`id_usuario`) VALUES (%s, %s)'
                vals = (c_total_compra, id_usuario)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                id_compra = self.cursor.lastrowid
                return id_compra
            except connector.Error as err:
                self.cnx.rollback()
                return(err)

    def leer_una_compra(self, id_compra):
        try:
            sql = 'SELECT compras.*, usuarios.* FROM compras JOIN usuarios ON usuarios.id_usuario = compras.id_usuario and compras.id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_una_compra_usuario(self, id_compra, id_usuario):
        try:
            sql = 'SELECT compras.*, usuarios.* FROM compras JOIN usuarios ON usuarios.id_usuario = compras.id_usuario and compras.id_compra = %s and compras.id_usuario = %s'
            vals = (id_compra, id_usuario)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_todas_compras(self):
        try:
            sql = 'SELECT compras.*, usuarios.* FROM compras JOIN usuarios ON usuarios.id_usuario = compras.id_usuario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)
    
    def leer_todas_compras_usuario(self, id_usuario):
        try:
            sql = 'SELECT compras.*, usuarios.* FROM compras JOIN usuarios ON usuarios.id_usuario = compras.id_usuario and compras.id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_compra(self, fields, vals):
        try:
            sql = 'UPDATE compras SET ' + ','.join(fields)+'WHERE id_compra = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_compra(self, id_compra):
        try:
            sql = 'DELETE FROM compras WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    """
     ************************************
     *        Metodos Boletos             *
     ************************************
     """

    # id_asiento
    # id_funcion
    # id_compra

    

    def crear_boleto(self, id_asiento,id_funcion,id_compra):
        try:
            sql = 'INSERT INTO boletos (`id_asiento`,`id_funcion`,`id_compra`) VALUES (%s,%s,%s)'
            vals = (id_asiento,id_funcion,id_compra)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def leer_un_boleto(self, id_compra, id_asiento, id_funcion):
        try:
            sql = 'SELECT asientos.id_asiento, asientos.id_funcion, asientos.a_estado, funciones.f_precio FROM boletos JOIN asientos ON boletos.id_asiento = asientos.id_asiento and boletos.id_compra = %s and boletos.id_asiento = %s JOIN funciones ON boletos.id_funcion = funciones.id_funcion and boletos.id_funcion = %s'
            vals = (id_compra,id_asiento,id_funcion)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def leer_todos_boletos(self, id_compra):
        try:
            sql = 'SELECT asientos.id_asiento, funciones.f_fecha_hora, funciones.f_precio, peliculas.p_titulo, funciones.id_funcion FROM boletos JOIN asientos ON boletos.id_asiento = asientos.id_asiento and boletos.id_funcion = asientos.id_funcion and boletos.id_compra = %s JOIN funciones ON boletos.id_funcion = funciones.id_funcion JOIN peliculas ON funciones.id_pelicula = peliculas.id_pelicula and  funciones.id_funcion = boletos.id_funcion'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    def eliminar_boleto(self, id_asiento, id_funcion, id_compra):
        try:
            sql = 'DELETE FROM boletos WHERE id_asiento=%s and id_funcion=%s and id_compra=%s'
            vals = (str(id_asiento), int(id_funcion), int(id_compra))
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    # id_asiento
    # id_funcion
    # id_compr
 