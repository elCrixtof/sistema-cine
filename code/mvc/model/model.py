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