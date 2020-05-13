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

