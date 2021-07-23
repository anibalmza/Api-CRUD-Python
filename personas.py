import mysql.connector

class Personas:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="sistema")

    def __str__(self):
        datos=self.consulta_personas()  
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_personas(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM personas")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_persona(self, id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM personas WHERE id = {}".format(id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_persona(self,apellido, nombre, dni):
        cur = self.cnn.cursor()
        sql='''INSERT INTO personas (apellido, nombre, dni) 
        VALUES('{}', '{}', '{}')'''.format(apellido, nombre, dni)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_persona(self,id, apellido, nombre, dni):
        cur = self.cnn.cursor()
        sql='''UPDATE personas SET apellido='{}', nombre='{}', dni='{}' WHERE Id={}'''.format(apellido, nombre, dni, id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n

    def elimina_persona(self,id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM personas WHERE id = {}'''.format(id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n