from bs4 import BeautifulSoup
from movie import Movie
import admin
import requests
import os
import display

def main():
    display.bienvenida()

    # First check if db exists. If it doesn't then create it
    if not admin.checkDb():
        admin.createDb()
        check = u'\u2713'
        print 'DB: \033[92m' + check + '\033[0m'
        admin.createMovieTable()
        print 'TABLE pelicula: \033[92m' + check + '\033[0m'
        admin.createMovieLinkTable()
        print 'TABLE linkpelicula: \033[92m' + check + '\033[0m'
    else:
        check = u'\u2713'
        print 'DB: \033[92m' + check + '\033[0m'
    i = 1
    while True: 
        r = requests.get('https://miradetodo.co/page/'+str(i))
        soup = BeautifulSoup(r.content , 'html.parser')

        # Container of all movies
        contenedorDiv = soup.find('div' , {'class': 'items'})

        itemDivs = contenedorDiv.find_all('div' , {'class': 'item'})
        peliculas = []
        for itemDiv in itemDivs:
            infoDiv = itemDiv.find('div' , {'class': 'fixyear'})
            name = infoDiv.find('h2').string[0:-7]
            year = infoDiv.find('span').string
            playerLink = itemDiv.a.get('href')

            boxDiv = itemDiv.find('div' , {'class': 'boxinfo'})
            puntuacion = boxDiv.find('div' , {'class': 'cocs imdb_r'}).find('span').text
            cantVotos = boxDiv.find('div' , {'class': 'cocs imdb_r'}).find('div' , {'class': 'b'}).find_all('b')[1].text[0:-6]

            # Por ahora ignoro las series
            if playerLink.find('/series/') == -1:
                links = movieLinks(playerLink)

                pelicula = Movie({
                    'name': name,
                    'year': year,
                    'original-link': playerLink,
                    'links': links,
                    'score': puntuacion,
                    'totalVotes': cantVotos
                })
                pelicula.save()
                progreso = 'Se guardo ' + pelicula.name
                display.progress(progreso)
                print "\n"
        i = i + 1

def movieLinks(playerLink):
    r = requests.get(playerLink)
    soup = BeautifulSoup(r.content , 'html.parser')

    player = soup.find('div' , {'id': 'div2'})
    try:
        sourcesLink = player.iframe.get('data-lazy-src')
        r = requests.get(sourcesLink)
        soup = BeautifulSoup(r.content , 'html.parser')

        linksDOM = soup.find_all('a')
        links = []
        for link in linksDOM:
            links.append(link.get('href'))
        return links
    except:
        print 'No se pudo obtener los links de: '+playerLink
        return []
        
main()