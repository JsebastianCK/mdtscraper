from config import dbConfig
import MySQLdb

class Movie:

    def __init__(self, param):
        self.name = param['name']
        self.year = param['year']
        self.links = param['links']
        self.score = param['score']
        self.totalVotes = param['totalVotes'].replace(',' , '')
    
    # Guardo la pelicula en la base
    def save(self):
        db = MySQLdb.connect(**dbConfig)
        cur = db.cursor()

        command = "INSERT INTO pelicula (nombre,anio,cantidadVotos,puntuacion) VALUES( \":nombre\" , :anio , :cantidadVotos , :puntuacion )"
        command = command.replace(':nombre' , self.name)
        command = command.replace(':anio' , self.year)
        command = command.replace(':cantidadVotos' , self.totalVotes)
        command = command.replace(':puntuacion' , self.score)

        cur.execute(command)

        idpelicula = cur.lastrowid

        for link in self.links:
            command = "INSERT INTO linkpelicula (idpelicula,link) VALUES( :idpelicula , \":link\" )"
            command = command.replace(':idpelicula' , str(idpelicula))
            command = command.replace(':link' , link)
            cur.execute(command)

        db.commit()
        db.close()
    
    def toString(self):
        print "["
        print " Nombre: " + self.name
        print " Anio: " + self.year
        print " Puntuacion: " + self.score
        print " Votos totales: " + self.totalVotes
        print "]"