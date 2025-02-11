#Cecily Strong Movie Recommender
"""
requierments:
Uses the provided Movies list
User is able to choose at least 2 filters for the program to search through
User can get recommendations based on genre, directors, length and/or actors 
User is able to print the whole list"""
import csv
movie={}

def display(movie):
    for titles in movie:
        print(titles)
        for categories in movie[titles]:
            print(f"    {categories}: {movie[titles][categories]}")

with open("movie_recommender\Movies list.csv") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        movie[row[0]]={
                        "Director":row[1],
                        "Genre": row[2],
                        "Rating": row[3],
                        "Length": row[4],
                        "Notable Actors":[row[5]]
                         }
    display(movie)
def filters_setup():
    title=""
    director=""
    identifiers=["director",'genre','rating','length','notable actor(s)']
    vars=[title,director,genre,rating,length,notable_actors]
    for x in identifiers:
        choose=input(f"What is the {x}? type none to skip")
        if choose.lower() != "none":

def check(filter,titles,variable,text):
        if len(variable)>0:
            if (movie[titles][text]).lower()==variable.lower():
                return(filter.append[True])
            else: return(filter.append[False])
        else:return(filter.append[True])

def search(movie,title,director,genre,rating,length,notable_actors):
    filter=[]
    search=[]

    for titles in movie:
        if len(title)>0:
            if title.lower() == titles.lower():
                filter.append[True]
            else: filter.append[False]
        else:filter.append[True]
        check(filter,titles,director,"Director")
        check(filter,titles,genre,"Genre")
        check(filter,titles,rating,"Rating")
        check(filter,titles,length,"Length")
        if len(notable_actors)>0:
            if notable_actors.lower() in (movie[titles]["Notable Actors"]).lower():
                filter.append[True]
            else: filter.append[False]
        else:filter.append[True]
        if False not in filter:
            search.append(titles)
    return(search)