
import imdb

movies = {"Minari":[],"Sound of Metal":[],"Mank":[], "Promising Young Woman":[], "The Father":[], "Judas and the Black Messiah":[], "The Trial of the Chicago 7":[],"Nomadland":[]}

# creating instance of IMDb
ia = imdb.IMDb()

#buscamos los códigos/id de las películas
for i in movies:
  search = ia.search_movie(i)
  
  for j in range(len(search)):
      # getting the id
      id = search[j].movieID
      
      if search[j]['title'] == i:
        # printing it
        print(search[j]['title'] + " : " + id )
        
        #obtenemos la info de esa película
        movie = ia.get_movie(id)
        
        #Hacemos for para los que tienen varias entradas
        directors = [p['name'] for p in movie['directors']]
        cast = [movie['cast'][x]['name'] for x in range(5)]

        movies[i]={"Year":movie['year'], "Rating":movie['rating'], "Director(s)":directors,"Plot":movie['plot'], "Cast (top 5)": cast, "Genre":movie['genre'] }
        break #si aparece más de un código para esa película toma solo el primero

#print(movies)

with open("challenge.txt",'w') as challenge_file:
  for nombre, valor  in movies.items():
        challenge_file.write("%s %s\n" %(nombre, valor))
