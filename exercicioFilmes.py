import imdb
import csv

ia = imdb.IMDb()

with open('Movies.xlsx', 'w', newline='') as csvfile:
    code = [20880628 , 10872600, 3501632, 9419884, 7131622]
   
    writer = csv.writer(csvfile)
    writer.writerow(['imdbID','tilte','year','genres','kind'])
    
    for i in range(len(code)):
        series = ia.get_movie(code[i])
        
        writer.writerow([series.data['imdbID'],series.data['title'],series.data['year'],series.data['genres'],series.data['kind']])