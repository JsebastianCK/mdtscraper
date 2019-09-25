from config import dbConfig
import MySQLdb

# Check if database exists
def checkDb():
    config = dbConfig.copy()
    del config['db']

    db = MySQLdb.connect(**config)
    cur = db.cursor()
    
    existe = cur.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '"+ dbConfig['db'] +"'")

    db.close()

    return existe

# Creates database
def createDb():
    config = dbConfig.copy()
    del config['db']

    db = MySQLdb.connect(**config)
    cur = db.cursor()
    
    cur.execute("CREATE DATABASE " + dbConfig['db'])

    db.close()

# Check movies table schema
def checkMovieTable():
    db = MySQLdb.connect(**dbConfig)
    cur = db.cursor()
    cur.execute("SELECT * FROM pelicula LIMIT 0")
    for d in cur.description:
        print d

    db.close()

def createMovieTable():
    db = MySQLdb.connect(**dbConfig)
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE `pelicula` (
            `idPelicula` int(11) NOT NULL,
            `nombre` varchar(250) CHARACTER SET utf8 NOT NULL,
            `anio` int(4) NOT NULL,
            `cantidadVotos` int(5) NOT NULL,
            `puntuacion` decimal(4,1) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        ALTER TABLE `pelicula`
        ADD PRIMARY KEY (`idPelicula`);
        ALTER TABLE `pelicula`
        MODIFY `idPelicula` int(11) NOT NULL AUTO_INCREMENT;
    """)
    db.close()

def createMovieLinkTable():
    db = MySQLdb.connect(**dbConfig)
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE `linkpelicula` (
            `idPelicula` int(11) NOT NULL,
            `link` varchar(250) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    """)
    db.close()