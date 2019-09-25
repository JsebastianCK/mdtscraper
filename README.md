# MiraDeTodo - Web Scraper
Bajate todas las peliculas de [MiraDeTodo](www.miradetodo.net) y guardalas en una base de datos MySQL para despues hacer lo que quieras con ellas.
### ¿Que se baja?
 Pelicula
|idPelicula| nombre | anio| cantidadVotos|puntuacion|
|--|--|--|--|--|--|

linkpelicula
|idPelicula| link|
|--|--|


## Empezando
Tendras que completar todos los datos dentro del archivo config.py segun correspona
```
dbConfig = {
	"host": "localhost",	# El host de tu servidor MySQL
	"user": "",		# Tu usuario
	"passwd": "",		# Tu password
	"db": "mdtscraper",	# El nombre de la base de datos en la que vamos a guardar todo (podes cambiarlo, no pasa nada. Yo por defecto le dejo mdtscraper)
	"charset": "utf8",	# No toques esto
	"use_unicode": True 	# Esto tampoco
}
```

Luego instala las librerias dentro del requirements.txt con algun gestor de paquetes como pip.

Correlo y llenate de peliculas
```$ python main.py```
