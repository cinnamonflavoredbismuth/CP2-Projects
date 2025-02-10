#Cecily Strong Movie Recommender
"""
requierments:
Uses the provided Movies list
User is able to choose at least 2 filters for the program to search through
User can get recommendations based on genre, directors, length and/or actors 
User is able to print the whole list"""
import csv
movie={}
with open("movie_recommender\Movies list.csv") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        movie.update({"Title":row[0],
                       "Director":row[1],
                       "Genre": row[2],
                       "Rating": row[3],
                       "Length": row[4],
                       "Notable Actors":[row[5]]
                        })
        print(movie)
    print(movie)
